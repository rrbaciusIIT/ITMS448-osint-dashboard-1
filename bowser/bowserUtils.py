import datetime
from json import JSONDecodeError
from pprint import pprint

import cloudscraper
from requests import Response

from bowserHTTPExceptions import CloudFlareWAFError

cloudScraper = cloudscraper.create_scraper()

TOTALLY_LEGIT_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
				  'Chrome/50.0.2661.102 Safari/537.36 '
}

BOARDS_4PLEBS = ['adv', 'f', 'hr', 'o', 'pol', 's4s', 'sp', 'tg', 'trv', 'tv', 'x']
'''All boards that 4plebs serves.
This is hardcoded as I could not find a way to programmatically retrieve it.'''

ESCAPE_TABLE = {
	# "&": "&amp;",
	'"': "&quot;",
	"'": "&apos;",
	# ">": "&gt;",
	# "<": "&lt;",
	',': "&#44;",
	'\n': '\\n',
	'\r': '\\r',
}

UNESCAPE_TABLE = {}

for k, v in ESCAPE_TABLE.items():
	UNESCAPE_TABLE[v] = k


def epoch_to_ISO8601(epoch: int) -> str:
	return datetime.datetime.fromtimestamp(epoch).strftime("%Y%m%dT%H%M%S")


def csv_safe_string(string: str, escape_table=None) -> str:
	if string is None:
		return ""

	if escape_table is None:
		escape_table = ESCAPE_TABLE

	for badchar, goodchar in escape_table.items():
		string = string.replace(badchar, goodchar)

	return string


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
			raise CloudFlareWAFError(message="Cloudflare very likely is blocking this app from using a service.",
									 status_code=response.status_code,
									 payload={'headers': dict(response.headers),
											  'url': response.url,
											  'reason': response.reason,
											  'status': response.status_code,
											  'history': response.history,
											  'raw_content:': response.content.decode(response.encoding)})

		raise Exception("Response from {url} gave {sc} != 200!".format(url=url, sc=response.status_code, ),
						response.headers,
						json,
						response.reason,
						response.raw)

	data = (response.json())

	return data
