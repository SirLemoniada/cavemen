from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

from index import tweets
from index import AirFrance_conversations
from index import KLM_conversations
from index import British_Airways_conversations
from index import AmericanAir_conversations
from index import Lufthansa_conversations
from index import easyJet_conversations
from index import RyanAir_conversations
from index import SingaporeAir_conversations
from index import Qantas_conversations
from index import EtihadAirways_conversations
from index import VirginAtlantic_conversations

# time = [1]

# for tweet in tweets.find({"entities.user_mentions.id":56377143, 'is_a_reply':False, "sentiment":-1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}}):
#     print(tweet["id"])

# dct_weeks = 

# for week in range(1,2):
#     total = tweets.count_documents({ "$expr": { "$eq": [{ "$week": "$created_at" }, week]}, 'is_a_reply':False, 'entities.user_mentions.id':56377143, 'sentiment':-1})
#     #negative_to_positive = KLM_conversations.count_documents({ "$expr": { "$eq": [{ "$week": "$created_at" }, week]},'depth_3':{'$exists':True}, 'depth_1.sentiment':-1, 'depth_3.sentiment':{'$in':[0, 1]}})

# print(total)

for_plot = tweets.aggregate([
    {"$match": {'is_a_reply':False, 'entities.user_mentions.id':56377143}},
   {"$group" : {"_id":{"year":{"$year":"$created_at"}, "week": {"$week":"$created_at"}}, "count": {"$sum":1}}}
])
list_cursor = list(for_plot)
df = DataFrame(list_cursor)
print(df)