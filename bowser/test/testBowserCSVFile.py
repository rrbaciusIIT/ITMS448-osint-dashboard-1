from typing import IO

import os
import shutil
import unittest

from bowser4PlebsScraper import FourPlebsAPI_Post, CSVPostWriter
from bowserUtils import gen_index_api_url, gen_thread_api_url, httpGET_json
from contentFlagger import ALL_CONTENT_FLAGGERS


class TestCSVFile(unittest.TestCase):

	def ensure_csv_has_no_empty_fields(self, csvFile: IO, delim: str = ',', count=2):
		"""Given a CSV file, make sure it does not have any empty fields."""

		empty_delim = delim * count  # two consecutive delimiters. i.e. ',,'

		for line in csvFile.readlines():
			self.assertNotIn(empty_delim, line)  # line should not have 2 commas consecutively

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

		output_csv_filepath = 'out/testcase-output-small-example.csv'
		CSVPostWriter.write_posts_to_csv(postList, output_csv_filepath, ALL_CONTENT_FLAGGERS)

		i = 0
		# All lines in this CSV should contain commas!
		with open(output_csv_filepath, 'r') as f:
			for line in f:
				print("line {}".format(i))
				self.assertIn(',', line)

				i += 1

		with open(output_csv_filepath, 'r') as f:
			self.ensure_csv_has_no_empty_fields(f, count=4)


if __name__ == '__main__':
	unittest.main()
