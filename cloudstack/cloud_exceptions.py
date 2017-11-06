
import json

__all__ = ['CloudException']


class CloudException(Exception):
	def __init__(self, http_exc):
		self.code = http_exc.code
		try:
			message = http_exc.headers['X-Description']
		except KeyError:
			response = http_exc.fp.read()
			try:
				message = list(json.loads(response).values())[0]['errortext']
			except ValueError:
				message = response
		Exception.__init__(self,  message)
