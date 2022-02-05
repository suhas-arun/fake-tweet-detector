# this is a test
#This is a 2nd test

L = 0.2

from benfordslaw import benfordslaw
import pandas as pd
import json
from get_data import get_account_info


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


""" with open('src/user-tweets-single.json') as raw:
    res = json.load(raw)
print(type(res))
for key in res:
    print(key)

print(res['retweetCount'])

with open('src/user-tweets.json') as raw:
    dat = raw.readlines()

res = {}

tweet = 0
for line in dat:
    res |= {tweet: json.loads(line)}
    tweet += 1

for i in range(0,99):
    data['likes'].append(res[i]['likeCount'])
    data['retweets'].append(res[i]['retweetCount'])

print(data)

print(testProcedure(data, 'ks', L)) """

# get data
returnedData = get_account_info("BBC", 1000)


data['likes'] = returnedData.tweet_likes
data['retweets'] = returnedData.tweet_retweets

print(data)