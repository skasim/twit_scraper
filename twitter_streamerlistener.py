#!/usr/bin/env python

# STREAMLISTENER TO SEARCH FOR CURRENT TWITTER ACTIVITY
# Use this code to find out what is going on right now for any hashtag, username, etc.
# Code taken from: http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

import tweepy
from tweepy import OAuthHandler
from working_files.app_keys import keys
from tweepy import Stream
from tweepy.streaming import StreamListener
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
# StreamListener to search for a keyword  
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('%s_tweets.json' % search_term, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
search_term = 'Obama'
twitter_stream.filter(track=[search_term])