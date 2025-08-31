import os

from dotenv import load_dotenv

from src.infrastructure.config.key_import import import_key
from src.infrastructure.persistence.redis.r_credentials import RedisCredentials

load_dotenv()

my_domain = os.getenv('DOMAIN_NAME', 'localhost:5000')
key_location = os.getenv('KEY_LOCATION', './test.key')
key = import_key(key_location)

redis_host = os.getenv('REDIS_HOST', '127.0.0.1')
redis_port = os.getenv('REDIS_PORT', '6379')
redis_password = os.getenv('REDIS_PWD', None)

redis_credentials = RedisCredentials(redis_host, int(redis_port), redis_password)

google_safe_browsing_api_key = os.getenv('SAFE_BROWSING_KEY', '')
