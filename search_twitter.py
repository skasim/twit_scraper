#!/usr/bin/env python

# USE TWITTERSEARCH TO SEARCH FOR KEYWORDS
# For more information, visit: https://pypi.python.org/pypi/TwitterSearch/ or https://github.com/ckoepp/TwitterSearch

import tweepy
from tweepy import OAuthHandler
from working_files.app_keys import keys
from TwitterSearch import *

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Obama', 'Clinton'])
    #tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = keys['consumer_key'],
        consumer_secret = keys['consumer_secret'],
        access_token = keys['access_token'],
        access_token_secret = keys['access_token_secret']
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)