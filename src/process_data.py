# this is a test
#This is a 2nd test

L = 0.2

from get_data import get_account_info
from scipy import stats


numbers = {1: 0,
           2: 0,
           3: 0,
           4: 0,
           5: 0,
           6: 0,
           7: 0,
           8: 0,
           9: 0}

expected = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

def frequencyCalc(dataSet):
    for val in dataSet:
        leadingDigit = int(str(val)[0])
        if (leadingDigit != 0):
            numbers[leadingDigit] += 1

    # convert to percentage
    total = sum(numbers.values())
    print("Sum:", total)
    print(numbers)

    observedFrequencies = []
    for value in numbers.values():
        observedFrequencies.append((value/total)*100)
    return observedFrequencies


def calculateMagnitude(inputList):
    minVal = min(inputList)
    minOrder = len(str(minVal))-1
    maxVal = max(inputList)
    maxOrder = len(str(maxVal))-1
    print("Mag:", maxOrder-minOrder)
    return (maxOrder - minOrder)
           

def calulateWeightings(l, magnitudeOrder):
    return ((magnitudeOrder**l)/(6**l)+0.1)


def testProcedure(importedData, method, l):
    # imported data will have three sets of data - likes, follows and tweets
    # the p values of each data set will be weighted averaged
    likes = importedData['likes']
    retweets = importedData['retweets']

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

    pAverage = ((likesStat * wLikes) + (retweetStat * wRetweets))/(wLikes + wRetweets)
    print("P Average:\t", pAverage)
    return pAverage, (wLikes+wRetweets)/2
    



def test(accountName):
    data = {'likes' :[],
        'retweets': []}

    global numbers
    numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0,6: 0, 7: 0, 8: 0, 9: 0}

    # get data
    returnedData = get_account_info(accountName, 1000)

    data['likes'] = returnedData.tweet_likes
    data['retweets'] = returnedData.tweet_retweets
    print(data)
    finalP, confidence = testProcedure(data, 'ks', L)
    if finalP > 0.35:
        return True, finalP, confidence
    else:
        return False, finalP, confidence


accounts = ["imperialCollege", "BBC", "A12_Info", "HEISEI_love_bot", "earthquakesSF"]
for account in accounts:
    bot, p, confidence = test(account)
    print(account, ":", bot)
