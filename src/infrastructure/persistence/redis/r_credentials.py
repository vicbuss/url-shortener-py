from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class RedisCredentials:
	host: str
	port: int
	password: Union[str, None] = None
