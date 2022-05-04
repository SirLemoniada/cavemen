import index
tweet = index.tweets

results = tweet.find({"truncated": True})

for result in results:
    tweet.update_one({"id" : result["id"]}, {"$set" : {"text" : result["extended_tweet"]["full_text"]}})
