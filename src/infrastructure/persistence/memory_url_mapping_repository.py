from typing import Dict, Union

from src.models.repositories.url_mapping_repository import (
	IUrlMappingRepository,
)
from src.models.url_mapping import UrlMapping


class MemoryURLMappingRepository(IUrlMappingRepository):
	__data: Dict[str, str] = {}

	def save(self, url_mapping: UrlMapping) -> None:
		slug = url_mapping.slug
		long_url = url_mapping.long_url

		self.__data[slug] = long_url

	def get(self, slug: str) -> Union[UrlMapping, None]:
		long_url = self.__data.get(slug)
		return UrlMapping(slug, long_url) if long_url is not None else None
