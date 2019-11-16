import unittest

		# No bad words!
		self.assertTrue(cfn.flag_content('faggot'))
		self.assertTrue(cfn.flag_content('tranny'))

	def test_custom_contentflagger(self):
		customcf = ContentFlagger(
			regex_matches=[r'abc \d\d\d'],
			keywords=['potato']
		)

		# ABC digit digit digit should get flagged
		self.assertTrue(customcf.flag_content('abc 234'))
		self.assertTrue(customcf.flag_content('abc 111'))
		self.assertTrue(customcf.flag_content('abc 300'))

		# this contains 'potato', a keyword.
		self.assertTrue(customcf.flag_content('  a sdffdas afsdafds asdf asdfafsd asdf asdf !! potato !! asdfafsd asdfafsdasdf '))

		# only 2 digits. shouldn't match.
		self.assertFalse(customcf.flag_content('abc 12X'))
