import requests_cache

CACHE_NAME = '4plebs_scraper_cache'
CACHE_BACKEND = 'sqlite'


def get_cache_filename() -> str:
	return '{}.{}'.format(CACHE_NAME, CACHE_BACKEND)


def install_4plebs_cache(expire=60):
	"""Enables a cache for requests."""
	# Cache for rapid querying that lasts 60 seconds.
	requests_cache.install_cache(CACHE_NAME, backend=CACHE_BACKEND, expire_after=expire)
