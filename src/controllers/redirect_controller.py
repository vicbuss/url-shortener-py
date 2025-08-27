from flask import abort, redirect, render_template, request
from werkzeug.wrappers import Response

from src.services.url_shortening_service import URLShorteningService
from src.services.url_validation_service import URLValidationService
from src.services.utils.service_errors import NotFoundError


class RedirectController:
	def __init__(
		self,
		url_shortening_service: URLShorteningService,
		url_validation_service: URLValidationService,
	) -> None:
		self.__url_shortening_service = url_shortening_service
		self.__url_validation_service = url_validation_service

	def redirection(self, slug: str) -> str:
		try:
			url_mapping = self.__url_shortening_service.get_mapping(slug)

			long_url = url_mapping.long_url
			return render_template(
				'redirection_confirmation.html', slug=slug, long_url=long_url
			)
		except NotFoundError:
			abort(404)
		except Exception:
			abort(500)

	def redirect_user(self) -> Response:
		try:
			slug = request.form['slug']
			url_mapping = self.__url_shortening_service.get_mapping(slug)

			long_url = url_mapping.long_url
			self.__url_validation_service.is_valid_url(long_url)

			return redirect(long_url)

		except ValueError:
			abort(422)
		except NotFoundError:
			abort(404)
		except Exception:
			abort(500)
