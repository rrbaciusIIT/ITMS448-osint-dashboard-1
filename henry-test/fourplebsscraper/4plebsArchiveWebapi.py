#!/usr/bin/env python3
import json
from pprint import pprint
from typing import List

import requests
import requests_cache

from cache import install_4plebs_cache

install_4plebs_cache()

# doc from https://archive.4plebs.org/_/articles/faq/


# Interesting links:
# https://github.com/Grayson112233/python-4chan-scraper/

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
	return f"http://archive.4plebs.org/_/api/chan/post/?board={board}&num={postid}"


def gen_thread_api_url(board: str, threadid: int) -> str:
	"""Given a board and thread number, return a URL for the web API that will retrieve that thread's info."""
	return f"http://archive.4plebs.org/_/api/chan/thread/?board={board}&num={threadid}"


def extract_threadids_from_index_json(index_json: dict) -> List[int]:
	"""Given a JSON object from an index, return a list of thread IDs inside that index JSON object."""
	postids = index_json.keys()

	threadids = []

	# See if we can extract threads posts
	# Go through each post,
	for postid in postids:
		json_obj = index_json[postid]
		threadids.append(int(json_obj['op']['thread_num']))

	return threadids


def httpGET_json(url: str) -> dict:
	"""Given a URL, request content via HTTP GET and return the JSON object the request provides."""
	response = requests.get(url, headers=TOTALLY_LEGIT_HEADERS)

	data = (response.json())

	return data


if __name__ == '__main__':

	BOARD = 'pol'

	result = httpGET_json(gen_index_api_url(BOARD, 1))

	postids = result.keys()

	pprint(result)
	pprint(postids)

	print("All thread API URLs from the first page of /{}/:".format(BOARD))
	for threadid in extract_threadids_from_index_json(result):
		print(gen_thread_api_url(board=BOARD, threadid=threadid))
