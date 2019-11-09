#!/usr/bin/env python3
import copy
import os
import csv
from pprint import pprint
from typing import List, Dict

import requests

from cache import install_4plebs_cache

install_4plebs_cache()

TOTALLY_LEGIT_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
	              'Chrome/50.0.2661.102 Safari/537.36 '
}

HTML_ESCAPE_TABLE = {
	"&": "&amp;",
	'"': "&quot;",
	"'": "&apos;",
	">": "&gt;",
	"<": "&lt;",
	',': "&#44;",
	'\n': '\\n',
}


def csv_safe_string(string: str, html_escape_table_opt=None) -> str:
	if html_escape_table_opt is None:
		html_escape_table_opt = HTML_ESCAPE_TABLE

	for badchar, goodchar in html_escape_table_opt.items():
		string = string.replace(badchar, goodchar)

	return string


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
	def comment(self):

		comment = self._json['op']['comment']

		if comment is None:  # no comment, just a subject and a picture
			return ""
		else:
			return comment

	@property
	def comment_escaped_newline(self):
		"""A comment with no newlines."""
		return self.comment.replace('\n', '\\n')

	@property
	def should_flag_content(self):
		return \
			(should_flag_content(self.comment) or
			 should_flag_content(self.title))

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
	response = requests.get(url, headers=TOTALLY_LEGIT_HEADERS)

	if not response.status_code == 200:
		raise Exception("Response from {} gave {} != 200!".format(url, response.status_code))

	data = (response.json())

	return data


class CSVPostWriter:
	@staticmethod
	def write_posts_to_csv(posts: List[FourPlebsAPI_Post], filepath: str) -> None:

		# Ensure that enclosing directory exists
		if not os.path.exists(os.path.dirname(filepath)):
			os.makedirs(os.path.dirname(filepath))

		if not filepath.split('.')[-1] == 'csv':
			raise Exception("File doesn't end in `csv`!")

		with open(filepath, 'w', newline='') as csvfile:

			# Fields we want to save in the CSV
			fieldnames = [
				'board',
				'post_id',
				'post_url',
				'thread_id',
				'thread_url',
				'short_comment',
				'full_comment',
				'thread_api_url',
				'post_api_url',
			]

			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

			for post in posts:
				writer.writerow({
					'board': post.board_code,
					'post_id': post.post_id,
					'post_url': post.gen_post_url(),
					'post_api_url': post.gen_post_api_url(),
					'thread_id': post.thread_num,
					'thread_url': post.gen_thread_url(),
					'thread_api_url': post.gen_thread_api_url(),
					'short_comment': csv_safe_string(post.short_comment),
					'full_comment': csv_safe_string(post.comment),
				})

		print("Enjoy your CSV file located at {} with {} rows!".format(
			os.path.abspath(filepath),
			len(posts) + 1,
		))


if __name__ == '__main__':

	# Get the posts from page 1 /pol/
	results = httpGET_json(gen_index_api_url('pol', 1))

	# Add on the posts from page 1 /x/
	results.update(**httpGET_json(gen_index_api_url('x', 1)))

	# Turn that json dict into a list of Post objects
	frontPagePosts = FourPlebsAPI_Post.from_post_json(results)

	# For all posts from the two index pages (/x/, /pol/)
	for post in frontPagePosts:
		print(post)

	CSVPostWriter.write_posts_to_csv(frontPagePosts, 'out/post-output.csv')
