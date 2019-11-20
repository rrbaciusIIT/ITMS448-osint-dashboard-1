import os
import re
from typing import List

import yaml

DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


class ContentFlagger:
	"""A class that can flag content as containing specific words or phrases."""

	def __init__(self, name: str, keywords: List[str], regex_matches: List[str], description: str = None):

		self.name = name
		'''Content flagger's name.'''

		self.match_words = keywords
		'''A list of keywords that match content.'''

		self.regex_matches = regex_matches
		'''A list of regex matches that flag content.'''

		self.description = description
		'''The description of the flagger.'''

	@property
	def csv_description(self):
		return '[content flagger] ' + self.description

	def flag_content(self, content: str):

		if content is None:  # thanks for the null values json <3 i feel like i'm in Java all over again
			return False

		# Fix any issues dealing with capitalization
		content = content.lower()

		# check all our keywords
		for word in self.match_words:
			word = str(word).lower()
			if word in content.split(" "):  # split by spaces -- word must be padded by spaces
				return True

		# check all our regex
		for rexp in self.regex_matches:
			if re.compile(rexp).match(content):
				return True

		return False

	@staticmethod
	def from_yaml(filepath: str, **kwargs):
		"""Load a ContentFlagger's rules from a YAML data file."""

		with open(filepath, 'r') as fh:
			obj = yaml.safe_load(fh)

			keywords = obj.get('keywords', [])
			regex_matches = obj.get('regex_matches', [])
			description = obj.get('description', 'no description')
			name = obj.get('name', 'NONAME')

			return ContentFlagger(
				name=name,
				keywords=keywords,
				regex_matches=regex_matches,
				description=description,
			)


ContentFlaggerRacism = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'RacismDatafile.yaml'))

ContentFlaggerHateSpeech = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'HateSpeechDatafile.yaml'))

ContentFlaggerTerrorist = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'TerrorismDatafile.yaml'))

ContentFlaggerConspiracyTheories = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'ConspiracyTheoriesDatafile.yaml'))

ContentFlaggerPRISM = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'BUSINESS_INSIDER_NSA_PRISM_KEYWORDS.yaml'))

ContentFlaggerECHELON = ContentFlagger.from_yaml(
	os.path.join(DATA_DIRECTORY, 'THEREGISTER_ECHELON_TRIGGER_WORDS.yaml'))

ALL_CONTENT_FLAGGERS: List[ContentFlagger] = [
	ContentFlaggerRacism, ContentFlaggerHateSpeech,
	ContentFlaggerTerrorist, ContentFlaggerConspiracyTheories,
	ContentFlaggerPRISM, ContentFlaggerECHELON
]
