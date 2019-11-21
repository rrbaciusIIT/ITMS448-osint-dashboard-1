import datetime

TOTALLY_LEGIT_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
				  'Chrome/50.0.2661.102 Safari/537.36 '
}

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


def epoch_to_human_date(epoch: int) -> str:
	return datetime.datetime.fromtimestamp(epoch).strftime('%c')


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
