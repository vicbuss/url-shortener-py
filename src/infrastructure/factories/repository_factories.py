from src.infrastructure.config import google_safe_browsing_api_key
from src.infrastructure.external.google_safe_browsing_api import GoogleSafeBrowsingAPI
from src.infrastructure.persistence.url_mapping_repository_factory import (
	UrlMappingRepositoryFactory,
)
from src.infrastructure.persistence.url_safety_repository_factory import (
	URLSafetyRepositoryFactory,
)
from src.repositories.url_mapping_repository import (
	IURLMappingRepository,
)
from src.repositories.url_safety_status_repository import IURLSafetyStatusRepository
from src.repositories.url_safety_validation_repository import (
	IURLSafetyValidationRepository,
)


def make_url_mapping_repository(type: str) -> IURLMappingRepository:
	return UrlMappingRepositoryFactory.create(type)


def make_url_safety_status_repository(type: str) -> IURLSafetyStatusRepository:
	return URLSafetyRepositoryFactory.create(type)


def make_url_safety_validation_repository() -> IURLSafetyValidationRepository:
	url_safety_status_repository = make_url_safety_status_repository('redis')
	return GoogleSafeBrowsingAPI(
		api_key=google_safe_browsing_api_key,
		url_safety_status_repository=url_safety_status_repository,
	)
