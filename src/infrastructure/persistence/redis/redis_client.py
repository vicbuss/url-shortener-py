from __future__ import annotations

import time
from typing import Callable

import redis
from redis.exceptions import ConnectionError, TimeoutError

def with_retry(func: Callable) -> Callable: # type: ignore
    def wrapper(self, *args, **kwargs) -> Any: # type: ignore
        for _ in range(self.max_retries):
            try:
                return func(self, *args, **kwargs)
            except (ConnectionError, TimeoutError):
                time.sleep(0.5)
        raise ConnectionError(f"Redis operation '{func.__name__}' failed after {self.max_retries} attempts")
    return wrapper

class RedisClient:
    __instance: RedisClient | None = None

    def __new__(
        cls,
        host: str = 'localhost',
        port: int = 6379,
        password: str | None = None,
        db: int = 0,
        max_retries: int = 3,
        socket_timeout: int = 5,
    ) -> RedisClient:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__init_pool(
                host, port, password, db, max_retries, socket_timeout
            )
        return cls.__instance

    def __init_pool(
        self,
        host: str,
        port: int,
        password: str | None,
        db: int,
        max_retries: int,
        socket_timeout: int,
    ) -> None:
        self.max_retries = max_retries
        self.client = redis.Redis(
            host=host,
            port=port,
            password=password,
            db=db,
            socket_timeout=socket_timeout,
            socket_connect_timeout=socket_timeout,
            decode_responses=True,
            retry_on_timeout=True,
        )

    @with_retry
    def set(
        self,
        key: str,
        value: str,
        ex: int | None = None,
        exat: int | None = None,
        nx: bool = False,
        xx: bool = False,
    ) -> bool:
        res: bool = self.client.set(
            name=key, value=value, ex=ex, exat=exat, nx=nx, xx=xx
        )
        return res

    @with_retry
    def get(self, key: str) -> str | None:
        res: str | None = self.client.get(key)
        return res
    
    @with_retry
    def delete(self, *keys: str) -> None:
        self.client.delete(keys)
    
    @with_retry
    def exists(self, key: str) -> bool:
        matches: int = self.client.exists(key)
        return matches > 0

    def increment(self, key: str, amount: int = 1) -> int:
        counter: int = self.client.incr(key, amount)
        return counter
    
    @with_retry
    def expire(self, key: str, ttl_sec: int, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False) -> bool:
        set_expire: bool = self.client.expire(key, ttl_sec, nx, xx, gt, lt)
        return set_expire

