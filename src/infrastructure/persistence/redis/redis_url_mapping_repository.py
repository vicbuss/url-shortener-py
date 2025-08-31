from typing import Union

from src.infrastructure.persistence.redis.redis_client import RedisClient
from src.models.url_mapping import UrlMapping
from src.repositories.url_mapping_repository import IURLMappingRepository


class RedisURLMappingRepository(IURLMappingRepository):
	def __init__(self, client: RedisClient, namespace: str, tti_sec: int) -> None:
		super().__init__()
		self.__client = client
		self.__namespace = namespace
		self.__tti = tti_sec

	def save(self, url_mapping: UrlMapping) -> None:
		slug = url_mapping.slug
		url = url_mapping.long_url
		key = self.__get_key(slug)

		self.__client.set(key=key, value=url, ex=self.__tti)

	def get(self, slug: str) -> Union[UrlMapping, None]:
		key = self.__get_key(slug)
		res: Union[str, None] = self.__client.get(key=key)

		if res is not None:
			self.__client.expire(key=key, ttl_sec=self.__tti)
			return UrlMapping(slug=slug, long_url=res)

		return None

	def get_id(self) -> int:
		key = self.__get_key('counter')
		counter = self.__client.increment(key=key)

		return counter

	def __get_key(self, key: str) -> str:
		return f'{self.__namespace}:{key}'
