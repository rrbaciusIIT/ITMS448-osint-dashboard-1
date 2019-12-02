#!/usr/bin/env python3
import io
import random
from io import StringIO
from typing import List, Union

from flask import Flask, request, url_for, jsonify, make_response, render_template
from flask_cors import CORS

from bowserHTTPExceptions import CloudFlareWAFError, InvalidUsage
from bowser4PlebsScraper import gather_range_with_boards
from bowserRedditScraper import grab_subreddit, grab_threadlist
from bowserUtils import BOARDS_4PLEBS
from contentFlagger import ALL_CONTENT_FLAGGERS, ContentFlagger
from csvWriter import CSVPostWriter, JSONPostWriter

app = Flask(__name__, static_folder="../client/build/static", template_folder="../client/build/")
CORS(app)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error: InvalidUsage):
	# Stolen from https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response


@app.errorhandler(CloudFlareWAFError)
def handle_cloudflare_error(error: CloudFlareWAFError):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response


def list_routes_dangerous(app: Flask, prefix='') -> List[str]:
	"""
	Get a list of routes this app can serve.

	Stolen from https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app :)
	This is insecure for larger apps as it exposes implementation details. This is just for convenience.
	"""

	routes = []

	for rule in app.url_map.iter_rules():
		routes.append('{prefix}{routename}'.format(
			prefix=prefix,
			routename=rule)
		)

	return routes


def get_base_url_dangerous() -> str:
	return request.scheme + "://" + request.host


@app.route("/api")
def index():
	return jsonify({
		"message": "Welcome to the Bowser OSINT Web API! This is the index! See /routes/ for routes.",
		"read-more-url": "https://github.com/Team-Bowser-ITMS-448/ITMS448-osint-dashboard/",
		"route-url": url_for("routes"),
		"example-urls": [
			(url_for('generate_csv') + "?boards=x,pol&flaggers=NSA_PRISM,TERRORISM&start_page=3&stop_page=10"),
			(url_for(
				'generate_4plebs_json') + "?boards=pol,s4s,x&flaggers=NSA_ECHELON,RACISM&start_page=1&stop_page=3"),
			(url_for('generate_reddit_json') + '?subreddit=Sino'),
		]
	})


def parameter_blacklist(param: object, name: str, desc: str, disallowed_values=[None, '', ['']]) -> object:
	"""Restrict param from being inside disallowed_values."""
	for badvalue in disallowed_values:
		if param == badvalue:
			raise InvalidUsage({
				"error": "Missing required parameter!",
				"required_parameter": name,
				'bad_value': param,
				"desc": desc,
			})

	return param


def parameter_must_be_numeric(param: object, name: str, desc: str,
							  klass: Union[int, float, complex] = int) -> Union[int, float, complex]:
	try:
		val = klass(param)

		return val

	except (ValueError, TypeError):
		raise InvalidUsage({
			'error': "Parameter is not in the proper numeric format!",
			"required_parameter": name,
			'bad_value': param,
			'desc': desc,
		})


def parameters_must_be_inside_list(params: List[object], allowed: List[object], desc: str) -> List[object]:
	"""Require that params' elements be only comprised of elements inside the 'allowed' list."""

	for item in params:
		if item not in allowed:
			raise InvalidUsage({
				'error': "Parameter is not allowed to be this value!",
				"allowed_values": allowed,
				"bad_value": item,
				"all_values": params,
				"desc": desc
			})

	return params


def unpack_http_get_list(string: str) -> Union[List[str], None]:
	"""Given a comma-separated string, turn it into a list of strings.
	Useful for allowing lists over HTTP GET parameters"""
	if string is None:
		return None

	if ',' in string:  # TODO: Enforce HTTP POST to avoid this ugly interface.
		return string.split(',')
	else:
		return [string]


@app.route("/api/health")
def health():
	return jsonify({
		"status": "online"
	})


@app.route("/api/routes")
def routes():
	return jsonify({
		"desc": "This is a list of routes available to you to consume.",
		"routes": list_routes_dangerous(app=app)
	})


def content_flagger_names() -> List[str]:
	"""Names of all content flaggers."""
	return [cf.name for cf in ALL_CONTENT_FLAGGERS]


