#Importing modules
from textblob import TextBlob as tb #NLP module
import tweepy #Twitter API
import numpy as np #for some calculation. You may want to use your favorite module for this, such as statistics

#You need to configure an app in Twitter Apps. After that, create four variables that will store your consumer key and secret, and your tokens
consumer_key = 'IuhoiuhiouahsdiouahoIDUHsdALKSDNnoiqwn'
consumer_secret = 'PAOISDUPOWNQOPJNpijndasdaklsdHIASDPIQOWUN'

access_token = 'as7d6a4sd3a654sd6A84SD9A84S6D94A6SD4ASD'
access_token_secret = 'QWEQWE1QW3E21AS0D98S7987J746TYK74YUI'

#Authentication process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Calling the API
api = tweepy.API(auth)

#Let's search for some tweets. You can you any English word
public_tweets = api.search('Trump')

#I will use this variable later for some computation
analysis = None 

#Loop for which will print every tweet and its sentiment polarity
tweets = []
for tweet in public_tweets:
    print(tweet.text)
    analysis = tb(tweet.text)
    polarity = analysis.sentiment.polarity
    tweets.append(polarity)
    print(polarity)

#After that, let's check the average of all tweets polarity
print('SENTIMENT AVERAGE: ' + str(np.mean(tweets)))
