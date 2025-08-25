import ipaddress
import socket
from urllib.parse import urljoin, urlparse

import requests

from src.repositories.url_safety_validation_repository import (
	IURLSafetyValidationRepository,
)
from src.services.decorators import cache_url_validation


class URLValidationService:
	def __init__(
		self,
		url_safety_validation_repository: IURLSafetyValidationRepository,
		my_domain: str,
	) -> None:
		self.__url_safety_validation_repository = url_safety_validation_repository
		self.__my_domain = my_domain

	def __is_unsafe_host(self, hostname: str) -> bool:
		try:
			infos = socket.getaddrinfo(hostname, None)
		except socket.gaierror:
			raise

		for _, _, _, _, sockaddr in infos:
			ip_str = sockaddr[0]
			ip = ipaddress.ip_address(ip_str)

			if (
				ip.is_private
				or ip.is_loopback
				or ip.is_link_local
				or ip.is_reserved
				or ip.is_multicast
			):
				return True

		return False

	def __is_unsafe_url(self, url: str) -> bool:
		parsed = urlparse(url)
		host = parsed.hostname
		return (
			parsed.scheme not in ('http', 'https')
			or not host
			or host == self.__my_domain
			or self.__is_unsafe_host(host)
		)

	def __safe_resolve_url(self, url: str, max_redirects: int = 5) -> str:
		parsed = urlparse(url)
		if parsed.scheme not in ('http', 'https'):
			raise ValueError(f'Unsupported URL scheme: {parsed.scheme}')

		for _ in range(max_redirects):
			resp = requests.head(url, allow_redirects=False, timeout=5)

			if 300 <= resp.status_code < 400:
				location = resp.headers.get('Location')
				if not location:
					break

				url = urljoin(url, location)

				url_is_unsafe = self.__is_unsafe_url(url)

				if url_is_unsafe:
					raise ValueError(f'Redirect blocked, unsafe url: {url}')
			else:
				url_is_unsafe = self.__is_unsafe_url(url)
				if url_is_unsafe:
					raise ValueError(f'Unsafe url: {url}')
				return url
		raise ValueError('Too many redirects or unsafe chain')

	@cache_url_validation(10 * 60, 2 * 60, 1 * 60)
	def is_valid_url(self, url: str) -> bool:
		try:
			resolved_url = self.__safe_resolve_url(url)
			is_safe = self.__url_safety_validation_repository.validate_url_safety(
				resolved_url
			)

			if not is_safe:
				raise ValueError(f'Unsafe URL: {url}')

			return True

		except Exception as e:
			raise ValueError(f'URL validation failed: {e}') from e
