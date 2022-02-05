# this is a test
#This is a 2nd test

L = 0.2

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

    pFollowers = benfordsLawTest(followers, method=method)
    pLikes = benfordsLawTest(likes, method=method)
    pRetweets = benfordsLawTest(retweets, method=method)
    
    wFollowers = calulateWeightings(l, calculateMagnitude(followers))
    wLikes = calulateWeightings(l, calculateMagnitude(likes))
    wRetweets = calulateWeightings(l, calculateMagnitude(retweets))

    print(wFollowers, wLikes, wRetweets)

    pAverage = ((pFollowers * wFollowers) + (pLikes * wLikes) + (pRetweets * wRetweets))/(wFollowers + wLikes + wRetweets)
    print("P Average:\t", pAverage)
    return pAverage, (wFollowers+wLikes+wRetweets)/3

    

    


data = {'followers' :[12,14,18,3,2,54,85,97656,7,847,4542,465],
        'likes' :[1,1,14,5,2,67,1,234,6,23,56,7,8,2,0,0,1],
        'retweets': [1,2,2,1,1,1,1,5,3,6,8,5,0,4,9]}

res = {}
for i in range(1, 9, 1):
    j = i/10
    res[j] = list(testProcedure(data, 'ks', j))

print(res)


