import unittest

from contentFlagger import ContentFlaggerHateSpeech, ContentFlagger, ContentFlaggerTerrorist, ContentFlaggerRacism, \
	ContentFlaggerPRISM, ContentFlaggerECHELON


class ContentFlaggerTests(unittest.TestCase):

	def test_terrorism_contentflagger(self):
		cft = ContentFlaggerTerrorist

		self.assertTrue(
			cft.flag_content('someone should fuckin shoot the paper targets at the range and not a real person'))
		self.assertTrue(cft.flag_content('i will bomb the test'))
		self.assertTrue(cft.flag_content('i will assault this website with good intentions'))

	def test_hate_speech(self):
		cfn = ContentFlaggerHateSpeech

		# No bad words!
		self.assertTrue(cfn.flag_content('faggot'))
		self.assertTrue(cfn.flag_content('tranny'))

	def test_racism(self):
		cfr = ContentFlaggerRacism

		self.assertTrue(cfr.flag_content('nigga'))
		self.assertTrue(cfr.flag_content('nigger'))
		self.assertTrue(cfr.flag_content('niggers'))

	def testPRISM(self):
		cfp = ContentFlaggerPRISM

		self.assertTrue(cfp.flag_content('shipment of plutonium'))

	def testECHELON(self):

		cfe = ContentFlaggerECHELON

		self.assertFalse(cfe.flag_content('I'))
		self.assertFalse(cfe.flag_content('am'))
		self.assertFalse(cfe.flag_content('the'))
		self.assertFalse(cfe.flag_content('a'))
		self.assertFalse(cfe.flag_content('he'))
		self.assertFalse(cfe.flag_content('she'))
		self.assertFalse(cfe.flag_content('we'))
		self.assertFalse(cfe.flag_content('go'))

	def test_custom_contentflagger(self):
		customcf = ContentFlagger(
			regex_matches=[r'abc \d\d\d'],
			keywords=['potato'],
			keywords_case_sensitive=True,  # case sensitive
			name=''
		)

		# ABC digit digit digit should get flagged
		self.assertTrue(customcf.flag_content('abc 234'))
		self.assertTrue(customcf.flag_content('abc 111'))
		self.assertTrue(customcf.flag_content('abc 300'))

		# this contains 'potato', a keyword.
		self.assertTrue(
			customcf.flag_content('  a sdffdas afsdafds asdf asdfafsd asdf asdf !! potato !! asdfafsd asdfafsdasdf '))

		# it is case sensitive, so it should not flag this:
		self.assertFalse(customcf.flag_content("Potato pOtato potatO"))

		# only 2 digits. shouldn't match.
		self.assertFalse(customcf.flag_content('abc 12X'))
