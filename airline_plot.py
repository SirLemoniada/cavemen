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
#, 'dayofmon':{"$dayOfMonth":"$created_at"}}
for_plot = tweet.aggregate([
    {"$match": {"user.screen_name":"KLM"}},
   {"$group" : {"_id":{"year":{"$year":"$created_at"},'month':{"$month":"$created_at"}, 'dayofmon':{"$week":"$created_at"}},"count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 1, "count":1}}
])
for_plot2 = tweet.aggregate([
    {"$match": {"user.screen_name":"AmericanAir"}},
   {"$group" : {"_id":{"year":{"$year":"$created_at"},'month':{"$month":"$created_at"}, 'dayofmon':{"$week":"$created_at"}},"count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 0, "count":1}}
])
for_plot3 = tweet.aggregate([
    {"$match": {"user.screen_name":"British_Airways"}},
   {"$group" : {"_id":{"year":{"$year":"$created_at"},'month':{"$month":"$created_at"}, 'dayofmon':{"$week":"$created_at"}},"count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 0, "count":1}}
])
for_plot4 = tweet.aggregate([
    {"$match": {"user.screen_name":"SingaporeAir"}},
   {"$group" : {"_id":{"year":{"$year":"$created_at"},'month':{"$month":"$created_at"}, 'dayofmon':{"$week":"$created_at"}},"count": {"$sum":1}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 0, "count":1}}
])
for_plot5 = tweet.aggregate([
    {"$match": {'is_a_reply':False, 'entities.user_mentions.id':22536055}},
   {"$group" : {"_id":{"year":{"$year":"$created_at"},'month':{"$month":"$created_at"}, "week": {"$week":"$created_at"}},"avg": {"$avg":"$sentiment"}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 1, "avg":1}}
])

# index1 = pd.date_range(start='5/22/2019', end='3/30/2020')
# print(index1)

list_cursor = list(for_plot)
df = DataFrame(list_cursor)
print(len(df))
# Expected 287 rows, received array of length 314
list_cursor2 = list(for_plot2)
df2 = DataFrame(list_cursor2)

list_cursor3 = list(for_plot3)
df3 = DataFrame(list_cursor3)

list_cursor4 = list(for_plot4)
df4 = DataFrame(list_cursor4)

list_cursor5 = list(for_plot5)
df5 = DataFrame(list_cursor5)


# # "user":"$user.screen_name"
# # 'hour':{"$hour":"$created_at"}

# # df.set_index(index, inplace=True)
# # # df2.set_index(index, inplace=True)
# # # df3.set_index(index, inplace=True)
# # # df4.set_index(index, inplace=True)

fig, ax_combo = plt.subplots(figsize=[10,8])
df["count"].plot( ax=ax_combo)
df2["count"].plot(ax=ax_combo)
df3["count"].plot(ax=ax_combo)
df4["count"].plot(ax=ax_combo)
df5["avg"].plot(ax=ax_combo)
full_legend = ["KLM","Amercian_Air","British_Airways","SingaporeAir", "sentiment"]
plt.legend(full_legend)
plt.title("Tweeting over time")
plt.ylabel("Number of tweets per day")
plt.show()
# # print(df2)
# # plt.savefig("airline_plot")







