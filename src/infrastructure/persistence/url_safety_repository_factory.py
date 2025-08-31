from typing import Callable, Dict

from src.infrastructure.factories.singleton_factories import get_redis_client
from src.infrastructure.persistence.redis.redis_url_safety_cache import (
	RedisURLSafetyCache,
)
from src.repositories.url_safety_status_repository import IURLSafetyStatusRepository


class URLSafetyRepositoryFactory:
	__registry: Dict[str, Callable[[], IURLSafetyStatusRepository]] = {
		'redis': lambda: RedisURLSafetyCache(
			client=get_redis_client(), namespace='url_safety'
		)
	}

	@classmethod
	def create(cls, repo_type: str) -> IURLSafetyStatusRepository:
		try:
			return cls.__registry[repo_type]()
		except KeyError as err:
			raise ValueError(f'Unknown repository type: {repo_type}') from err
