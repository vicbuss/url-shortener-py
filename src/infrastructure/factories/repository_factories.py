from src.infrastructure.persistence.mock_url_safety_validation_repository import (
	MockURLSafetyValidationRepository,
)
from src.infrastructure.persistence.url_mapping_repository_factory import (
	UrlMappingRepositoryFactory,
)
from src.repositories.url_mapping_repository import (
	IURLMappingRepository,
)
from src.repositories.url_safety_validation_repository import (
	IURLSafetyValidationRepository,
)


def make_url_mapping_repository(type: str) -> IURLMappingRepository:
	return UrlMappingRepositoryFactory.create(type)


def make_url_safety_validation_repository() -> IURLSafetyValidationRepository:
	return MockURLSafetyValidationRepository()
