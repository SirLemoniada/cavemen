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


def remove_wrong_time():
    tweet.delete_many({"created_at": {"$exists": False} })



def time_to_timestamp():
    all_tweets = tweet.find({})
    
    for twt in all_tweets:
        try:
            tweet.update_one({"_id" : twt["_id"]},{ "$set": { 'created_at': datetime.datetime.strptime(str(twt["created_at"]), '%a %b %d %X %z %Y') } })
        except:
            pass
from random import sample
print(sample({-1,0,1},1))














