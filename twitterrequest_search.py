#!/usr/bin/env python

# REQUESTS TO PULL TWEETS FROM TWITTER FOR ANY USER, HASHTAG, OR KEYWORD
# Con: Returns only 100 tweets. Pro: Can search geolocation
# Modified original code from: http://stackoverflow.com/questions/33669199/how-to-read-twitter-json-file-and-save-it-as-a-csv-with-python

import tweepy
from working_files.app_keys import keys
from twitter import *
import json
from requests_oauthlib import OAuth1Session
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

twitter = OAuth1Session(CONSUMER_KEY,
                        CONSUMER_SECRET,
                        ACCESS_TOKEN,
                        ACCESS_TOKEN_SECRET)

# Use Twitter's documentation on the Search API to build out the search url: https://dev.twitter.com/rest/public/search                            
url = 'https://api.twitter.com/1.1/search/tweets.json?q=radiusnetworks&src=typd&count=100'

r = twitter.get(url)
r = r.json()  

# create a file to dump json data
with open('twitfile.json', 'w') as json_file:    
    data = json.dump(r, json_file)

#read json file
with open('twitfile.json') as afile:    
    a = json.loads(afile.read())

tweets = a['statuses']

ids = [tweet['id_str'] for tweet in tweets]
times = [tweet['created_at'] for tweet in tweets]
users = [tweet['user']['name'] for tweet in tweets]
texts = [tweet['text'] for tweet in tweets]
lats = [(T['geo']['coordinates'][0] if T['geo'] else None) for T in tweets]
lons = [(T['geo']['coordinates'][1] if T['geo'] else None) for T in tweets]
place_names = [(T['place']['full_name'] if T['place'] else None) for T in tweets]
place_types = [(T['place']['place_type'] if T['place'] else None) for T in tweets]

print texts