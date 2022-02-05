import tweepy
from config import *

client = tweepy.Client(bearer_token)


def get_user_id(username):
    """Gets user id for a given username. Returns -1 if user not found"""
    try:
        return client.get_user(username=username).data.id
    except tweepy.HTTPException:
        return -1


def get_tweets(username, max_results):
    """Gets the max_results most recent tweets from a given user"""
    return client.search_recent_tweets(
        query=f"from:{get_user_id(username)}",
        tweet_fields=["public_metrics"],
        max_results=max_results,
    )


tweets = get_tweets("barackobama", 10)

for tweet in tweets.data or []:
    print(f"{tweet.public_metrics}\n")
