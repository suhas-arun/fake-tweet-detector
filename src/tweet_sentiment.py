import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
#result = sia.polarity_scores("Wow, NLTK is really powerful!")
#print(result['neg'], result['pos'])

positive_list = ['Wow, NLTK is powerful! I love using it. This is all great and positive stuff. I\'m so happy for this!']
negative_list = ['This is terribly disgusting', 'You\'re completely idiotic', 'I hope you die']

#A list of strings will be taken as input, then an average of negativity and positivity will be returned.
def tweet_sentiment(strings_list):
    positive_sum = 0
    negative_sum = 0
    neutral_sum = 0
    for i in range(len(strings_list)):
        result = sia.polarity_scores(strings_list[0])
        positive_sum += result['pos']
        negative_sum += result['neg']
        neutral_sum += result['neu']
    return positive_sum/len(strings_list), negative_sum/len(strings_list), neutral_sum/len(strings_list)

print(tweet_sentiment(positive_list))
print(tweet_sentiment(negative_list))

