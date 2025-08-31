from typing import Callable, Dict

from src.infrastructure.factories.singleton_factories import get_redis_client
from src.infrastructure.persistence.memory_url_mapping_repository import (
	MemoryURLMappingRepository,
)
from src.infrastructure.persistence.redis.redis_url_mapping_repository import (
	RedisURLMappingRepository,
)
from src.repositories.url_mapping_repository import (
	IURLMappingRepository,
)


class UrlMappingRepositoryFactory:
	__registry: Dict[str, Callable[[], IURLMappingRepository]] = {
		'memory': lambda: MemoryURLMappingRepository(),
		'redis': lambda: RedisURLMappingRepository(
			client=get_redis_client(),
			namespace='slug',
			tti_sec=30 * 24 * 60 * 60,  # TTI = One month
		),
	}

	@classmethod
	def create(cls, repo_type: str) -> IURLMappingRepository:
		try:
			return cls.__registry[repo_type]()
		except KeyError as err:
			raise ValueError(f'Unknown repository type: {repo_type}') from err
