from src.infrastructure.factories.repository_factories import (
	make_url_mapping_repository,
	make_url_safety_validation_repository,
)
from src.services.url_shortening_service import URLShorteningService
from src.services.url_validation_service import URLValidationService
from src.infrastructure.config import my_domain

def make_url_validation_service() -> URLValidationService:
	url_safety_validtion_repository = make_url_safety_validation_repository()
	return URLValidationService(url_safety_validtion_repository, my_domain)


def make_url_shortening_service() -> URLShorteningService:
	url_mapping_repository = make_url_mapping_repository('memory')
	return URLShorteningService(url_mapping_repository)
