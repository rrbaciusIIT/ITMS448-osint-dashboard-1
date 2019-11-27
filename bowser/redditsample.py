import requests
import bowserScraper
import time

# Get JSON of a given subreddit
def grab_subreddit(name):
    return bowserScraper.httpGET_json('https://www.reddit.com/r/' + name + '.json')

# Get list of threads of given subreddit
def grab_threadlist(SR):
    return [child['data']['permalink'] for child in SR['data']['children']]

# Get messages from given thread
def grab_messages(thread):
    json = bowserScraper.httpGET_json(str('https://reddit.com' + thread)[0:-1] + '.json')
    messages = []
    messages.append(json[0]['data']['children'][0]['data']['title'] + ':' + json[0]['data']['children'][0]['data']['selftext'])
    [messages.append(comment['data']['body']) for comment in json[1]['data']['children']]
    return messages

if __name__ == '__main__':
    subreddit = grab_subreddit('Sino')
    threadList = grab_threadlist(subreddit)
    for i in range(0, len(threadList)):
        print('thread ' + str(i) + ': ')
        print(grab_messages(threadList[i]), '\n')
        time.sleep(0.1) # Because of 429

