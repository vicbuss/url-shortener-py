from typing import Dict, Union

from src.models.user import User
from src.repositories.users_repository import IUsersRepository


class MemoryUsersRepository(IUsersRepository):
	def __init__(self) -> None:
		self.__data: Dict[str, User] = {}

	def save(self, user: User) -> None:
		id = user.username
		self.__data[id] = user

	def find_by_username(self, username: str) -> Union[User, None]:
		return self.__data.get(username)
