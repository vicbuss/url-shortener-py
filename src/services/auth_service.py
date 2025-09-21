from typing import Union

from src.models.user import User
from src.repositories.users_repository import IUsersRepository


class AuthenticationSevice:
	def __init__(self, users_repository: IUsersRepository) -> None:
		self.__users_repository = users_repository

	def check_username_availability(self, username: str) -> bool:
		return self.__users_repository.find_by_username(username) is None

	def register(self, username: str, password: str, role: str = 'user') -> None:
		user = User(username=username, password=password, role=role, hashPwd=True)
		self.__users_repository.save(user)

	def validate_credentials(self, username: str, password: str) -> Union[User, None]:
		user = self.__users_repository.find_by_username(username)
		return user if user and user.verify_password(password) else None
