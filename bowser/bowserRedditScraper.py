import time
from typing import Dict, List

import bowserUtils


def grab_subreddit(name):
	"""Get JSON of a given subreddit"""
	return bowserUtils.httpGET_json('https://www.reddit.com/r/' + name + '.json')


def grab_threadlist(SR: Dict) -> List:
	"""Get list of threads of given subreddit"""
	return [child['data']['permalink'] for child in SR['data']['children']]


def grab_messages(thread: str):
	"""Get messages from given thread"""
	json = bowserUtils.httpGET_json(str('https://reddit.com' + thread)[0:-1] + '.json')
	messages = []
	messages.append(json[0]['data']['children'][0]['data']['title'] +
					':' +
					json[0]['data']['children'][0]['data']['selftext'])

	[messages.append(comment['data']['body']) for comment in json[1]['data']['children']]

	return messages


if __name__ == '__main__':
	subreddit = grab_subreddit('Sino')
	threadList = grab_threadlist(subreddit)
	for i in range(0, len(threadList)):
		print('thread ' + str(i) + ': ')
		print(grab_messages(threadList[i]), '\n')
		time.sleep(0.1)  # Because of 429
