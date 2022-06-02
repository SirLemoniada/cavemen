
import pymongo
import pandas as pd
import datetime
import pprint
from collections import OrderedDict
from pandas import DataFrame

import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt

KLM = index.KLM_conversations

pprint.pprint(tweet.find({'user.id':56377143, 'is_a_reply':True}).explain())

# def KLM_conversation_start_with_others_function():
#     for depth_2 in tweet.find({'user.id':56377143, 'is_a_reply':True}):

#         KLM.insert_one(depth_2)
#         depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
#         depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
#         if (depth_1 != None) :
#             KLM.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
#             if (depth_3 != None) :
#                 KLM.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
#         else:
#             KLM.delete_one({'id' : depth_2['id']})
#KLM_conversation_start_with_others_function()
#15 conv in one minute
#7k conv in on eminute