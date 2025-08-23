from typing import Union


def import_key(key_path: str) -> Union[bytes, None]:
	try:
		with open(key_path, 'rb') as f:
			key = f.read()
			return key
	except FileNotFoundError:
		return None
