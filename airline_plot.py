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
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 0, "count":1}}
])
for_plot2 = tweet.aggregate([
    {"$match": {"user.screen_name":"AmericanAir"}},
   {"$group" : {"_id":{'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}},"count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 0, "count":1}}
])
for_plot3 = tweet.aggregate([
    {"$match": {"user.screen_name":"British_Airways"}},
   {"$group" : {"_id":{'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}},"count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 0, "count":1}}
])
for_plot4 = tweet.aggregate([
    {"$match": {"user.screen_name":"SingaporeAir"}},
   {"$group" : {"_id":{'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}},"count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 0, "count":1}}
])
index = pd.date_range(start='1/10/2018', end='1/11/2018')

list_cursor = list(for_plot)
df = DataFrame(list_cursor)

list_cursor2 = list(for_plot2)
df2 = DataFrame(list_cursor2)

list_cursor3 = list(for_plot3)
df3 = DataFrame(list_cursor3)

list_cursor4 = list(for_plot4)
df4 = DataFrame(list_cursor4)

#"user":"$user.screen_name"
#'hour':{"$hour":"$created_at"}

df.set_index(index, inplace=True)
df2.set_index(index, inplace=True)
df3.set_index(index, inplace=True)
df4.set_index(index, inplace=True)

fig, ax_combo = plt.subplots(figsize=[10,8])
df["count"].plot(x=index, ax=ax_combo)
df2["count"].plot(x=index,ax=ax_combo)
df3["count"].plot(x=index,ax=ax_combo)
df4["count"].plot(x=index,ax=ax_combo)

plt.legend(["KLM","Amercian_Air","British_Airways","SingaporeAir"])
plt.title("Tweeting over time")
plt.ylabel("Number of tweets per day")
plt.show()
# print(df2)
plt.savefig("airline_plot")







