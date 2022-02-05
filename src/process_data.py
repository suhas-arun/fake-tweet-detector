# this is a test
#This is a 2nd test

L = 0.5

from benfordslaw import benfordslaw
import pandas as pd



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
    return results['P']


def calculateMagnitude(inputList):
    minVal = min(inputList)
    minOrder = len(str(minVal))-1
    maxVal = max(inputList)
    maxOrder = len(str(minVal))-1
    return (maxOrder - minOrder)
           

def calulateWeightings(l, magnitudeOrder):
    return (magnitudeOrder**l)/(6**l)


def testProcedure(importedData, method, l):
    # imported data will have three sets of data - likes, follows and tweets
    # the p values of each data set will be weighted averaged
    followers = importedData['followers']
    likes = importedData['likes']
    retweets = importedData['retweets']

    pFollowers = benfordsLawTest(followers, method=method)
    pLikes = benfordsLawTest(likes, method=method)
    pRetweets = benfordsLawTest(retweets, method=method)
    wFollowers = calulateWeightings(L, calculateMagnitude(followers))
    wLikes = calulateWeightings(L, calculateMagnitude(likes))
    wRetweets = calulateWeightings(L, calculateMagnitude(retweets))

    pAverage = ((pFollowers * wFollowers) + (pLikes * wLikes) + (pRetweets * wRetweets))/(wFollowers + wLikes + wRetweets)
    print("P Average:\t", pAverage)
    return pAverage

    

    


data = []
testProcedure(data, 'ks', L)


