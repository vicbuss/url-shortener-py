from src.infrastructure.persistence.memory_url_mapping_repository import (
	MemoryURLMappingRepository,
)
from src.repositories.url_mapping_repository import (
	IURLMappingRepository,
)


class UrlMappingRepositoryFactory:
	__registry = {'memory': lambda: MemoryURLMappingRepository()}

	@classmethod
	def create(cls, repo_type: str) -> IURLMappingRepository:
		try:
			return cls.__registry[repo_type]()
		except KeyError as err:
			raise ValueError(f'Unknown repository type: {repo_type}') from err
