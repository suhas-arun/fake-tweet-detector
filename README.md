# fake-tweet-detector

This is a program which performs several statistical and machine learning tests on any public twitter account, giving in result different values describing the twitter account: probability of account being a bot, probability of account spreading misinformation or "fake news", and an overall positivity/negativity rating based on the account's tweets.

There are several obvious applications to the real world, particularly in times where misinformation is prevalent, and harmful bots exist with the sole reason of spreading lies and negativity, things which can greatly affect the physical wellbeing of large numbers of people (as seen during the pandemic) but also general mental health.
    As a result, this tool can also be used on one's own account or the accounts you follow to analyse whether your social media atmosphere is more generally positive or negative. 

To use the program, simply run main.py, at which you will be given an opportunity to input a twitter account name (what's after the @), and the data analysis is completed in real time. Results may take up to a minute.
Keep in mind that the fewer number of tweets an account has, the less accurate the data, but similarly, an account with too frequent tweets would be recognised as a bot account.

# Bot Accounts
To find bot accounts, we used a Kolmogorov-Smirnov test in comparing the number of likes and retweets on the account's tweets to Benford's Law. This is in the idea that bots that are artificially created would follow each other, in an artificial way, such that they would not follow Benford's Law with precision.

# Fake news accounts
For this, we used a machine learning algorithm, trained with tweets from both misleading/misinformed tweets but also trustworthy tweets. We have also prioritised against having false positives, so that a tweet is more likely to be noticed as true than not.

# Positivity/negativity
We used a built-in ML algorithm from NLTK python library for analysing the type of words/phrases used, and therefore giving a result on the sentiment behind each tweet.