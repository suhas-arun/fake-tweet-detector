import nltk

nltk.download(
    [
        "names",
        "stopwords",
        "state_union",
        "twitter_samples",
        "movie_reviews",
        "averaged_perceptron_tagger",
        "vader_lexicon",
        "punkt",
    ]
)
from get_data import get_tweets
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

sia = SentimentIntensityAnalyzer()
stopwords = nltk.corpus.stopwords.words("english")


# A list of strings will be taken as input, then an average of negativity and positivity will be returned.
def tweet_sentiment_bygen(strings_list):
    positive_sum = 0
    negative_sum = 0
    neutral_sum = 0
    for i in range(len(strings_list)):
        # print(strings_list[i])
        result = sia.polarity_scores(strings_list[i])
        positive_sum += result["pos"]
        negative_sum += result["neg"]
        neutral_sum += result["neu"]
    return (
        positive_sum / len(strings_list),
        negative_sum / len(strings_list),
        neutral_sum / len(strings_list),
    )


# Takes in long string (sentence or paragraph), then returns the final string without any meaningless punctuation/words.
def remove_stopwords(message):
    words = nltk.word_tokenize(message)
    # print(words)
    words = [w for w in words if w not in stopwords]
    # print(words)
    final_string = ""
    for i in range(len(words)):
        if words[i].isalpha() or (("." or "!" or "?") in words[i]):
            final_string += (words[i].lower()) + " "
    return final_string


# Takes in paragraph then splits into sentences, then uses nltk lib to test for positivity and negativity.
def tweet_sentiment_bysent(strings_list):
    positive_sum = 0
    negative_sum = 0
    neutral_sum = 0
    counter = 0
    for i in range(len(strings_list)):
        sentences = nltk.sent_tokenize(strings_list[i])
        for j in range(len(sentences)):
            # print(sentences[j])
            sentences[j] = remove_stopwords(sentences[j])
            # print(sentences[j])
            result = sia.polarity_scores(sentences[j].lower())
            positive_sum += result["pos"]
            negative_sum += result["neg"]
            neutral_sum += result["neu"]
            counter += 1
    return positive_sum / counter, negative_sum / counter, neutral_sum / counter


if __name__ == "__main__":
    data = pd.DataFrame(
        get_tweets("ICHackUK", max_tweets=1000)
    )  # Put person's twitter account here.

    tweets = data["content"]

    print(tweet_sentiment_bysent(tweets))
