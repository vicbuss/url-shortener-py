from src.infrastructure.factories.repository_factories import (
	make_url_mapping_repository,
)
from src.services.url_shortening_service import URLShorteningService
from src.services.url_validation_service import URLValidationService


def make_url_validation_service() -> URLValidationService:
	return URLValidationService()


def make_url_shortening_service() -> URLShorteningService:
	url_mapping_repository = make_url_mapping_repository('memory')
	return URLShorteningService(url_mapping_repository)
