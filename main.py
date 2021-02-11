import os
from os.path import join, dirname
from dotenv import load_dotenv # noqa
from pushover import init, Client # noqa


# load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

usertoken = os.getenv("USERTOKEN")
token = os.getenv("TOKEN")
init(token)
Client(usertoken).send_message("Hello!", title="Hello")