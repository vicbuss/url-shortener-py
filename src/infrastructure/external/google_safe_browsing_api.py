from dataclasses import asdict
from urllib.parse import urlparse

import requests

from src.infrastructure.external.safe_browsing_payload import (
	Client,
	SafeBrowsingPayload,
	ThreatEntry,
	ThreatInfo,
)
from src.infrastructure.external.safe_browsing_response import ThreatMatchesResponse
from src.repositories.url_safety_validation_repository import (
	IURLSafetyValidationRepository,
)


class GoogleSafeBrowsingAPI(IURLSafetyValidationRepository):
	def __init__(self, api_key: str) -> None:
		super().__init__()
		self.__api_key = api_key
		self.__safe_browsing_url = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={self.__api_key}'

	def validate_url_safety(self, long_url: str) -> bool:
		url = self.__get_protocol_and_domain(long_url)
		payload = SafeBrowsingPayload(
			client=Client(
				clientId='vicbuss-url-shortener-project', clientVersion='1.0.0'
			),
			threatInfo=ThreatInfo(
				threatTypes=[
					'MALWARE',
					'SOCIAL_ENGINEERING',
					'POTENTIALLY_HARMFUL_APPLICATION',
				],
				platformTypes=['ANY_PLATFORM'],
				threatEntryTypes=['URL'],
				threatEntries=[ThreatEntry(url=url)],
			),
		)

		payload_dict = asdict(payload)

		try:
			response = requests.post(self.__safe_browsing_url, json=payload_dict)
			response.raise_for_status()

			data = response.json()
			if not data:
				return True
			
			threatMatchData: ThreatMatchesResponse = data

			matches = data['matches']


			return False
		except requests.exceptions.HTTPError as e:
			status = e.response.status_code if e.response else 'unknown'
			raise RuntimeError(f'HTTP error {status}: {e.response.text}') from e
		except requests.exceptions.RequestException as e:
			raise RuntimeError(f'Request failed: {e}') from e

	def __get_protocol_and_domain(self, url: str) -> str:
		parsed = urlparse(url)
		return f'{parsed.scheme}://{parsed.hostname}'
