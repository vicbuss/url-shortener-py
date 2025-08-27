from flask import abort, render_template, request

from src.infrastructure.config import my_domain
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
			try:
				self.__url_validation_service.is_valid_url(original_url)

				url = my_domain
				slug = self.__url_shortening_service.shorten_url(original_url).slug
				short_url = f'{url}/{slug}'
				return render_template('shortened.html', short_url=short_url)
			except ValueError:
				abort(422)
			except Exception:
				abort(500)

		return render_template('index.html')
