from typing import NamedTuple


class AccountInfo(NamedTuple):
    account_id: int
    account_name: str
    num_followers: int
    tweet_likes: list[int]
    tweet_retweets: list[int]
