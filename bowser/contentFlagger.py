import re
from typing import List


class ContentFlagger:
	"""A class that can flag content as containing specific words or phrases."""

	def __init__(self, keywords: List[str], regex_matches: List[str]):
		self.match_words = keywords
		self.regex_matches = regex_matches

	def flag_content(self, content: str):

		if content is None:  # thanks for the null values json <3 i feel like i'm in Java all over again
			return False

		# check all our keywords
		for word in self.match_words:
			if word in content:
				return True

		# check all our regex
		for rexp in self.regex_matches:
			if re.compile(rexp).match(content):
				return True

		return False


ContentFlaggerBadWords = ContentFlagger(
	keywords=['fuck', 'shit'],
	regex_matches=['f(.|)ck'],
)

ContentFlaggerTerrorist = ContentFlagger(
	keywords=['bomb', 'assault', 'nuke', 'nuclear', 'gun', 'assassin', 'kill', 'president', 'chemical', 'poison',
	          'virus', 'merc'],
	regex_matches=[],
)
