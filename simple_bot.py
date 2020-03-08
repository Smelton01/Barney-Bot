import tweepy
import time
import pdb
from config import get_api
# NOTE: I put my keys in the keys.py to separate them
# from this main file.

def retrieve_saved_ids(file_name):
    try:
        f_read = open(file_name, "a+")
        cont = f_read.readlines()
    finally:
        f_read.close()
    return [line.strip("\n") for line in cont]

def retweet_fn(api, file_name):
    print('Searching for juicy tits.... I mean tweets!!!!', flush=True)

    results = api.search("#HIMYM", count=5)
    results_id = [result.id for result in results]
    saved = retrieve_saved_ids(file_name)

    for id in results_id:
        #pdb.set_trace()
        if id not in saved:
            print('New tweet found!!', flush=True)
            print('Retweeting...', flush=True)

            text = api.get_status(id).text
            #api.update_status(text)
            print(text)
            f_write = open(file_name, "a+")
            f_write.write("\n" + str(id))
            f_write.close()


def main():
    SAVED_ID = "saved.txt"
    api = get_api()
    while True:
        retweet_fn(api, SAVED_ID)
        #reply_to_tweets()
        time.sleep(30)

if __name__ == "__main__":
    main()