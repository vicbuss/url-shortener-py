import base64
import struct
from abc import ABC, abstractmethod
from typing import Union

from Crypto.Cipher import Blowfish


class SlugGenerationStrategy(ABC):
	@abstractmethod
	def generate_slug(self, input: int) -> str:
		pass


class BlowfishSlugGeneration(SlugGenerationStrategy):
	def __init__(self, key: Union[bytes, None]):
		super().__init__()
		self.__key = key

	def generate_slug(self, input: int) -> str:
		if self.__key is None:
			raise RuntimeError('Encryption key not loaded')
		cipher = Blowfish.new(self.__key, Blowfish.MODE_ECB)

		block = struct.pack('>Q', input)

		encrypted = cipher.encrypt(block)

		slug = base64.urlsafe_b64encode(encrypted).rstrip(b'=')
		slug_str = slug.decode('ascii')

		return slug_str
