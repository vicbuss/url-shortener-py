from typing import Union

from src.infrastructure.persistence.redis.redis_client import RedisClient
from src.repositories.url_safety_status_repository import IURLSafetyStatusRepository


class RedisURLSafetyCache(IURLSafetyStatusRepository):
	def __init__(self, client: RedisClient, namespace: str) -> None:
		super().__init__()
		self.__client = client
		self.__namespace = namespace

	def save(self, url: str, is_safe: bool, ttl: int) -> None:
		key = self.__get_key(url)
		value = str(is_safe)
		self.__client.set(key=key, value=value, ex=ttl)

	def get(self, url: str) -> Union[bool, None]:
		key = self.__get_key(url)
		value = self.__client.get(key)
		return bool(value) if value is not None else None

	def __get_key(self, key: str) -> str:
		return f'{self.__namespace}:{key}'
