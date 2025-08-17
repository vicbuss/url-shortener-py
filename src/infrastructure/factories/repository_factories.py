from src.infrastructure.persistence.url_mapping_repository_factory import (
	UrlMappingRepositoryFactory,
)
from src.models.repositories.url_mapping_repository import (
	IUrlMappingRepository,
)


def make_url_mapping_repository(type: str) -> IUrlMappingRepository:
	return UrlMappingRepositoryFactory.create(type)
