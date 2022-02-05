import snscrape.modules.twitter as sntwitter
from itertools import islice
from account_info import AccountInfo
from time import time


def get_user_id(username):
    try:
        return sntwitter.TwitterUserScraper(username)._get_entity().id
    except (AttributeError, ValueError):
        return -1


def get_tweets(username, max_tweets=100):
    return islice(
        sntwitter.TwitterSearchScraper(f"from:{username}").get_items(), max_tweets
    )


def get_account_info(username, max_tweets=100):
    tweets = get_tweets(username, max_tweets)
    account_id = get_user_id(username)
    if id == -1:
        return None

    likes = []
    retweets = []

    start = time()
    likes, retweets = get_likes_retweets(tweets)
    t = time() - start

    num_followers = sntwitter.TwitterUserScraper(username)._get_entity().followersCount

    return AccountInfo(account_id, username, num_followers, likes, retweets)


def get_likes_retweets(tweets, likes=[], retweets=[]):
    for tweet in tweets:
        likes.append(tweet.likeCount)
        retweets.append(tweet.retweetCount)

    return likes, retweets


print(get_account_info("barackobama", 10))
