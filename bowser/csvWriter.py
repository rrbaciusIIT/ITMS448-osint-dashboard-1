import csv
import os
from typing import List, TextIO

from bowserUtils import epoch_to_human_date, csv_safe_string, gen_post_api_url, gen_thread_api_url, gen_thread_url, \
	gen_post_url
from contentFlagger import ContentFlagger


class CSVPostWriter:

	@staticmethod
	def write_posts_to_stream(threads: List, stream: TextIO,
	                          content_flaggers: List[ContentFlagger] = None) -> None:
		"""
		:param threads: The list of FourPlebsAPI_Post objects to save.
		:param stream: A TextIO object.
		:param content_flaggers: Optional. The list of ContentFlagger objects that should flag posts.
			Use ALL_CONTENT_FLAGGERS to use all content flaggers that are defined by default.
		:return:
		"""

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

		writer = csv.DictWriter(stream, fieldnames=fieldnames)
		writer.writeheader()

		for thread in threads:

			row_reply = {
				'board': thread.board_code,
				'post_id': thread.post_id,
				'post_url': thread.gen_post_url(),
				'post_api_url': thread.gen_post_api_url(),
				'thread_id': thread.thread_num,
				'thread_url': thread.gen_thread_url(),
				'thread_api_url': thread.gen_thread_api_url(),
				'country_code': thread.poster_country,
				'full_comment': csv_safe_string(thread.comment),
				'op': True,
				'timestamp': epoch_to_human_date(thread.timestamp),
				'timestamp_epoch': thread.timestamp,
			}

			# for every flagger, apply its analysis to the post's comment
			for flagger in content_flaggers:
				row_reply.update(**{
					flagger.csv_description: flagger.flag_content_rapidminer_boolean(thread.comment)
				})

			writer.writerow(row_reply)

			for reply in thread.subposts:
				# TODO: Find a more elegant way to process these subposts! This is duplicated code!

				# print("Subpost:")
				# print(subpost)
				print('WOW WOW', reply)
				row_reply = {
					'board': reply['board']['shortname'],
					'post_id': reply['num'],
					'post_url': gen_post_url(reply['board']['shortname'], reply['thread_num'], reply['num']),
					'post_api_url': gen_post_api_url(reply['board']['shortname'], reply['num']),
					'thread_id': reply['thread_num'],
					'thread_url': gen_thread_url(reply['board']['shortname'], reply['thread_num']),
					'thread_api_url': gen_thread_api_url(reply['board']['shortname'], reply['thread_num']),
					'country_code': reply['poster_country'],
					'full_comment': csv_safe_string(reply['comment']),
					'op': False,
					'timestamp': epoch_to_human_date(reply['timestamp']),
					'timestamp_epoch': reply['timestamp'],
				}

				# for every flagger, apply its analysis to the subpost's comment
				for flagger in content_flaggers:
					row_reply.update(**{
						flagger.csv_description: flagger.flag_content_rapidminer_boolean(reply['comment'])
					})

				writer.writerow(row_reply)

	@staticmethod
	def write_posts_to_csv(posts: List, filepath: str,
	                       content_flaggers: List[ContentFlagger] = None):
		"""
		:param posts: The list of FourPlebsAPI_Post objects to save.
		:param stream: A TextIO object.
		:param content_flaggers: Optional. The list of ContentFlagger objects that should flag posts.
			Use ALL_CONTENT_FLAGGERS to use all content flaggers that are defined by default.
		:return:
		"""

		# Ensure that enclosing directory exists
		if not os.path.exists(os.path.dirname(filepath)):
			os.makedirs(os.path.dirname(filepath))

		if not filepath.split('.')[-1] == 'csv':
			raise Exception("File doesn't end in `csv`!")

		csvfile = open(filepath, 'w', newline='', encoding='utf-8')

		CSVPostWriter.write_posts_to_stream(threads=posts, content_flaggers=content_flaggers, stream=csvfile)

		csvfile.close()

		print("Enjoy your CSV file located at {}!".format(
			os.path.abspath(filepath),
		))
