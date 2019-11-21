from requests import Response


class WebException(Exception):  # Stolen from https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/
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


class CloudFlareSucks(WebException):
	def __init__(self, response: Response):
		self.status_code = response.status_code
		self.headers = response.headers


class InvalidUsage(WebException):
	pass
