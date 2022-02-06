# this is a test
# This is a 2nd test

L = 0.5

from datetime import datetime, timezone
from turtle import position
from get_data import get_account_info, get_tweets
from tweet_sentiment import tweet_sentiment_bysent
from scipy import stats
import pandas as pd


numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

expected = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]


def frequencyCalc(dataSet):
    for val in dataSet:
        leadingDigit = int(str(val)[0])
        if leadingDigit != 0:
            numbers[leadingDigit] += 1

    # convert to percentage
    total = sum(numbers.values())
    print("Sum:", total)
    print(numbers)

    observedFrequencies = []
    for value in numbers.values():
        observedFrequencies.append((value / total) * 100)
    return observedFrequencies


def calculateMagnitude(inputList):
    minVal = min(inputList)
    minOrder = len(str(minVal)) - 1
    maxVal = max(inputList)
    maxOrder = len(str(maxVal)) - 1
    return maxOrder - minOrder


def calulateWeightings(l, magnitudeOrder):
    return (magnitudeOrder**l) / (6**l) + 0.1


def testProcedure(importedData, method, l):
    # imported data will have three sets of data - likes, follows and tweets
    # the p values of each data set will be weighted averaged
    likes = importedData["likes"]
    retweets = importedData["retweets"]

    # frequency analysis of leading digit data set
    observedRetweets = frequencyCalc(retweets)
    observedLikes = frequencyCalc(likes)

    # this returns 2 values, statistic and p value.
    # it is assumed that the the two distributions are identical (null hypothesis)
    # if stat is small or P  value is large, we accept the null hypothesis
    # if stat is large or p small, we reject the null hypothesis and say that they are different distribtuions
    # i.e. the data set does not follow benfords law.
    retweetStat, retweetP = stats.ks_2samp(observedRetweets, expected)
    likesStat, likesP = stats.ks_2samp(observedLikes, expected)

    # calculate weightings
    wLikes = calulateWeightings(l, calculateMagnitude(likes))
    wRetweets = calulateWeightings(l, calculateMagnitude(retweets))

    print(wLikes, wRetweets)

    pAverage = ((likesStat * wLikes) + (retweetStat * wRetweets)) / (wLikes + wRetweets)
    print("retweet stat: \t", retweetStat)
    print("like stat:\t", likesStat)
    print("P Average:\t", pAverage)

    print("Confidence:\t", (wLikes+wRetweets)/2)
    return pAverage, (wLikes+wRetweets)/2, observedLikes, observedRetweets
    




def test(accountName):
    data = {"likes": [], "retweets": []}

    global numbers
    numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    # get data
    returnedData = get_account_info(accountName, 1000)

    data["likes"] = returnedData.tweet_likes
    data["retweets"] = returnedData.tweet_retweets

    finalP, confidence, observedLikes, observedRetweets = testProcedure(data, "ks", L)
    if finalP > 0.35:
        return True, finalP, confidence, observedLikes, observedRetweets
    else:
        return False, finalP, confidence, observedLikes, observedRetweets


def timeDifferenceTest(timeDifferences):
    # takes a list of time differences in, calculates as a proportion of total tweets the number of tweets that happend
    # within 1 minute of each other (changeable)
    timeThreshold = 60
    shortTimes = 0
    for time in timeDifferences:
        if time < timeThreshold:
            shortTimes += 1
    return shortTimes / len(timeDifferences)


def timeDeltaAnalysis(tweets):
    dates = tweets["date"]

    # get time deltas between tweet times
    lastDate = dates[0]
    timeDifferences = []
    for i in range(1, dates.size):
        timeDeltaTotalSeconds = (lastDate - dates[i]).seconds + 86400 * (
            lastDate - dates[i]
        ).days
        timeDifferences.append(timeDeltaTotalSeconds)
        lastDate = dates[i]

    return timeDifferenceTest(timeDifferences)


def assortedTest(data):
    # function to apply several basic tests to assertain bot or not:
    #   - creation date? is the account very young (less thn 7, 14, 28 days etc.)
    #   - is there an account description?
    #   - proportion of numbers in the name - is it likely autogenerated?
    # test creation date
    userDetails = data["user"]

    created = userDetails[0]["created"]

    utc_dt = datetime.now(timezone.utc)
    age = (utc_dt - created).days
    if age < 7:
        ageW = 0.8
    elif age < 14:
        ageW = 0.4
    else:
        ageW = 0

    description = userDetails[0]["rawDescription"]
    if description == None:
        # no description
        descW = 0.9
    else:
        descW = 0.1

    ints = 0
    chars = 0
    for char in userDetails[0]["displayname"]:
        if char.isnumeric():
            ints += 1
        chars += 1

    intsW = ints / chars

    averageW = (ageW + descW + intsW) / 3

    return averageW


def weightTotal(benfordP, shortProp, assortedP):
    benfordWeight = 0.8
    timeWeight = 0.7
    assortedPW = 0.4
    averagedScore = (
        (benfordP * benfordWeight) + (timeWeight * shortProp) + (assortedPW * assortedP)
    ) / 3
    return averagedScore



def accountBotTest(account):
    if account == "ichack22":
        bot = True
    else:
        bot, p, confidence, observedLikes, observedRetweets = test(account)

    tweets = pd.DataFrame(get_tweets(account))
    shortProp = timeDeltaAnalysis(tweets)

    assortedP = assortedTest(tweets)

    botScore = weightTotal(p, shortProp, assortedP)

    print(account, ":", bot)
    print(account, ":", shortProp)
    print(account, ":", assortedP)
    print(account, ":", botScore)
    threshold = 0.11
    # times by 500 so anything above 55% is a bit
    botScore = botScore * 500

    # get sentiment
    positivity, negativity, neutrality = tweet_sentiment_bysent(tweets['content'])
    if neutrality >= 0.9:
        return 'Neutral'
    if position > negativity:
        # positive
        if (positivity - negativity) > 5:
            return 'Very Positive', botScore
        else:
            return 'Slightly Positive', botScore
    
    else:
        if (negativity - positivity) > 5:
            return 'Very Negative', botScore
        else:
            return 'Slightly Negative', botScore

# accounts = ["ICHackUK","FoxNews", "imperialcollege", "BBCNews", "A12_Info", "HEISEI_love_bot", "earthquakesSF"]
# accounts = ["elonmusk"] 

