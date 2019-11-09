import re
from typing import List


class ContentFlagger:
	"""A class that can flag content as containing specific words or phrases."""

	def __init__(self, keywords: List[str], regex_matches: List[str]):
		self.match_words = keywords
		self.regex_matches = regex_matches

	def flag_content(self, content: str):

		# check all our keywords
		for word in self.match_words:
			if word in content:
				return True

		# check all our regex
		for rexp in self.regex_matches:
			if re.compile(rexp).match(content):
				return True

		return False


def ContentFlaggerBadWords():
	return ContentFlagger(
		keywords=['fuck', 'shit'],
		regex_matches=['f(.|)ck'],
	)


def ContentFlaggerTerrorist():
	return ContentFlagger(
		keywords=['bomb', 'assault'],
		regex_matches=['todo \:\)'],
	)
