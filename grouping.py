from ctypes import create_unicode_buffer
from unittest import result
import pymongo
from bson.regex import Regex
import pandas as pd
import datetime
import pprint
from pandas import DataFrame

import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt
from random import sample


screen_names = ["KLM", "AirFrance", "British_Airways", "AmericanAir", "Lufthansa", "AirBerlin", "AirBerlin assist", 
"easyJet"," RyanAir","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]

for_plot = tweet.aggregate([
    #{ "$unwind": "$user.screen_name" },
    {"$match": {"user.screen_name":{"$in":screen_names}}},
   {"$group" : {"_id":{"user":"$user.screen_name", 'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}, 'hour':{"$hour":"$created_at"}},"count": {"$sum":1}}},
   #{"$group" : {"_id":"$lang", "count": {"$sum":1}}},
   #{ "$push": { "created_at": <value1>, ... } }
   {"$sort": {"count": -1}},
   {"$project": {"_id": 1, "count":1}},
   {"$limit":5}
])
#"user":"$user.screen_name"
list_cursor = list(for_plot)
df = DataFrame(list_cursor)
#df2 = df.set_index("_id")
print(df.head())
# df.plot(kind='bar', x='_id', y='count')
# plt.show()

# for doc in for_plot: #iterating through commandcursor object
#     pprint.pprint(doc)



# init_users_to_KLM = tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143})
# reply_to_KLM = tweet.find({"in_reply_to_user_id":56377143})
# tweets_by_KLM = tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}})

# KLM_conversation_start_with_others = {}

# def KLM_conversation_start_with_others_function():
#     for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
#         for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}): 
#             if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
#                 for reply_to_KLM in tweet.find({"in_reply_to_user_id":56377143}):
#                     if (reply_to_KLM["in_reply_to_status_id"] == reply_by_KLM['id']) & (reply_to_KLM['user']['id'] == init_tweet['user']['id']):
#                         KLM_conversation_start_with_others[init_tweet['id']] = {reply_by_KLM['id']:[reply_to_KLM['id'],[sample({"pos", "neg","neu"},1),"pos",sample({"pos", "neg","neu"},1)] ]}
#                 #if init_tweet['id'] not in KLM_conversation_start_with_others:
#                     #KLM_conversation_start_with_others[init_tweet['id']] = reply_by_KLM['id']
#     return(KLM_conversation_start_with_others)

# d = KLM_conversation_start_with_others_function()
# print(d)