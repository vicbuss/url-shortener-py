import functools
import time
from typing import Any, Callable, Dict, Optional, Tuple, TypeVar

F = TypeVar('F', bound=Callable[..., bool])


CacheValue = Tuple[Optional[bool], float, Optional[Exception]]


def cache_url_validation(
	ttl_valid: int,
	ttl_unsafe: int,
	ttl_error: int,
	prune_interval: float = 60.0,
) -> Callable[[F], F]:
	def decorator(func: F) -> F:
		cache: Dict[str, CacheValue] = {}
		last_prune: float = 0.0

		@functools.wraps(func)
		def wrapper(*args: Any, **kwargs: Any) -> bool:
			nonlocal last_prune
			now = time.time()

			if now - last_prune > prune_interval:
				for cached_url, (_, expires_at, _) in list(cache.items()):
					if now >= expires_at:
						del cache[cached_url]
				last_prune = now

			if 'url' in kwargs:
				url = kwargs['url']
			else:
				url = args[1] if len(args) > 1 else args[0]

			if not isinstance(url, str):
				raise TypeError("Expected 'url' to be a str")

			if url in cache:
				value, expires_at, cached_exc = cache[url]
				if now < expires_at:
					if cached_exc:
						raise cached_exc

					return bool(value)

			try:
				value = func(*args, **kwargs)
				ttl = ttl_valid
				exc: Optional[Exception] = None
			except ValueError as ve:
				value = None
				ttl = ttl_unsafe
				exc = ve
			except Exception as e:
				value = None
				ttl = ttl_error
				exc = e

			cache[url] = (value, now + ttl, exc)

			if exc:
				raise exc

			assert value is not None
			return value

		return wrapper  # type: ignore[return-value]

	return decorator
