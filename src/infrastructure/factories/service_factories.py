from src.infrastructure.config import key, my_domain
from src.infrastructure.factories.repository_factories import (
	make_url_mapping_repository,
	make_url_safety_validation_repository,
)
from src.services.url_shortening_service import URLShorteningService
from src.services.url_validation_service import URLValidationService
from src.services.utils.slug_generation_strategy import BlowfishSlugGeneration


def make_url_validation_service() -> URLValidationService:
	url_safety_validtion_repository = make_url_safety_validation_repository()
	return URLValidationService(url_safety_validtion_repository, my_domain)


def make_url_shortening_service() -> URLShorteningService:
	url_mapping_repository = make_url_mapping_repository('memory')
	slug_generation_strategy = BlowfishSlugGeneration(key)
	return URLShorteningService(url_mapping_repository, slug_generation_strategy)
