from abc import ABC, abstractmethod
from typing import Union

from src.models.user import User


class IUsersRepository(ABC):
	@abstractmethod
	def find_by_username(self, username: str) -> Union[User, None]:
		pass

	@abstractmethod
	def save(self, user: User) -> None:
		pass
