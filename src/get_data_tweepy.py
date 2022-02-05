# # TODO: Sort out private accounts

# import tweepy
# from config import bearer_token
# from account_info import AccountInfo

# client = tweepy.Client(bearer_token)


# def get_user_id(username):
#     """Gets user id for a given username. Returns -1 if user not found"""
#     try:
#         return client.get_user(username=username).data.id
#     except tweepy.HTTPException:
#         return -1


# def get_tweets(username, max_results=100):
#     """Gets the max_results most recent tweets from a given user"""
#     return client.search_recent_tweets(
#         query=f"from:{get_user_id(username)}",
#         tweet_fields=["public_metrics"],
#         max_results=max_results,
#     )


# def get_account_info(name, max_tweets=100):
#     tweets = get_tweets(name, max_tweets)
#     account_id = get_user_id(name)
#     if account_id == -1:
#         return None
#     num_followers = client.get_user(
#         username=name, user_fields=["public_metrics"]
#     ).data.public_metrics["followers_count"]
#     likes, retweets = get_likes_retweets(tweets)

#     while len(likes) < 1000 or len(retweets) < 1000:
#         for follower in get_followers(account_id).data:
#             get_likes_retweets(
#                 get_tweets(follower.data.get("username")), likes, retweets
#             )
#             # print(follower)
#             # print(len(likes), len(retweets))

#     return AccountInfo(get_user_id(name), name, num_followers, likes, retweets)


# def get_likes_retweets(tweets, likes=[], retweets=[]):
#     for tweet in tweets.data or []:
#         metrics = tweet.public_metrics
#         likes.append(metrics["like_count"])
#         retweets.append(metrics["retweet_count"])

#     return (likes, retweets)


# def get_followers(account_id):
#     return client.get_users_followers(account_id)


# print(get_account_info("imperialcollege", 10))
