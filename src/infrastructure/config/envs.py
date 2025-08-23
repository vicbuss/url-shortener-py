import os

from src.infrastructure.config.key_import import import_key

my_domain = os.getenv('DOMAIN_NAME', 'localhost:5000')
key_location = os.getenv('KEY_LOCATION', './test.key')
key = import_key(key_location)
