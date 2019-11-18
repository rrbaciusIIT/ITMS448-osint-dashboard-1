import os
import shutil
import unittest

from bowserScraper import httpGET_json, FourPlebsAPI_Post, CSVPostWriter
from bowserUtils import gen_index_api_url, gen_thread_api_url
from contentFlagger import ALL_CONTENT_FLAGGERS


class TestCSVFile(unittest.TestCase):

	def tearDown(self) -> None:
		if os.path.exists('out'):
			shutil.rmtree('out')

	def testSmallCSVFile(self):
		results = {}

		# Add a specific thread, http://archive.4plebs.org/x/thread/23732801/
		results.update(**httpGET_json(gen_thread_api_url('x', 23732801)))

		# First page of /x/
		results.update(**httpGET_json(gen_index_api_url('x', 1)))

		# Turn that json dict into a list of Post objects
		postList = FourPlebsAPI_Post.from_post_json(results)

		CSVPostWriter.write_posts_to_csv(postList, 'out/testcase-output-small-example.csv', ALL_CONTENT_FLAGGERS)

		i = 0
		# All lines in this CSV should contain commas!
		with open('out/testcase-output-small-example.csv', 'r') as f:
			for line in f:
				print("line {}".format(i))
				self.assertIn(',', line)

				i += 1


if __name__ == '__main__':
	unittest.main()
