from typing import Union

from src.models.repositories.url_mapping_repository import (
	IUrlMappingRepository,
)
from src.models.url_mapping import UrlMapping


class URLShorteningService:
	def __init__(self, url_mapping_repository: IUrlMappingRepository):
		self.__url_mapping_repository = url_mapping_repository

	def shorten_url(self, long_url: str) -> UrlMapping:
		slug = 'abc123'
		url_mapping = UrlMapping(slug, long_url)
		self.__url_mapping_repository.save(url_mapping)

		return url_mapping

	def get_mapping(self, slug: str) -> Union[UrlMapping, None]:
		url_mapping_or_none = self.__url_mapping_repository.get(slug)

		return url_mapping_or_none
