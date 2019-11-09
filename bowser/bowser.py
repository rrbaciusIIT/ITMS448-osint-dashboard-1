#!/usr/bin/env python3
from pprint import pprint
from typing import List, Dict

import requests

from cache import install_4plebs_cache

install_4plebs_cache()

TOTALLY_LEGIT_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
	              'Chrome/50.0.2661.102 Safari/537.36 '
}


def should_flag_content(content: str) -> bool:
	"""Should this content be flagged?"""
	# TODO This is naive
	return 'fuck' in content


def gen_index_api_url(board: str, page: int) -> str:
	"""Given a board and page number, return a URL for the web API that will retrieve that index page's posts."""
	return "http://archive.4plebs.org/_/api/chan/index/?board={board}&page={page}".format(
		board=board,
		page=page,
	)


def gen_post_api_url(board: str, postid: int) -> str:
	"""Given a board and post number, return a URL for the web API that will retrieve that post's info."""
	return "http://archive.4plebs.org/_/api/chan/post/?board={board}&num={postid}".format(
		board=board,
		postid=postid,
	)


def gen_thread_api_url(board: str, threadnum: int) -> str:
	"""Given a board and thread number, return a URL for the web API that will retrieve that thread's info."""
	return "http://archive.4plebs.org/_/api/chan/thread/?board={board}&num={threadnum}".format(
		board=board,
		threadnum=threadnum
	)


def gen_thread_url(board: str, threadnum: int) -> str:
	"""Given a board and thread number, return a human-readable forum URL for the thread."""
	return "http://archive.4plebs.org/{board}/thread/{threadnum}/".format(
		board=board,
		threadnum=threadnum,
	)


def gen_post_url(board: str, threadnum: int, postid: int) -> str:
	"""Given a board, thread number, and post id, return a human-readable URL for the post in that thread."""
	return "http://archive.4plebs.org/{board}/thread/{threadnum}/#{postid}".format(
		board=board,
		threadnum=threadnum,
		postid=postid,
	)


class FourPlebsAPI_Post:
	"""
	Constructor to access properties of 4plebs API response objects.

	Not necessary per se but makes interacting with 4plebs API response objects easier.
	"""

	@classmethod
	def from_post_json(cls, post_json: Dict[int, Dict]):
		"""Construct a list of FourPlebsAPI_Post objects from a JSON response containing {id, post} pairs."""

		posts = []

		for id, jsonObject in post_json.items():
			post = FourPlebsAPI_Post(id, jsonObject)
			posts.append(post)

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
	def comment(self):

		comment = self._json['op']['comment']

		if comment is None:  # no comment, just a subject and a picture
			return ""
		else:
			return comment

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
			retComment = self.comment[0:maxlen]
		else:
			retComment = self.comment + "(...)"

		retComment = retComment.replace('\n', '\\n')

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
	response = requests.get(url, headers=TOTALLY_LEGIT_HEADERS)

	if not response.status_code == 200:
		raise Exception("Response from {} gave {} != 200!".format(url, response.status_code))

	data = (response.json())

	return data


if __name__ == '__main__':

	result = httpGET_json(gen_index_api_url('pol', 1))

	posts = FourPlebsAPI_Post.from_post_json(result)

	for post in posts:
		print(post)

	pprint(post._json)
