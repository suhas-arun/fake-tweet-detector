from typing import NamedTuple

class AccountInfo(NamedTuple):
    account_name: str
    num_followers: int
    tweet_likes: list[int]

# will this merge?
