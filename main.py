import os
from os.path import join, dirname
from dotenv import load_dotenv # noqa
from pushover import init, Client # noqa
import feedparser
from time import time, sleep


# load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# start pushover
usertoken = os.getenv("USERTOKEN")
token = os.getenv("TOKEN")
init(token)

while True:
	sleep(10 - time() % 10)
	with open('rsslist.txt') as f:
		for line in f:
			d = feedparser.parse(line)
			feed = feedparser.parse(line, modified=d.modified)
			if feed.status == 304:
				print('Nothing new')
				break
			else:
				for key in feed["entries"]:
					title = key['title']
					url = key['links'][0]['href']
				print(title, url)
				Client(usertoken).send_message(url, title=title)
				print('Notification sent')
