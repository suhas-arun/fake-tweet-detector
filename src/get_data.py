import tweepy
from config import bearer_token
from account_info import AccountInfo

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


def get_account_info(name):
    tweets = get_tweets(name, 10)
    num_followers = client.get_user(username=name, user_fields=["public_metrics"]).data.public_metrics['followers_count']
    likes = []
    retweets = []

    for tweet in tweets.data or []:
        metrics = tweet.public_metrics
        likes.append(metrics['like_count'])
        retweets.append(metrics['retweet_count'])

    return AccountInfo(name, num_followers, likes, retweets)

print(get_account_info("barackobama"))