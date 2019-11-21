#!/usr/bin/env python3
from json import JSONDecodeError
from pprint import pprint
from typing import List, Dict

import cloudscraper
from requests import Response

from bowserHTTPAPI import CloudFlareSucks
from bowserUtils import csv_safe_string, gen_index_api_url, gen_post_api_url, gen_thread_api_url, \
	gen_thread_url, gen_post_url
from cache import install_4plebs_cache
from contentFlagger import ALL_CONTENT_FLAGGERS
from csvWriter import CSVPostWriter

cloudScraper = cloudscraper.create_scraper()

BOARDS_4PLEBS = ['adv', 'f', 'hr', 'o', 'pol', 's4s', 'sp', 'tg', 'trv', 'tv', 'x']
'''All boards that 4plebs serves.
This is hardcoded as I could not find a way to programmatically retrieve it.'''

install_4plebs_cache()


# TODO: This really should be called 'FourPlebsAPI_Thread'.
#       The reason we sub-index at 'op' is that I didn't fully understand the return type of the
#       JSON response I got from the 4plebs API.
class FourPlebsAPI_Post:
	"""
	Constructor to access properties of 4plebs API response objects.

	Not necessary per se but makes interacting with 4plebs API response objects easier.
	"""

	@classmethod
	def from_post_json(cls, post_json: Dict[int, Dict]):
		"""Construct a list of FourPlebsAPI_Post objects from a JSON response containing {id, post} pairs."""

		pprint(post_json.keys())

		posts = []

		for postid, jsonObject in post_json.items():
			post = FourPlebsAPI_Post(postid, jsonObject)
			posts.append(post)

		# # If this post has more posts after it, add them all.
		# if 'posts' in jsonObject:
		#
		# 	subPosts = jsonObject['posts']
		# 	del subPosts[0]  # This is the OP, we don't need it.
		#
		# 	if len(subPosts) > 0:
		#
		# 		for subPost in subPosts:
		# 			print("FUCK")
		#
		# 			post_api_url = gen_post_api_url(board=subPost['board']['shortname'], postid=subPost['doc_id'])
		#
		# 			post_resp = httpGET_json(post_api_url)
		#
		# 			# if 'error' in post_resp:
		# 			# 	if post_resp['error']=='Post not found.':
		#
		# posts.append(cls.from_post_json({post_resp["num"]: post_resp}))
		#
		# posts += cls.from_post_json(jsonObject['posts'])

		return posts

	def __init__(self, id: int, json: dict):
		"""
		:rtype: FourPlebsAPI_Post
		"""
		self._json = json
		self.post_id = id

	@property
	def board_code(self):
		"""Short board code, i.e. 'x' or 'pol'."""
		return self._json['op']['board']['shortname']

	@property
	def poster_country(self) -> str:
		return self._json['op']['poster_country']

	@property
	def timestamp(self) -> int:
		return self._json['op']['timestamp']

	@property
	def comment(self):

		comment = self._json['op']['comment']

		if comment is None:  # no comment, just a subject and a picture
			return ""
		else:
			return comment

	@property
	def subposts(self) -> List[Dict]:
		if 'posts' in self._json:

			# The web API we use may or may not return a list or dict, depending on certain factors.
			# This code ensures it is consistent.
			if isinstance(self._json['posts'], list):
				return self._json['posts']

			elif isinstance(self._json['posts'], dict):
				return list(self._json['posts'].values())

			else:
				raise Exception("posts in object is neither list nor dictionary! This should never happen!")
		else:
			return []

	@property
	def comment_escaped_newline(self):
		"""A comment with no newlines."""
		return self.comment.replace('\n', '\\n')

	@property
	def comment_csv_safe(self):
		"""A comment safe for CSV files."""

		return csv_safe_string(self.comment)

	@property
	def title(self):

		title = self._json['op']['title']

		if title is None:  # No title
			return ""
		else:
			return title

	@property
	def short_comment(self, maxlen=100):

		if len(self.comment) > maxlen:
			retComment = self.comment_escaped_newline[0:maxlen]
		else:
			retComment = self.comment_escaped_newline + "(...)"

		return retComment

	@property
	def thread_num(self):
		"""Thread number."""
		return self._json['op']['thread_num']

	def gen_post_api_url(self):
		return gen_post_api_url(self.board_code, self.post_id)

	def __str__(self):
		return ''' >> {klassname} << 
	Post ID: {postid}
	Thread #: {threadnum}
	Post Title: {posttitle}
	OP Comment: {comment}
	Post URL: {posturl}
	Thread URL: {threadurl}
	Post API URL: {postapiurl}
	'''.format(
			klassname=self.__class__.__name__,
			postid=self.post_id,
			posttitle=self.title,
			threadnum=self.thread_num,
			posturl=self.gen_post_url(),
			threadurl=self.gen_thread_url(),
			postapiurl=self.gen_post_api_url(),
			comment=self.short_comment
		)

	def gen_post_url(self):
		return gen_post_url(self.board_code, self.thread_num, self.post_id)

	def gen_thread_url(self):
		return gen_thread_url(self.board_code, self.thread_num)

	def gen_thread_api_url(self):
		return gen_thread_api_url(self.board_code, self.thread_num)


