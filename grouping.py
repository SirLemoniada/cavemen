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

screen_names = ["KLM", "AirFrance", "British_Airways", "AmericanAir", "Lufthansa", "AirBerlin", "AirBerlin assist", 
"easyJet"," RyanAir","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]

for_plot = tweet.aggregate([
    #{ "$unwind": "$user.screen_name" },
   {"$match": {"entities.user_mentions.id":56377143}},
   {"$group" : {"_id":{"user":"$user.screen_name", 'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}, 'hour':{"$hour":"$created_at"}},"count": {"$sum":1}}},
   #{"$group" : {"_id":"$lang", "count": {"$sum":1}}},
   {"$sort": {"count": -1}},
   {"$limit":5}
])

list_cursor = list(for_plot)
df = DataFrame(list_cursor)
df2 = df.set_index("_id")
print(df2.head())

# for doc in for_plot: #iterating through commandcursor object
#     pprint.pprint(doc)