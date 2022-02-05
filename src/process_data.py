# this is a test
#This is a 2nd test

L = 0.2

from cgi import test
from optparse import Values
from benfordslaw import benfordslaw
import pandas as pd
import json
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



def benfordsLawTest(data, method='ks'):
    # conducts benfords law test on 1D array of data supplied as data
    # mthod specifies benfords law method test
    # returns the p value of the test

    # Initialize
    bl = benfordslaw(alpha=0.05, method=method)
    # data expected as a 1D list of values
    X = pd.DataFrame({'values':data})
    testData = X['values']
    results = bl.fit(testData)
    bl.plot()
    return results['P']


def calculateMagnitude(inputList):
    minVal = min(inputList)
    minOrder = len(str(minVal))-1
    maxVal = max(inputList)
    maxOrder = len(str(maxVal))-1
    print("Mag:", maxOrder-minOrder)
    return (maxOrder - minOrder)
           

def calulateWeightings(l, magnitudeOrder):
    return (magnitudeOrder**l)/(6**l)


def testProcedure(importedData, method, l):
    # imported data will have three sets of data - likes, follows and tweets
    # the p values of each data set will be weighted averaged
    followers = importedData['followers']
    likes = importedData['likes']
    retweets = importedData['retweets']

    #pFollowers = benfordsLawTest(followers, method=method)
    pFollowers = 1
    pLikes = benfordsLawTest(likes, method=method)
    pRetweets = benfordsLawTest(retweets, method=method)
    
    wFollowers = calulateWeightings(l, calculateMagnitude(followers))
    wLikes = calulateWeightings(l, calculateMagnitude(likes))
    wRetweets = calulateWeightings(l, calculateMagnitude(retweets))

    print(wFollowers, wLikes, wRetweets)

    pAverage = ((pFollowers * wFollowers) + (pLikes * wLikes) + (pRetweets * wRetweets))/(wFollowers + wLikes + wRetweets)
    print("P Average:\t", pAverage)
    return pAverage, (wFollowers+wLikes+wRetweets)/3

    

    


data = {'followers' :[1929345],
        'likes' :[],
        'retweets': []}

 

# get data
returnedData = get_account_info("earthquakesSF", 1000)


data['likes'] = returnedData.tweet_likes
data['retweets'] = returnedData.tweet_retweets
print(data)
print(testProcedure(data, 'ks', L))

observed = frequencyCalc(data['retweets'])
# observed = [10.1, 17.6, 7.5, 16.7, 9.9, 1.7, 8.8, 10.1, 11.6]
expected = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
print(observed)

# this returns 2 values, statistic and p value.
# it is assumed that the the two distributions are identical (null hypothesis)
# if stat is small or P  value is large, we accept the null hypothesis
# if stat is large or p small, we reject the null hypothesis and say that they are different distribtuions
# i.e. the data set does not follow benfords law.
print(stats.ks_2samp(observed, expected))