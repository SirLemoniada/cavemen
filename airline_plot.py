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

for_plot = tweet.aggregate([
    {"$match": {"user.screen_name":"KLM"}},
   {"$group" : {"_id":{'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}},"count": {"$sum":1}}},
   #{"$group" : {"_id":"$lang", "count": {"$sum":1}}},
   #{ "$push": { "created_at": <value1>, ... } }
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 1, "count":1}}
])
#"user":"$user.screen_name"
#'hour':{"$hour":"$created_at"}
list_cursor = list(for_plot)
df = DataFrame(list_cursor)
df2 = df.set_index("_id")
print(df2.head())
df2['count'].plot()
# df.plot(kind='bar', x='_id', y='count')
plt.show()







