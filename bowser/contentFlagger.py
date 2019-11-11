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
	keywords = [
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

	regex_matches = [
				'\({2,}.&\){2,}',
				'she{1,}i{1,}t',
				'anti.white'
				'deep.state'
				'nationalis[tm]'
				'wipe. out',
				'birth.rate', 
				'fag(|got)',
			],
)

ContentFlaggerTerrorist = ContentFlagger(
	keywords = [
			'bomb', 'assault', 'nuke', 'nuclear', 'gun', 'assassin', 'kill', 'president', 'chemical', 'poison', 
			'virus', 'merc', 'suicide', 'IED', 'weapon', 'terror', 'cartel', 'breach', 'NSA', 'radio'],

	regex_matches = [
				'(love if|someone (should|will|)) \w{1,10} (sho{1,2}t|bomb)',
			'],
)
