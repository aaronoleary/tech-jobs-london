import tweepy
from time import sleep
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,q='#jobsintech').items():

# Print out usernames of the last 10 people to use #ocean
    try:
        print('New Job from @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        sleep(90)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
