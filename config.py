#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy
from keys import *

def get_api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    return tweepy.API(auth)