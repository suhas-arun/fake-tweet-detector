import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
stopwords = nltk.corpus.stopwords.words("english")
#result = sia.polarity_scores("Wow, NLTK is really powerful!")
#print(result['neg'], result['pos'])

positive_list_1 = ['Wow, NLTK is powerful!', 'I love using it.', 'This is all great and positive stuff.', 'I\'m so happy for this!']
positive_list = ['Wow, NLTK is powerful! I love using it. This is all great and positive stuff. I\'m so happy for this!']
negative_list = ['This is terribly disgusting', 'You\'re completely idiotic', 'I hope you die']

#A list of strings will be taken as input, then an average of negativity and positivity will be returned.
def tweet_sentiment_bygen(strings_list):
    positive_sum = 0
    negative_sum = 0
    neutral_sum = 0
    for i in range(len(strings_list)):
        #print(strings_list[i])
        result = sia.polarity_scores(strings_list[i])
        positive_sum += result['pos']
        negative_sum += result['neg']
        neutral_sum += result['neu']
    return positive_sum/len(strings_list), negative_sum/len(strings_list), neutral_sum/len(strings_list)

#Takes in paragraph then splits into sentences.
def tweet_sentiment_bysent(strings_list):
    positive_sum = 0
    negative_sum = 0
    neutral_sum = 0
    counter = 0
    for i in range(len(strings_list)):
        sentences = nltk.sent_tokenize(strings_list[i])
        for j in range(len(sentences)):
            print(sentences[j])
            result = sia.polarity_scores(sentences[j])
            positive_sum += result['pos']
            negative_sum += result['neg']
            neutral_sum += result['neu']
            counter += 1
    return positive_sum/counter, negative_sum/counter, neutral_sum/counter

print(tweet_sentiment_bygen(positive_list_1))
print(tweet_sentiment_bysent(positive_list))