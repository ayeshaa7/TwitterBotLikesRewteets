# from twitter dev account, use access token, and twitter api
# make sure you have installed python3, pip and tweepy: pip3 install tweepy, from terminal

import tweepy
import time

auth = tweepy.OAuthHandler('', '')  # enter api key and api secret key here

# enter access token and access token secret key here
auth.set_access_token('', '')

# to avoid making too many requests so you don't be banned from twitter, use time.sleeep because when using twitter API, it sets activity limit for spam.
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_notify=True)
# the advantage is to use authentication from auth and use wait_on_rate_limit to pause when you take a pause for limit of likes or followers.
# wait_on_rate_notify gets you notifications on when you've reached the limit

user = api.me()  # to get myself

search = 'Javascript'
noOfTweets = 500

# for favorites
# it gets search term of javascript from tweets and items specify how many tweets we want to search
for tweet in tweepy.Cursor(api.search, search).items(noOfTweets):
    try:
        print('Tweet Favorited')
        tweet.favorite()
        # waits for 10 seconds before liking another tweet. you can like 1000 tweets per day
        time.sleep(10)
    except tweepy.TweepError as e:  # catches all the errors, renames as e.
        print(e.reason)
    except StopIteration:  # when it reaches completion, stop iteration so break
        break

# run python twitterbot.py and you'll see Tweet Liked, when the code has run

# for retweets
# it gets search term of javascript from tweets and items specify how many tweets we want to search
for tweet in tweepy.Cursor(api.search, search).items(noOfTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        # waits for 10 seconds before liking another tweet. you can like 1000 tweets per day
        time.sleep(10)
    except tweepy.TweepError as e:  # catches all the errors, renames as e.
        print(e.reason)
    except StopIteration:  # when it reaches completion, stop iteration so break
        break
