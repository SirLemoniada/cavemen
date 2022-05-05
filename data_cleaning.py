import pymongo
from pymongo import MongoClient
import index

tweet = index.tweets 
cavemen = index.cavemen

result = tweet.find({})

# for i in result:
#     tweet.delete_one({"id_str" : i["id_str"]})

outliers = tweet.find({"id": {"$exists" : False}}) # Find all values that do not have an id

for i in outliers:
    tweet.delete_many({"_id" : i["_id"]})








