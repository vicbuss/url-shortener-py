from typing import Callable, Dict

from src.infrastructure.persistence.memory.memory_users_repository import (
	MemoryUsersRepository,
)
from src.repositories.users_repository import IUsersRepository


class UsersRepositoryFactory:
	__registry: Dict[str, Callable[[], IUsersRepository]] = {
		'memory': lambda: MemoryUsersRepository()
	}

	@classmethod
	def create(cls, repo_type: str) -> IUsersRepository:
		try:
			return cls.__registry[repo_type]()
		except KeyError as err:
			raise ValueError(f'Unknown repository type: {repo_type}') from err
