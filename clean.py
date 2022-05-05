import index #import other file
tweet = index.tweets #get tweets variable from index.py

truncated = tweet.find({"truncated": True}) #find tweets that are truncated
for object in truncated: #loop over all the tweets and replace the truncated tweet with the full text one
    tweet.update_one({"id" : object["id"]}, {"$set" : {"text" : object["extended_tweet"]["full_text"]}})

#The same, but for truncated tweets in retweeted status:
truncated_retweets = tweet.find({"retweeted_status": {"$exists": True}}) 
for object in truncated_retweets:
    if object['retweeted_status']['truncated']:
        tweet.update_one({"id" : object["id"]}, {"$set" : {"retweeted_status.text" : object["retweeted_status"]["extended_tweet"]["full_text"]}})