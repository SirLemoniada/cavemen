import index #import other file
tweet = index.tweets #get tweets variable from index.py

all_tweets = tweet.find({}) # Find all tweets

for tweet_object in all_tweets: # Deletes all unnecessary information from the place object
    tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"place.url" : "", "place.bounding_box" : "", "place.attributes" : ""}})