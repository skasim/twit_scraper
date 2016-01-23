#!/usr/bin/env python

# TWITTER API SEARCH FOR DESIRED NUMBER OF TWEETS
# Twitter API only allows you to scrape 100 tweets at a time
# This code scrapes desired number of tweets for a keyword, username, or hashtag using a while loop
# Due to twitter limitations, only pulls from tweets from the past 7 days
# Modified code from: https://gist.github.com/yanofsky/5436496

import tweepy
from tweepy import OAuthHandler
from working_files.app_keys import keys
from twitter import *
import json
import csv
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def get_all_tweets(query, total_tweets):
    #initialize a list to hold all the tweepy Tweets  
    alltweets = []

    #make initial request for most recent tweets (100 is the maximum allowed count)
    new_tweets = api.search(q=query, count=100)
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one    
    oldest = alltweets[-1].id - 1

    #print "this is the oldest tweet: {0}".format(oldest)

    #loop until desired number of tweets is grabbed
    while len(alltweets) < total_tweets:
        print "getting tweets before %s" % (oldest)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.search(q=query, count=100, max_id=oldest)
    
        #save most recent tweets
        alltweets.extend(new_tweets)
    
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
    
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    
    #write the csv	
    with open('%s_tweets.csv' % query, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
        print "csv file created"
    
    pass
    
if __name__ == '__main__':
	#pass in the keyword, username, hashtag, etc. you want to search
	get_all_tweets("Hillary Clinton", 1200)  

