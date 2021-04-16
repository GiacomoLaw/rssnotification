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

# count lines in file
count = 0
for line in open('rsslist.txt'): count += 1

def fileread():
	f = open('rsslist.txt')
	line = f.readline()
	while line:
		stripped_line = line.strip('\n')
		print(stripped_line)
		d = feedparser.parse(stripped_line)
		try:
			feed = feedparser.parse(stripped_line, modified=d.modified)
		except AttributeError:
			feed = feedparser.parse(stripped_line, etag=d.etag)
		if feed.status == 304:
			print('Nothing new')
		else:
			for key in feed["entries"]:
				title = key['title']
				url = key['links'][0]['href']
			print(title, url)
			Client(usertoken).send_message(url, title=title)
			print('Notification sent')
		line = f.readline()
	f.close()

while True:
	fileread()
