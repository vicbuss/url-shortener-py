from flask import abort, redirect, render_template, request
from werkzeug.wrappers import Response

from src.services.url_shortening_service import URLShorteningService
from src.services.url_validation_service import URLValidationService


class RedirectController:
	def __init__(
		self,
		url_shortening_service: URLShorteningService,
		url_validation_service: URLValidationService,
	) -> None:
		self.__url_shortening_service = url_shortening_service
		self.__url_validation_service = url_validation_service

	def redirection(self, slug: str) -> str:
		url_mapping = self.__url_shortening_service.get_mapping(slug)
		if url_mapping is None:
			abort(404)

		long_url = url_mapping.long_url
		return render_template(
			'redirection_confirmation.html', slug=slug, long_url=long_url
		)

	def redirect_user(self) -> Response:
		slug = request.form['slug']
		url_mapping = self.__url_shortening_service.get_mapping(slug)

		if url_mapping is None:
			abort(404)

		long_url = url_mapping.long_url
		url_is_still_safe = self.__url_validation_service.is_valid_url(long_url)

		if not url_is_still_safe:
			abort(422)

		return redirect(long_url)
