import index 
tweet = index.tweets
all_tweets = tweet.find({})

def delete_non_english_tweets():

    tweet.delete_many({"lang" : {"$ne" : "en"}})

def data_preparation():

    tweet.delete_many({"id": {"$exists" : False}})

    tweet.update_many({"truncated": True}, [{"$set" : {"text" : "$extended_tweet.full_text", 
        "entities" : "$extended_tweet.entities"}}])

    tweet.update_many({"retweeted_status": {"$exists" : True}}, {"$set" : {"is_a_retweet" : True}})
    tweet.update_many({"retweeted_status.truncated" : True}, [{"$set" : {"text" : "$retweeted_status.extended_tweet.full_text"}}])
    tweet.update_many({"retweeted_status.truncated" : False}, [{"$set" : {"text" : "$retweeted_status.text"}}])
    tweet.update_many({}, [{ "$set": { "created_at": { "$toDate" : "$created_at" }}}])

    for tweet_object in all_tweets:

        tweet.update_one({}, {"$set" : {"timestap_ms" : int(tweet_object["timestamp_ms"])}})

def is_a_reply():

    tweet.update_many({"in_reply_to_status_id" : None}, {"$unset" : {"in_reply_to_status_id" : "", "in_reply_to_user_id" : "", 
    "in_reply_to_screen_name" : ""}, "$set" : {"is_a_reply" : False}})

    tweet.update_many({"in_reply_to_status_id" : {"$ne" : None}}, {"$set" : {"is_a_reply" : True}})

def place_object():

    tweet.update_many({}, [{"$set" : {"place_country" : "$place.country"}}])
    tweet.update_many({"place" : None}, {"$set" : {"place_information" : None}})

def tweet_object_cleaning():

    tweet.update_many({}, {"$unset" : {"id_str" : "", "in_reply_to_status_id_str" : "", "in_reply_to_user_id_str" : "", "geo" : "", 
    "coordinates" : "", "quoted_status_permalink" : "", "extended_entities" : "", "extended_tweet" : "",
    "display_text_range" : "", "possibly_sensitive" : "", "contributors" : "", "truncated" : "", "source" : "", "quote_count" : "", "reply_count" : "", "retweet_count" : "",
    "favorite_count" : "", "favorited" : "", "retweeted" : "", "retweeted_status" : "", "quoted_status" : "", "quoted_status_id_str" : "", "place" : ""}})

def user_object_cleaning():

    tweet.update_many({}, {"$unset" : {"user.id_str" : "", "user.name" : "", 
    "user.url" : "", "user.translator_type" : "", "user.utc_offset" : "", "user.time_zone" : "", 
    "user.geo_enabled": "", "user.lang" : "", "user.contributors_enabled" : "", "user.is_translator" : "",
    "user.profile_background_color" : "", "user.profile_background_image_url" : "", "user.profile_background_image_url_https" : "",
    "user.profile_background_tile" : "", "user.profile_link_color " : "", "user.profile_sidebar_border_color " : "",
    "user.profile_sidebar_fill_color" : "", "user.profile_text_color" : "", "user.profile_use_background_image" : "",
    "user.profile_image_url" : "", "user.profile_image_url_https" : "", "user.profile_banner_url" : "", "user.default_profile" : "",
    "user.default_profile_image" : "", "user.following" : "", "user.follow_request_sent" : "", "user.notifications" : "", 
    "user.profile_link_color" : "", "user.profile_sidebar_border_color" : "", "user.description" : "", "user.created_at" : "", "user.listed_count" : ""}})

def tweet_entities_cleaning():

    tweet.update_many({}, {"$unset" : {"entities.urls" : "", "entities.media" : ""}})

def entities_cleaning():
    
    tweet.update_many({"entities.user_mentions" : {"$ne" : None}}, {"$unset" : {"entities.user_mentions.$[].name" : "", 
    "entities.user_mentions.$[].indices" : "", "entities.user_mentions.$[].id_str" : ""}})