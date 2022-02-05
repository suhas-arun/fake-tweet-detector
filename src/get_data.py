import tweepy
from config import *

client = tweepy.Client(bearer_token)

tweets = client.search_recent_tweets(
    query="covid", tweet_fields=["context_annotations", "created_at"], max_results=10
)

for tweet in tweets.data:
    print("\n\n")
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
