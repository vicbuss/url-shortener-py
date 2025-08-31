from typing import Union

from src.infrastructure.config import redis_credentials
from src.infrastructure.persistence.redis.redis_client import RedisClient

_redis_client: Union[RedisClient, None] = None


def get_redis_client() -> RedisClient:
	global _redis_client
	if _redis_client is None:
		_redis_client = RedisClient(
			host=redis_credentials.host,
			port=int(redis_credentials.port),
			password=redis_credentials.password,
		)
	return _redis_client
