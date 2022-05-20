import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import pymongo

db.getSiblingDB("cavemen").tweet.aggregate( [
    { $group : { _id : "$author", books: { $push: "$title" } } },
    { $out : { db: "reporting", coll: "authors" } }
] )