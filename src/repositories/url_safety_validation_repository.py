from abc import ABC, abstractmethod


class IURLSafetyValidationRepository(ABC):
	@abstractmethod
	def validate_url_safety(self, long_url: str) -> bool:
		"""Call validator and validate the safety of a url"""
		pass
