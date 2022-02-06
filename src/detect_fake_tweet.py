from joblib import load
from svc.preprocess import process_tweet_text

MODEL_PATH = "models/svc.joblib"
VECT_PATH = "models/count_vect.joblib"

svc = load(MODEL_PATH)
count_vect = load(VECT_PATH)


def detect_fake_tweet(tweet_text):
    """Returns 1 if tweet is fake and 0 if it is real."""
    words = [process_tweet_text(tweet_text)]
    X = count_vect.transform(words).toarray()
    prediction = svc.predict(X)
    return prediction[0]
