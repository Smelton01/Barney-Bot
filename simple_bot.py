import tweepy
import time
from config import get_api
from rnn_bot import pred

# NOTE: I put my keys in the keys.py to separate them
# from this main file.

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        try:
            print(f"{tweet.user.name}:{tweet.text}")
            pred(tweet.text.split()[1])
        except:
            print("Error word not in vocab!!")
            pass
        if not tweet.retweet: #self.me.screen_name in tweet.text:
            print('Found some juicy tits.... I mean tweets!!!!', flush=True)
            time.sleep(3*60)
            tweet.retweet()
            #self.api.update_status(tweet.text, " ...Copied")
            #retweet_fn(tweet)
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print(status)
        print("Error detected")
        time.sleep(15 * 60)

def main():
    #SAVED_ID = "saved.txt"
    api = get_api()
    listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, listener)
    stream.filter(track=["HIMYM"], languages=["en"])
    
    #while True:
     #   retweet_fn(api, SAVED_ID)
        #reply_to_tweets()
      #  time.sleep(30)

#if __name__ == "__main__":
#    main()