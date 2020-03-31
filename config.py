#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy
from keys import *
import os

def get_api():
    auth = tweepy.OAuthHandler(os.getenv(API_key), os.getenv(API_secret))
    auth.set_access_token(os.getenv(token_key), os.getenv(token_secret))
    return tweepy.API(auth)