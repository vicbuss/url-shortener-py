from src.repositories.url_safety_validation_repository import (
	IURLSafetyValidationRepository,
)


class MockURLSafetyValidationRepository(IURLSafetyValidationRepository):
	def __init__(self) -> None:
		super().__init__()

	def validate_url_safety(self, long_url: str) -> bool:
		return True
