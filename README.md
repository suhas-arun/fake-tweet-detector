# Fake Tweet Detector

Performs statistical and machine learning tests on any public Twitter account, giving the following results:

- Probability of the account being a bot
- Probability of account spreading misinformation/"fake news"
- Sentiment rating based on the account's tweets

# Usage

First install all dependencies:

    pip3 install -r requirements.txt

Then you will need to train the model using

    python3 src/svc/train.py

This will create two files: [models/svc.jolib](./models/svc.jolib) and [models/count_vect.jolib](./models/count_vect.jolib).

Then use

    python3 src/main.py

to run the program.

Enter a twitter account username and the data analysis is completed in real time.

N.B. The fewer number of tweets an account has, the less accurate the data, but similarly, an account with too frequent tweets may be recognised as a bot account.

# Methods

## Bot Accounts

To find bot accounts, we used a Kolmogorov-Smirnov test in comparing the number of likes and retweets on the account's tweets to Benford's Law. This is in the idea that bots that are artificially created would follow each other, in an artificial way, such that they would not follow Benford's Law with precision.

## Fake news accounts

For this, we used a machine learning algorithm ([State Vector Classification](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)), trained with the [PHEME dataset](https://doi.org/10.6084/m9.figshare.6392078.v1), which contains tweets from both misinformed and trustworthy sources. We were able to achieve an accuracy level of 85% on the test data.

## Sentiment Analysis

We used a built-in ML algorithm from NLTK python library for analysing the type of words/phrases used, and therefore giving a result on the sentiment behind each tweet.

# Applications

There are several obvious applications to the real world, particularly in times where misinformation is prevalent, and harmful bots exist with the sole reason of spreading lies and negativity, which can greatly affect the physical wellbeing of large numbers of people (as seen during the pandemic) but also general mental health.

As a result, this tool can also be used on the user's own account or the accounts they follow to analyse whether their social media atmosphere is more generally positive or negative.
