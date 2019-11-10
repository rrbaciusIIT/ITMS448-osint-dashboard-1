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


def testCacheWorks():
	"""This should not take 50 seconds if the cache works."""
	install_4plebs_cache()
	print("Testing if the request cache works.")
	for i in range(0, 10):
		print(requests.get('http://httpbin.org/delay/5'))


class TestCache(unittest.TestCase):

	def tearDown(self) -> None:
		os.remove(get_cache_filename())

	def testCache(self):
		try:
			# This should not take longer than 6 seconds.
			with timeout(seconds=6):
				testCacheWorks()

		except TimeoutError:
			self.fail("Timed out. Requests cache is not working.")
