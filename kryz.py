from unittest import result
import pymongo
from bson.regex import Regex
import pandas as pd
from dateutil.parser import parse
import datetime


import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt

def tweets_per_lang():

    lang_dict = {}   

    for language in tweet.distinct('lang'):
        language_count = tweet.count_documents({"lang" : language})
        if language_count > 50:
            lang_dict[language] = language_count

    sorted_lang_dict = dict(sorted(lang_dict.items(), key=lambda item: item[1],reverse=True))
    return sorted_lang_dict

#plt.bar(*zip(*sorted_lang_dict.items()))
#plt.show()
screen_names = ["KLM", "AirFrance", "British_Airways", "AmericanAir", "Lufthansa", "AirBerlin", "AirBerlin assist", 
"easyJet"," RyanAir","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]

def tweets_per_airline(tweet):

    airline_dict = {}   

    for airline in screen_names:
        airline_count = tweet.count_documents({'user.screen_name' : airline})
        airline_dict[airline] = airline_count



    #sorted_airline_dict = dict(sorted(lang_dict.items(), key=lambda item: item[1],reverse=True))
    return airline_dict
#print(tweets_per_airline(tweet))

def df_airlines(tweet):
    lst = []
    for airline in screen_names:
        for twt in tweet.find({'user.screen_name' : airline}):
            lst.append({'airline':twt['user']['screen_name'], 'time':twt['created_at']})
    return pd.DataFrame(lst)



dt = df_airlines(tweet).loc[1]['time']

date = datetime.datetime.strptime(dt, '%a %b %d %X %z %Y')
all_tweets = tweet.find({})
for twt in all_tweets:
    tweet.update_one({},{ "$set": { 'created_at': datetime.datetime.strptime(twt["created_at"], '%a %b %d %X %z %Y') } })
t = tweet.find_one({})
print(t['created_at'])
# tweet.aggregate([
#     {"$group" : {"_id"}}
# ])
for twt in tweet:
    tweet.update_one({"_id" : twt["_id"]}, {"$unset" : {"retweeted_status.user.id_str" : ""}})
