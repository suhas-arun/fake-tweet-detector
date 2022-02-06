import json
import os
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

STEMMER = SnowballStemmer("english")
NON_ALPHABET = "[^A-Za-z]"


def process_tweet_files(path, data):
    print(f"Processing {path}")
    file_names = [dir for dir in next(os.walk(path))[1]]
    for i, tweet_path in enumerate(
        [os.path.join(path, file_name) for file_name in file_names]
    ):
        with open(
            os.path.join(tweet_path, "source-tweets", f"{file_names[i]}.json")
        ) as f:
            tweet_text = process_tweet_text(json.load(f)["text"])

        with open(os.path.join(tweet_path, "annotation.json")) as f:
            annotation = json.load(f)["is_rumour"]
            if annotation == "nonrumour":
                data[0].append(tweet_text)
                data[1].append(0)

            elif annotation == "rumour":
                data[0].append(tweet_text)
                data[1].append(1)

    return data


PATH = "data\\svm-data"


def process_tweet_text(text):
    text = re.sub(NON_ALPHABET, " ", text)
    words = [
        STEMMER.stem(word.lower()) for word in text.split() if word not in STOPWORDS
    ]
    return " ".join(words)


def create_df():
    data = [[], []]
    dirs = [os.path.join(PATH, dir) for dir in next(os.walk(PATH))[1]]

    for dir in dirs:
        data = process_tweet_files(os.path.join(dir, "non-rumours"), data)
        data = process_tweet_files(os.path.join(dir, "rumours"), data)

    return pd.DataFrame(list(zip(data[0], data[1])), columns=["tweet", "rumour"])


nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

df = create_df()
print(df)
