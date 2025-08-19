from abc import ABC, abstractmethod
from typing import Union

from src.models.url_mapping import UrlMapping


class IURLMappingRepository(ABC):
	@abstractmethod
	def save(self, url_mapping: UrlMapping) -> None:
		"""Save slug and long_url_pair"""
		pass

	@abstractmethod
	def get(self, slug: str) -> Union[UrlMapping, None]:
		"""Return Url Mapping if found"""
		pass
