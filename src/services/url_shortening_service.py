from typing import Union

from src.models.url_mapping import UrlMapping
from src.repositories.url_mapping_repository import (
	IURLMappingRepository,
)
from src.services.utils.slug_generation_strategy import SlugGenerationStrategy


class URLShorteningService:
	def __init__(
		self,
		url_mapping_repository: IURLMappingRepository,
		slug_generation_strategy: SlugGenerationStrategy,
	):
		self.__url_mapping_repository = url_mapping_repository
		self.__slug_generation_strategy = slug_generation_strategy

	def shorten_url(self, long_url: str) -> UrlMapping:
		incremental_id = self.__url_mapping_repository.get_id()
		slug = self.__slug_generation_strategy.generate_slug(incremental_id)
		url_mapping = UrlMapping(slug, long_url)
		self.__url_mapping_repository.save(url_mapping)

		return url_mapping

	def get_mapping(self, slug: str) -> Union[UrlMapping, None]:
		url_mapping_or_none = self.__url_mapping_repository.get(slug)

		return url_mapping_or_none
