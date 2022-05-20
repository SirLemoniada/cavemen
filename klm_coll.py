import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import pymongo

tweet.aggregate( [
    {"$match": {"entities.user_mentions.id":56377143}},
    { "$out" : { db: "reporting", coll: "authors" } }
] )
tweet.aggregate( [ { "$addFields": { "resultObject": { $regexFind: { input: "$category", regex: /cafe/ }  } } } ] )