#!/usr/bin/env bash

# Scrapy stuff is from:
#
# https://medium.com/better-programming/develop-your-first-web-crawler-in-python-scrapy-6b2ee4baf954
# https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
#
#

# Runs the spider that scrapes archived.moe of posts.

scrapy runspider testScrapyProject/testScrapyProject/spiders/aarchivedmoe.py