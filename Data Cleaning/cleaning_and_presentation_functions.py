def data_preparation():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

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

def user_object_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the user object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"user.id_str" : "", "user.name" : "", 
        "user.url" : "", "user.translator_type" : "", "user.utc_offset" : "", "user.time_zone" : "", 
        "user.geo_enabled": "", "user.lang" : "", "user.contributors_enabled" : "", "user.is_translator" : "",
        "user.profile_background_color" : "", "user.profile_background_image_url" : "", "user.profile_background_image_url_https" : "",
        "user.profile_background_tile" : "", "user.profile_link_color " : "", "user.profile_sidebar_border_color " : "",
        "user.profile_sidebar_fill_color" : "", "user.profile_text_color" : "", "user.profile_use_background_image" : "",
        "user.profile_image_url" : "", "user.profile_image_url_https" : "", "user.profile_banner_url" : "", "user.default_profile" : "",
        "user.default_profile_image" : "", "user.following" : "", "user.follow_request_sent" : "", "user.notifications" : "", 
        "user.profile_link_color" : "", "user.profile_sidebar_border_color" : ""}})

def tweet_object_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from tweet object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"id_str" : "", 
        "in_reply_to_status_id_str" : "", "in_reply_to_user_id_str" : "", "geo" : "", 
        "coordinates" : "", "timestamp_ms" : "", "quoted_status_permalink" : "", "extended_entities" : "", "extended_tweet" : "",
        "display_text_range" : ""}})

def retweeted_status_user_object_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the retweeted_status.user object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status.user.id_str" : "", "retweeted_status.user.name" : "", 
        "retweeted_status.user.url" : "", "retweeted_status.user.translator_type" : "", "retweeted_status.user.utc_offset" : "", "retweeted_status.user.time_zone" : "", 
        "retweeted_status.user.geo_enabled": "", "retweeted_status.user.lang" : "", "retweeted_status.user.contributors_enabled" : "", "retweeted_status.user.is_translator" : "",
        "retweeted_status.user.profile_background_color" : "", "retweeted_status.user.profile_background_image_url" : "", "retweeted_status.user.profile_background_image_url_https" : "",
        "retweeted_status.user.profile_background_tile" : "", "retweeted_status.user.profile_link_color " : "", "retweeted_status.user.profile_sidebar_border_color " : "",
        "retweeted_status.user.profile_sidebar_fill_color" : "", "retweeted_status.user.profile_text_color" : "", "retweeted_status.user.profile_use_background_image" : "",
        "retweeted_status.user.profile_image_url" : "", "retweeted_status.user.profile_image_url_https" : "", "retweeted_status.user.profile_banner_url" : "", "retweeted_status.user.default_profile" : "",
        "retweeted_status.user.default_profile_image" : "", "retweeted_status.user.following" : "", "retweeted_status.user.follow_request_sent" : "", "retweeted_status.user.notifications" : "", 
        "retweeted_status.user.profile_link_color" : "", "retweeted_status.user.profile_sidebar_border_color" : ""}})

def retweeted_status_object_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the retweeted_status object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status.id_str" : "", "retweeted_status.display_text_range" : "",
        "retweeted_status.in_reply_to_status_id_str" : "", "retweeted_status.in_reply_to_user_id_str" : "", "retweeted_status.geo" : "",
        "retweeted_status.coordinates" : "", "retweeted_status.extended_tweet" : "", "retweeted_status.quoted_status_permalink" : ""}})

def retweeted_status_object_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the retweeted_status object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status.id_str" : "", "retweeted_status.display_text_range" : "",
        "retweeted_status.in_reply_to_status_id_str" : "", "retweeted_status.in_reply_to_user_id_str" : "", "retweeted_status.geo" : "",
        "retweeted_status.coordinates" : "", "retweeted_status.extended_tweet" : "", "retweeted_status.quoted_status_permalink" : ""}})

