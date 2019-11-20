import csv
import io
import random
from typing import List

from flask import Flask, request, url_for, jsonify, make_response

app = Flask(__name__)


class InvalidUsage(Exception):  # Stolen from https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/
	status_code = 400

	def __init__(self, message, status_code=None, payload=None):
		Exception.__init__(self)
		self.message = message
		if status_code is not None:
			self.status_code = status_code
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or ())
		rv['message'] = self.message
		return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):  # Stolen from https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/
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


@app.route("/")
def index():
	nums = [random.randint(0, 100) for i in range(10)]

	return jsonify({
		"message": "Welcome to the Bowser OSINT Web API! This is the index! See /routes/ for routes.",
		"read-more-url": "https://github.com/Team-Bowser-ITMS-448/ITMS448-osint-dashboard/",
		"route-url": url_for("routes"),
		"lucky-numbers": nums
	})


def required_parameter(param: object, name: str, disallowed_values={None}):
	for badvalue in disallowed_values:
		if param is badvalue:
			raise InvalidUsage("'{}' is a required parameter, but it was {}!".format(name, badvalue))


@app.route("/routes")
def routes():
	return jsonify(list_routes_dangerous(app=app))


@app.route("/generate/csv", methods=['GET'])
def generate_csv():
	boards = request.args.get('boards', None)
	required_parameter(boards, 'boards')

	data = [
		['name', 'amount', 'price'],
		['apple', '3', '2'],
		['banana', '2', '4'],
	]

	si = io.StringIO()
	cw = csv.writer(si)
	cw.writerows(data)

	output = make_response(si.getvalue())
	output.headers["Content-Disposition"] = "attachment; filename=export.csv"
	output.headers["Content-type"] = "text/csv"

	return output


if __name__ == '__main__':
	# app.run(host='0.0.0.0', port=1839)
	app.run(host='0.0.0.0', port=3000)
