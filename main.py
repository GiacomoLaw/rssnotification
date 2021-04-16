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
		line = f.readline()
	f.close()

while True:
	fileread()