def retweeted_quoted_status_user():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the user object in quoted status object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status.quoted_status.user.id_str" : "", "retweeted_status.quoted_status.user.name" : "", 
        "retweeted_status.quoted_status.user.url" : "", "retweeted_status.quoted_status.user.translator_type" : "", "retweeted_status.quoted_status.user.utc_offset" : "", "retweeted_status.quoted_status.user.time_zone" : "", 
        "retweeted_status.quoted_status.user.geo_enabled": "", "retweeted_status.quoted_status.user.lang" : "", "retweeted_status.quoted_status.user.contributors_enabled" : "", "retweeted_status.quoted_status.user.is_translator" : "",
        "retweeted_status.quoted_status.user.profile_background_color" : "", "retweeted_status.quoted_status.user.profile_background_image_url" : "", "retweeted_status.quoted_status.user.profile_background_image_url_https" : "",
        "retweeted_status.quoted_status.user.profile_background_tile" : "", "retweeted_status.quoted_status.user.profile_link_color " : "", "retweeted_status.quoted_status.user.profile_sidebar_border_color " : "",
        "retweeted_status.quoted_status.user.profile_sidebar_fill_color" : "", "retweeted_status.quoted_status.user.profile_text_color" : "", "retweeted_status.quoted_status.user.profile_use_background_image" : "",
        "retweeted_status.quoted_status.user.profile_image_url" : "", "retweeted_status.quoted_status.user.profile_image_url_https" : "", "retweeted_status.quoted_status.user.profile_banner_url" : "", "retweeted_status.quoted_status.user.default_profile" : "",
        "retweeted_status.quoted_status.user.default_profile_image" : "", "retweeted_status.quoted_status.user.following" : "", "retweeted_status.quoted_status.user.follow_request_sent" : "", "retweeted_status.quoted_status.user.notifications" : "", 
        "retweeted_status.quoted_status.user.profile_link_color" : "", "retweeted_status.quoted_status.user.profile_sidebar_border_color" : ""}})

def retweeted_quoted_status_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the quoted status object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status.quoted_status.id_str" : "", 
        "retweeted_status.quoted_status.in_reply_to_status_id_str" : "", "retweeted_status.quoted_status.in_reply_to_user_id_str" : "", 
        "retweeted_status.quoted_status.geo" : "", "retweeted_status.quoted_status.coordinates" : "", "retweeted_status.quoted_status.extended_tweet" : ""}})

def quoted_status_user_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the user object in quoted status object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"quoted_status.user.id_str" : "", "quoted_status.user.name" : "", 
        "quoted_status.user.url" : "", "quoted_status.user.translator_type" : "", "quoted_status.user.utc_offset" : "", "quoted_status.user.time_zone" : "", 
        "quoted_status.user.geo_enabled": "", "quoted_status.user.lang" : "", "quoted_status.user.contributors_enabled" : "", "quoted_status.user.is_translator" : "",
        "quoted_status.user.profile_background_color" : "", "quoted_status.user.profile_background_image_url" : "", "quoted_status.user.profile_background_image_url_https" : "",
        "quoted_status.user.profile_background_tile" : "", "quoted_status.user.profile_link_color " : "", "quoted_status.user.profile_sidebar_border_color " : "",
        "quoted_status.user.profile_sidebar_fill_color" : "", "quoted_status.user.profile_text_color" : "", "quoted_status.user.profile_use_background_image" : "",
        "quoted_status.user.profile_image_url" : "", "quoted_status.user.profile_image_url_https" : "", "quoted_status.user.profile_banner_url" : "", "quoted_status.user.default_profile" : "",
        "quoted_status.user.default_profile_image" : "", "quoted_status.user.following" : "", "quoted_status.user.follow_request_sent" : "", "quoted_status.user.notifications" : "", 
        "quoted_status.user.profile_link_color" : "", "quoted_status.user.profile_sidebar_border_color" : ""}})

def quoted_status_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the quoted status object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"quoted_status.id_str" : "", 
        "quoted_status.in_reply_to_status_id_str" : "", "quoted_status.in_reply_to_user_id_str" : "", "quoted_status.geo" : "", 
        "quoted_status.coordinates" : "", "quoted_status.extended_tweet" : ""}})

def place_object_cleaning():

    import index #import other file
    tweet = index.tweets #get tweets variable from index.py

    all_tweets = tweet.find({}) # Find all tweets

    for tweet_object in all_tweets: # Deletes all unnecessary information from the place object
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"place.url" : "", "place.bounding_box" : "", "place.attributes" : ""}})

def print_hello():

    print("hello")