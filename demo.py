import tweepy
from textblob import TextBlob

consumer_key = zLdEvhBTae1U02Mp0EssLHvsX
consumer_secret = YvxzcsAgzF5msy3KXzPbQOBM0z5oeOzCNjQmlIVTAr7Q8qWvcZ

access_token = 888421116-LLJCwdqD8K9wRLXP2ZbMOmnk8LNPIGdvhRgAwEiH
access_token_secret = ShERBgRy3J1XZE8JVbV9cVELrHvNLneVzmp9t45jMmHAo

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Football')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)