import tweepy
import json
import os


def getTweets(query="belieber", lang="en", count="100", result_type="recent", filename="tweets.txt", geocode="53.721247,3.904416,300mi"):
    auth = tweepy.OAuthHandler(os.environ['ckey'], os.environ['csecret'])
    auth.set_access_token(os.environ['atoken'], os.environ['asecret'])

    api = tweepy.API(auth)

    # Specify your search parameters here
    results = api.search(q=query, lang=lang, count=count, result_type=result_type, geocode=geocode)

    tweets = []

    for result in results:
        tweets.append(result.text)

    return tweets
