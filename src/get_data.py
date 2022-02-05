import snscrape.modules.twitter as sntwitter


def get_user_id(username):
    try:
        return sntwitter.TwitterUserScraper(username)._get_entity().id
    except (AttributeError, ValueError):
        return -1


print(get_user_id("barackobama"))