def content_flagger_name_to_ContentFlagger(name: str) -> ContentFlagger:
	"""Given a name, return a ContentFlagger by that name."""
	for cf in ALL_CONTENT_FLAGGERS:
		if cf.name == name:
			return cf

	raise ValueError("No content flagger by {} found!".format(name))


def content_flagger_names_to_ContentFlaggers(names: List[str]) -> List[ContentFlagger]:
	"""Given a list of names, return a list of ContentFlaggers by those names."""

	cfs = []
	for name in names:
		cfs.append(content_flagger_name_to_ContentFlagger(name))
	return cfs


@app.route("/api/show/4chan/boards")
def boards():
	return jsonify({"boards": BOARDS_4PLEBS})


@app.route("/api/show/4chan/content-flaggers")
def content_flaggers():
	"""List of allowed content flagger names"""

	d = {}

	for cf in ALL_CONTENT_FLAGGERS:
		d[cf.name] = cf.description

	return jsonify(d)


@app.route("/api/generate/reddit/json", methods=['GET'])
def generate_reddit_json():
	subredditDesc = "The subreddit you wish to gather posts from"
	subreddit = request.args.get("subreddit")
	subreddit = parameter_blacklist(subreddit, 'subreddit', subredditDesc)

	subredditResponse = grab_subreddit(subreddit)
	threadlist = grab_threadlist(subredditResponse)

	return jsonify({"subreddit": subreddit,
					'subreddit_response': subredditResponse,
					'thread_list': threadlist})


def _generate_csv_string_4plebs(boards: str, flaggers: str, start_page: str, stop_page: str) -> str:
	boardsDesc = "The boards on 4chan you wish to gather from."
	boards = unpack_http_get_list(boards)
	boards = parameter_blacklist(boards, 'boards', boardsDesc)
	boards = parameters_must_be_inside_list(boards, BOARDS_4PLEBS, boardsDesc)
	print(boards)

	flaggerDesc = "The names of content flaggers to use. See {} for supported names.".format(
		url_for('content_flaggers'))
	flaggers = unpack_http_get_list(flaggers)
	flaggers = parameter_blacklist(flaggers, 'flaggers', flaggerDesc)
	flaggers = parameters_must_be_inside_list(flaggers, content_flagger_names(), flaggerDesc)
	print(flaggers)

	start_page = parameter_must_be_numeric(start_page, 'start_page',
										   "The page of the imageboard's board to start gathering from.")
	print(start_page)

	stop_page = parameter_must_be_numeric(stop_page, 'stop_page',
										  "The page of the imageboard's board to finish gathering from.")
	print(stop_page)

	stringInputStream = io.StringIO()

	posts = gather_range_with_boards(start=start_page, end=stop_page, boards=boards)

	CSVPostWriter.write_posts_to_stream(threads=posts,
										stream=stringInputStream,
										content_flaggers=content_flagger_names_to_ContentFlaggers(flaggers))
	# TODO: use their content flagger selections!

	return stringInputStream.getvalue()


@app.route("/api/generate/4chan/csv", methods=['GET'])
def generate_csv():
	boards = request.args.get('boards', None)
	flaggers = request.args.get('flaggers', None)
	start_page = request.args.get('start_page', None)
	stop_page = request.args.get('stop_page', None)

	csvString = _generate_csv_string_4plebs(
		boards=boards,
		flaggers=flaggers,
		start_page=start_page,
		stop_page=stop_page,
	)

	output = make_response(csvString)
	print('wow10:', output)
	output.headers["Content-Disposition"] = "attachment; filename=export.csv"
	output.headers["Content-type"] = "text/csv"
	output.headers["charset"] = 'utf-8'

	return output


@app.route("/api/generate/4chan/json", methods=['GET'])
def generate_4plebs_json():
	csvString = _generate_csv_string_4plebs(
		boards=request.args.get('boards', None),
		flaggers=request.args.get('flaggers', None),
		start_page=request.args.get('start_page', None),
		stop_page=request.args.get('stop_page', None),
	)

	return jsonify(JSONPostWriter.convert_csv_string_to_json(csvString))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')


if __name__ == '__main__':
	# app.run(host='0.0.0.0', port=3001)
	app.run(host='0.0.0.0', port=1839)
