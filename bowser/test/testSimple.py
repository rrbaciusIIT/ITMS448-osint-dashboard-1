import os
import signal
import unittest

import requests

from cache import install_4plebs_cache, get_cache_filename


class timeout:
	"""
	Stolen from https://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish
	"""

	def __init__(self, seconds=1, error_message='Timeout'):
		self.seconds = seconds
		self.error_message = error_message

	def handle_timeout(self, signum, frame):
		raise TimeoutError(self.error_message)

	def __enter__(self):
		signal.signal(signal.SIGALRM, self.handle_timeout)
		signal.alarm(self.seconds)

	def __exit__(self, type, value, traceback):
		signal.alarm(0)


def testCacheWorks(seconds_if_uncached=50):
	"""
	This should not take too long if the cache works.

	:param seconds_if_uncached: How many seconds this would take without caching.
	"""
	install_4plebs_cache()
	print("Testing if the request cache works.")
	for i in range(0, seconds_if_uncached):
		print(requests.get('http://httpbin.org/delay/1'))


class TestCache(unittest.TestCase):

	def tearDown(self) -> None:
		os.remove(get_cache_filename())

	def testCache(self):
		try:
			with timeout(seconds=25):
				testCacheWorks(seconds_if_uncached=100)

		except TimeoutError:
			self.fail("Timed out. Requests cache is not working.")
