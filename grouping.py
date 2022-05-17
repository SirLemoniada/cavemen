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

for_plot = tweet.aggregate([
    #{ "$unwind": "$user.screen_name" },
   {"$match": {"entities.user_mentions.id":56377143}},
   #{"$group" : {"_id":{"user":"$user.screen_name", 'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}, 'hour':{"$hour":"$created_at"}},"count": {"$sum":1}}},
   {"$group" : {"_id":"$lang", "count": {"$sum":1}}},
   {"$sort": {"count": -1}},
   #{"$project": {"lang":1, "_id":1, "created_at":1, "user.screen_name":1}},
   {"$limit":5}
])
for doc in for_plot:
    pprint.pprint(doc)