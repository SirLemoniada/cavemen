import index #import other file
tweet = index.tweets #get tweets variable from index.py

all_tweets = tweet.find({}) # Find all tweets

for tweet_object in all_tweets: # Deletes all unnecessary information from the quoted status object
    tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status.quoted_status.id_str" : "", 
    "retweeted_status.quoted_status.in_reply_to_status_id_str" : "", "retweeted_status.quoted_status.in_reply_to_user_id_str" : "", 
    "retweeted_status.quoted_status.geo" : "", "retweeted_status.quoted_status.coordinates" : "", "retweeted_status.quoted_status.extended_tweet" : ""}})