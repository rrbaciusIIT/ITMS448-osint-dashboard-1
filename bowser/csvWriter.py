import csv
import os
from typing import List

from bowserScraper import FourPlebsAPI_Post
from bowserUtils import epoch_to_human_date, csv_safe_string, gen_post_api_url, gen_thread_api_url, gen_thread_url, \
	gen_post_url

from contentFlagger import ContentFlagger


class CSVPostWriter:
	@staticmethod
	def write_posts_to_csv(posts: List[FourPlebsAPI_Post], filepath: str,
						   content_flaggers: List[ContentFlagger] = None) -> None:
		"""
		:param posts: The list of posts to save.
		:param filepath: The filepath of the CSV scraper.
		:param content_flaggers: Optional. The list of ContentFlagger objects that should flag posts.
			Use ALL_CONTENT_FLAGGERS to use all content flaggers that are defined by default.
		:return:
		"""

		# Ensure that enclosing directory exists
		if not os.path.exists(os.path.dirname(filepath)):
			os.makedirs(os.path.dirname(filepath))

		if not filepath.split('.')[-1] == 'csv':
			raise Exception("File doesn't end in `csv`!")

		with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:

			# Fields we want to save in the CSV
			fieldnames = [
				'board',
				'post_id',
				'post_url',
				'thread_id',
				'thread_url',
				'full_comment',
				'thread_api_url',
				'post_api_url',
				'op',
				'country_code',
				'timestamp_epoch',
				'timestamp',
			]
			# Add our flagger descriptions
			fieldnames += [flagger.csv_description for flagger in content_flaggers]

			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

			for post in posts:
				writer.writerow({
					'board': post.board_code,
					'post_id': post.post_id,
					'post_url': post.gen_post_url(),
					'post_api_url': post.gen_post_api_url(),
					'thread_id': post.thread_num,
					'thread_url': post.gen_thread_url(),
					'thread_api_url': post.gen_thread_api_url(),
					'country_code': post.poster_country,
					'full_comment': csv_safe_string(post.comment),
					'op': True,
					'timestamp': epoch_to_human_date(post.timestamp),
					'timestamp_epoch': post.timestamp,
				})

				# for every flagger, apply its analysis to the post's comment
				for flagger in content_flaggers:
					writer.writerow({
						flagger.csv_description: flagger.flag_content(post.comment)
					})

				for subpost in post.subposts:
					# TODO: Find a more elegant way to process these subposts! This is duplicated code!

					# print("Subpost:")
					# print(subpost)

					writer.writerow({
						'board': subpost['board']['shortname'],
						'post_id': subpost['num'],
						'post_url': gen_post_url(subpost['board']['shortname'], subpost['thread_num'], subpost['num']),
						'post_api_url': gen_post_api_url(subpost['board']['shortname'], subpost['num']),
						'thread_id': subpost['thread_num'],
						'thread_url': gen_thread_url(subpost['board']['shortname'], subpost['thread_num']),
						'thread_api_url': gen_thread_api_url(subpost['board']['shortname'], subpost['thread_num']),
						'country_code': subpost['poster_country'],
						'full_comment': csv_safe_string(subpost['comment']),
						'op': False,
						'timestamp': epoch_to_human_date(subpost['timestamp']),
						'timestamp_epoch': subpost['timestamp'],
					})

					# for every flagger, apply its analysis to the subpost's comment
					for flagger in content_flaggers:
						writer.writerow({
							flagger.csv_description: flagger.flag_content(subpost['comment'])
						})

		print("Enjoy your CSV file located at {}!".format(
			os.path.abspath(filepath),
		))
