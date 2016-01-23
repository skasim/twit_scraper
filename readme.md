## TWITTER SCRAPERS

I wanted to scrape Twitter for a project and I realized that there isn't one centralized place with scrapers built for various purposes. So I put together this repo to centralize scrapers for folks who don't want to learn the Twitter API and just need tweets for analysis.

Below is the list of scrapers. Most of the code is taken from other people's code and some of it has been modified by me. In each of the files, I have listed where I grabbed the original code from.

* *twitter_streamlistener.py*: Uses StreamListener to scrape for tweets in the moment
* *twitterapi_search.py*: Uses Twitter API to scrape for as many tweets as you want
* *twitterrequest_search.py*: Uses Request to scrape tweets
* *search_twitter,py*: Uses TwitterSearch to scrape tweets
* *scrape_username*: Scrapes all the tweets for a username