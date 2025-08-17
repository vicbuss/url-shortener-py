from flask import abort, render_template, request

from src.services.url_shortening_service import URLShorteningService
from src.services.url_validation_service import URLValidationService


class URLController:
	def __init__(
		self,
		url_validation_service: URLValidationService,
		url_shortening_service: URLShorteningService,
	):
		self.__url_validation_service = url_validation_service
		self.__url_shortening_service = url_shortening_service

	def shorten(self) -> str:
		if request.method == 'POST':
			original_url = request.form['original_url']
			url_is_safe = self.__url_validation_service.validate_url(
				original_url
			)
			if not url_is_safe:
				abort(422)

			slug = self.__url_shortening_service.shorten_url(original_url)
			short_url = f'http://127.0.0.1:5000/{slug}'
			return render_template('shortened.html', short_url=short_url)

		return render_template('index.html')
