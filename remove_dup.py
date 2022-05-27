import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
from pandas import DataFrame
klm = index.klm_conversations
def remove_duplicates_in_klm_db(): #leaves one of the duplicates

    duplicates = klm.aggregate([
    { "$group": {"_id":{"id":"$id"},"count": {"$sum":1}}},
    {"$sort": {"count": -1}},
    {"$match":{"count":{"$gt":1}}}
    ])
    for doc in duplicates:
        for i in range(doc["count"]-1):
            klm.delete_one({"id": doc["_id"]["id"]})

def remove_duplicates_in_tweets(): #leaves one of the duplicates

    duplicates = tweet.aggregate([
    { "$group": {"_id":{"id":"$id"},"count": {"$sum":1}}},
    {"$sort": {"count": -1}},
    {"$match":{"count":{"$gt":1}}}
    ])
    for doc in duplicates:
        for i in range(doc["count"]-1):
            tweet.delete_one({"id": doc["_id"]["id"]})

# for doc in duplicates:
#     print(doc)

tweet_dup4 = 1243655702599487488
print(tweet.count_documents({"id":1243655702599487488}))

# list_cursor = list(rem_dup)
# df = DataFrame(list_cursor)
# #df2 = df.set_index("_id")
# print(df.head(20))