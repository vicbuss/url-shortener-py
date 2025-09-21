import os

from dotenv import load_dotenv

from src.infrastructure.config.key_import import import_key
from src.infrastructure.persistence.redis.r_credentials import RedisCredentials

load_dotenv()

my_domain = os.getenv('DOMAIN_NAME', 'localhost:5000')

slug_key_location = os.getenv('SLUG_KEY_LOCATION', './test.key')
slug_key = import_key(slug_key_location)

session_key_location = os.getenv('SESSION_KEY_LOCATION', './session.key')
session_key = import_key(session_key_location)

redis_host = os.getenv('REDIS_HOST', '127.0.0.1')
redis_port = os.getenv('REDIS_PORT', '6379')
redis_password = os.getenv('REDIS_PWD', None)

redis_credentials = RedisCredentials(redis_host, int(redis_port), redis_password)

google_safe_browsing_api_key = os.getenv('SAFE_BROWSING_KEY', '')
