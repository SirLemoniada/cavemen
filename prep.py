def data_preparation():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    outliers = tweet.find({"id": {"$exists" : False}}) # Find all values that do not have an id
    for error_tweets in outliers: # Iterates through outliers and deletes them
        tweet.delete_one({"_id" : error_tweets["_id"]})

    possibly_sensitive_tweets = tweet.find({"possibly_sensitive": {"$exists": False}}) # Finds all tweets that do not have possibly_sensitive atttribute
    for tweet_object in possibly_sensitive_tweets: # Loop over all the tweets and add possibly sensitive = und
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"possibly_sensitive" : "und"}})

    truncated = tweet.find({"truncated": True}) # Find tweets that are truncated
    for tweet_object in truncated: # Loop over all the tweets and replace the truncated tweet with the full text one
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"text" : tweet_object["extended_tweet"]["full_text"]}})

    truncated = tweet.find({"truncated": True}) # Find tweets that are truncated
    for tweet_object in truncated: # Exchanges entities from extended tweet to the tweet object for truncated tweets
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"entities" : tweet_object["extended_tweet"]["entities"]}})

    truncated_retweets = tweet.find({"retweeted_status": {"$exists": True}}) # Find tweets that are truncated inside retweeted status
    for tweet_object in truncated_retweets: # Loop over all the tweets and replace the truncated tweet with the full text inside retweeded_status object
        if tweet_object['retweeted_status']['truncated']:
            tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"retweeted_status.text" : tweet_object["retweeted_status"]["extended_tweet"]["full_text"]}})

    truncated_retweets = tweet.find({"retweeted_status": {"$exists": True}}) # Find tweets that are truncated inside retweeted status
    for tweet_object in truncated_retweets: # Exchanges entities from extended tweet to the tweet object for truncated tweets in retweeted status object
        if tweet_object['retweeted_status']['truncated']:
            tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"retweeted_status.entities" : tweet_object["retweeted_status"]["extended_tweet"]["entities"]}})

    truncated_quoted_status = tweet.find({"quoted_status.truncated": True}) # Find tweets that are truncated in quoted status
    for tweet_object in truncated_quoted_status: # Loop over all the tweets and replace the truncated tweet with the full text one
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"quoted_status.text" : tweet_object["quoted_status"]["extended_tweet"]["full_text"]}})

    truncated_quoted_status = tweet.find({"quoted_status.truncated": {"$exists": True}}) # Find tweets that are truncated inside quoted status object
    for tweet_object in truncated_quoted_status: # Exchanges entities from extended tweet to the tweet object for truncated tweets in quoted status object
        if tweet_object['quoted_status']['truncated']:
            tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"quoted_status.entities" : tweet_object["quoted_status"]["extended_tweet"]["entities"]}})