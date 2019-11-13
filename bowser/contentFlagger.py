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


ContentFlaggerRacism = ContentFlagger(
	keywords=['TODO'],

	regex_matches=['TODO'],
)

ContentFlaggerBadWords = ContentFlagger(
	keywords=[
		'nigger', 'negro', 'niglet', 'shitskin',
		'kike', 'jew', 'shekel', 'uss liberty',
		'chink', 'slanty eye',
		'gas', 'genocide', 'final solution',
		'cuck', 'soyboy',
		'scum', 'degenerate', 'crusade',
		'tranny', 'homo', 'queer', 'attack helicopter',
		'pepe', 'groyper', 'goyper',
		'maga', 'magapede',
		'pizzagate',
	],

	regex_matches=[
		r'\({2,}.&\){2,}',
		r'she{1,}i{1,}t',
		r'anti[.|]white'
		r'deep[.|]state'
		r'nationalis[tm]'
		r'wipe. out',
		r'birth[.|]rate',
		r'fag(|got)',
		r'f[.|]ck',
	],
)

ContentFlaggerTerrorist = ContentFlagger(
	keywords=[
		'bomb', 'assault', 'nuke', 'nuclear', 'gun',
		'kill', 'president', 'chemical', 'poison', 'virus',
		'merc', 'suicide', 'IED', 'weapon', 'terror', 'cartel',
		'breach', 'NSA', 'radio'],

	regex_matches=[
		r'(love if|someone (should|will|)) \w{1,10} (sho{1,2}t|bomb)',
		r'assassin(|ate(|d))'
	],
)
