import random
from typing import List

from flask import Flask, jsonify

app = Flask(__name__)


def list_routes(app: Flask) -> List[str]:
	"""
	Get a list of routes this app can serve.

	Stolen from https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app :)
	This is insecure for larger apps as it exposes implementation details. This is just for convenience.
	"""

	routes = []

	for rule in app.url_map.iter_rules():
		routes.append('%s' % rule)

	return routes


@app.route("/")
def index():
	nums = [random.randint(0, 100) for i in range(10)]

	return jsonify({
		"message": "Default route! See /routes/ for routes.",
		"lucky-numbers": nums
	})


@app.route("/routes")
def routes():
	return jsonify(list_routes(app=app))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1839)