def extract_threadnums_from_index_json(index_json: dict) -> List[int]:
	"""Given a JSON object from an index, return a list of thread IDs inside that index JSON object."""
	postids = index_json.keys()

	threadnums = []

	# See if we can extract threads posts
	# Go through each post,
	for postid in postids:
		json_obj = index_json[postid]
		threadnums.append(int(json_obj['op']['thread_num']))

	return threadnums


def httpGET_json(url: str) -> dict:
	"""Given a URL, request content via HTTP GET and return the JSON object the request provides."""
	response: Response = cloudScraper.get(url)

	if (not response.status_code == 200):

		print("response that is not HTTP OK:")
		pprint(response)

		# See if it has json
		try:
			json = response.json()
		except JSONDecodeError:
			json = ''

		if (response.headers.get('server') == 'cloudflare') and ('CF-RAY' in response.headers):
			raise CloudFlareSucks(message="Cloudflare very likely is blocking this app from using a service.",
								  status_code=response.status_code,
								  payload={'headers': dict(response.headers),
										   'url': response.url,
										   'reason': response.reason,
										   'status': response.status_code,
										   'history': response.history,
										   'raw_content:':response.content})

		raise Exception("Response from {url} gave {sc} != 200!".format(url=url, sc=response.status_code, ),
						response.headers,
						json,
						response.reason,
						response.raw)

	data = (response.json())

	return data


def gather_range_with_boards(start: int, end: int, boards: List[str]) -> List[FourPlebsAPI_Post]:
	"""Given a start and end page range, gather posts from various boards."""
	results = {}

	for i in range(start, end):
		for board in boards:
			results.update(**httpGET_json(gen_index_api_url(board, i)))

			print("Page {} of /{}/".format(i, board))

	return FourPlebsAPI_Post.from_post_json(results)


def generate_large_example_csv(page_start=1, page_end=20, boards=['pol', 'x']):
	postList = gather_range_with_boards(page_start, page_end, boards)

	CSVPostWriter.write_posts_to_csv(postList, 'out/post-output-large.csv', ALL_CONTENT_FLAGGERS)


def generate_small_example_csv():
	results = {}

	# Add a specific thread, http://archive.4plebs.org/x/thread/23732801/
	results.update(**httpGET_json(gen_thread_api_url('x', 23732801)))

	for i in range(1, 10):
		# Get the posts from page 1-10 /pol/
		results.update(**httpGET_json(gen_index_api_url('pol', i)))

	# Add on the posts from page 1 /x/
	results.update(**httpGET_json(gen_index_api_url('x', 1)))

	# Turn that json dict into a list of Post objects
	postList = FourPlebsAPI_Post.from_post_json(results)

	# # For all posts from the two index pages (/x/, /pol/)
	# for post in postList:
	# 	print(post)

	CSVPostWriter.write_posts_to_csv(postList, 'out/post-output-small-example.csv', ALL_CONTENT_FLAGGERS)


if __name__ == '__main__':
	print("Making small CSV file...")
	generate_small_example_csv()

	# If you're a data analyst and want to tweak your search queries easily, edit the arguments below!
	print("Making LARGE CSV file...")
	generate_large_example_csv(page_start=1, page_end=150, boards=['pol', 'x'])
