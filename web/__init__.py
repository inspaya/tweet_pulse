from os import environ
from unicodedata import normalize
from tweepy import API, Cursor, OAuthHandler


def twitter_auth():
    auth = OAuthHandler(environ["TWITTER_CONSUMER_KEY"], environ["TWITTER_CONSUMER_SECRET"])
    api = API(auth)
    return api


def clean_tweets(user_tweets):
    """
    Remove re-tweets, special unicode xters and URLs
    :return:
    """
    cleaned_tweets = []
    for tweet in user_tweets:
        if not tweet.full_text.startswith("RT @"):
            clean_tweet = normalize('NFKD', tweet.full_text).encode('ascii', 'ignore')
            cleaned_tweets.append(clean_tweet)
    print(cleaned_tweets)
    return cleaned_tweets


def get_user_tweets_from_timeline(twitter_username, item_count=20):
    twitter = twitter_auth()
    user = twitter.get_user(twitter_username)
    user_tweet_cursor = Cursor(twitter.user_timeline, id=user.id, tweet_mode='extended').items(item_count)
    return clean_tweets(user_tweet_cursor)
