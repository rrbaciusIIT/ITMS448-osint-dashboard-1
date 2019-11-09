# -*- coding: utf-8 -*-
from pprint import pprint
from typing import List

import scrapy
from scrapy import Selector


class AArchivedMoeSpider(scrapy.Spider):
	name = 'archived.moe'
	allowed_domains = ['archived.moe']
	start_urls = ['https://archived.moe/pol/']

	POST_CONTROLS_SELECTOR = 'header > .post_data > .post_controls'

	def parse(self, response):
		print("Hi! I'm parsing a response!")

		for item in response.css(self.POST_CONTROLS_SELECTOR):
			item: Selector

			# print("Here's the whole thing:")
			# pprint(item.get())

			post_matches: List[str] = item.re(r'href=".+?/thread/\d+?/"')

			if len(post_matches) is not 0:
				pprint(post_matches)

			# post_url = item.re('').get()
			#
			#
			# print("Just the URL link:")
			# pprint(post_url)
