from ctypes import create_unicode_buffer
from unittest import result
import pymongo
from bson.regex import Regex
import pandas as pd
from dateutil.parser import parse
import datetime
import pprint
from collections import OrderedDict
from pandas import DataFrame



import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt

screen_names = ["KLM", "AirFrance", "British_Airways", "AmericanAir", "Lufthansa", "AirBerlin", "AirBerlin assist", 
"easyJet"," RyanAir","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]

#1 removing empty time strings
#2 changing time to timestamp
#3 creating aggregation - groupby time, airline, and count()
#4 plotting

#for twt in tweet.find({}):
#    tweet.delete_one({"created_at": {"$exists": False}})


#print(tweet.count_documents({"created_at": {"$exists": False}}))
def remove_wrong_time():
    for twt in tweet.find({}):
        tweet.delete_one({"created_at": {"$exists": False} })
    return

    #     outliers = tweet.find({"id": {"$exists" : False}}) # Find all values that do not have an id
    # for error_tweets in outliers: # Iterates through outliers and deletes them
    #     tweet.delete_one({"_id" : error_tweets["_id"]})


#date = datetime.datetime.strptime("30 Nov 00", '%a %b %d %X %z %Y')


def time_to_timestamp():
    all_tweets = tweet.find({})
    
    for twt in all_tweets:
        try:
            tweet.update_one({"_id" : twt["_id"]},{ "$set": { 'created_at': datetime.datetime.strptime(str(twt["created_at"]), '%a %b %d %X %z %Y') } })
        except:
            pass
    return


# t = tweet.find_one({})
# k = t['created_at'].year
# print(k)

# def most_tweets():
#     new_json = tweet.aggregate([
#     {"$group" : {"_id":{"$user.screen_name"}, "count": {"$sum":1}}}
#     ])
# if __name__ == '__main__':
#     new_json = most_tweets()
#     pprint.pprint(new_json)
# {"screen_name":"$screen_name", "created_at":"$created_at"}
for_plot = tweet.aggregate([
    #{ "$unwind": "$user.screen_name" },
   {"$match": {"user.screen_name":{"$in":screen_names}}},
   #{"$group" : {"_id":{"user":"$user.screen_name", 'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}, 'hour':{"$hour":"$created_at"}},"count": {"$sum":1}}},
   {"$group" : {"_id":"$user.screen_name", "count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   #{"$project": {"lang":1, "_id":1, "created_at":1, "user.screen_name":1}},
   {"$limit":5}
])
list_cursor = list(for_plot)
df = DataFrame(list_cursor)
df2 = df.set_index("_id")
print(df2.head())
# for doc in for_plot:
#     pprint.pprint(doc)
plt.bar(*zip(*df2.items()))
plt.show()


# cursor = tweet.aggregate([
#    {"$match": {"user.screen_name":{"$in":["KLM", "British_Airways"]}}},
#    {"$sort": OrderedDict([("user.screen_name", -1)])},
#    {"$project": {"lang":1, "_id":0, "created_at":1, "user.screen_name":1}},
#     {"$limit":3}
# ])
# for doc in cursor:
#     pprint.pprint(doc)
#print(tweet.count_documents({"created_at":{"$exists":True}}))







