from abc import ABC, abstractmethod
from typing import Union


class IURLSafetyStatusRepository(ABC):
	@abstractmethod
	def save(self, url: str, is_safe: bool, ttl: int) -> None:
		pass

	@abstractmethod
	def get(self, url: str) -> Union[bool, None]:
		pass
