import tweepy
import time
from config import get_api
from rnn_bot import pred
import random

# NOTE: I put my keys in the keys.py to separate them
# from this main file.

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.num = 1

    def on_status(self, tweet):
        try:
            #print(f"{tweet.user.name}:{tweet.text}")
            print("Found some juicy tits... I mean tweets!!!")
            starts = [["You", "know", "what"], ["I","mean"], ["Let", "me", "tell"], ["Bro"],["Some", "day"], ["If", "you", "ask", "me"]] 
            #if not tweet.retweet:
            print("Retweeting!!!")
            tweet.retweet()
            status = pred(random.choice(starts))
            self.api.update_status(status[:270]+" #HIMYM"+"...")
            print("Done!!")
        except Exception as e:
            print("Failed to predict!! ", e)
            pass
        time.sleep(60*60)

    def on_error(self, status):
        print(status)
        print("Error detected")
        time.sleep(15 * 60)

def main():
    #SAVED_ID = "saved.txt"
    api = get_api()
    listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, listener)
    print("Connected... starting stream.")
    stream.filter(track=["HIMYM"], languages=["en"])
   
main()
