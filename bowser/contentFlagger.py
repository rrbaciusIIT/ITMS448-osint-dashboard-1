import os
import re
from typing import List

import yaml

DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


class ContentFlagger:
	"""A class that can flag content as containing specific words or phrases."""

	def __init__(self, keywords: List[str], regex_matches: List[str]):
		self.match_words = keywords
		self.regex_matches = regex_matches

	def flag_content(self, content: str):

		if content is None:  # thanks for the null values json <3 i feel like i'm in Java all over again
			return False

		# Fix any issues dealing with capitalization
		content = content.lower()

		# check all our keywords
		for word in self.match_words:
			if word in content.split(" "):
				return True

		# check all our regex
		for rexp in self.regex_matches:
			if re.compile(rexp).match(content):
				return True

		return False

	@staticmethod
	def from_yaml(filepath: str):
		"""Load a ContentFlagger's rules from a YAML data file."""

		with open(filepath, 'r') as fh:
			obj = yaml.load(fh)

			return ContentFlagger(
				keywords=obj['keywords'],
				regex_matches=obj['regex_matches']
			)


ContentFlaggerRacism = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'RacismDatafile.yaml'))

ContentFlaggerHateSpeech = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'HateSpeechDatafile.yaml'))

ContentFlaggerTerrorist = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'TerrorismDatafile.yaml'))

ContentFlaggerConspiracyTheories = ContentFlagger(
	keywords=[
		'Illuminati', 'Lizard', 'some facts', 'scientology', 'satan', 'cult', 'spying'
	],

	regex_matches=[
		r'.*gate'
		r'.*ology'
	]
)
