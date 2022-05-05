import index #import other file
tweet = index.tweets #get tweets variable from index.py

all_tweets = tweet.find({}) # Find all tweets

for tweet_object in all_tweets: # Deletes all unnecessary information from tweet object
    tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"id_str" : "", 
    "in_reply_to_status_id_str" : "", "in_reply_to_user_id_str" : "", "geo" : "", 
    "coordinates" : "", "timestamp_ms" : "", "quoted_status_permalink" : "", "extended_entities" : "", "extended_tweet" : "",
    "display_text_range" : ""}})
    