import index 
tweet = index.tweets
all_tweets = tweet.find({})

def data_preparation():

    tweet.delete_many({"id": {"$exists" : False}})

    tweet.update_many({"truncated": True}, [{"$set" : {"text" : "$extended_tweet.full_text", 
        "entities" : "$extended_tweet.entities"}}])

    tweet.update_many({"retweeted_status": {"$exists": True}}, [{"$set" : {"retweeted_status.text" : "$retweeted_status.extended_tweet.full_text", 
            "retweeted_status.entities" : "$retweeted_status.extended_tweet.entities"}}])

    tweet.update_many({"quoted_status.truncated": True}, [{"$set" : {"quoted_status.text" : "$quoted_status.extended_tweet.full_text", 
        "quoted_status.entities" : "$quoted_status.extended_tweet.entities"}}])

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

def tweet_object_cleaning():

    tweet.update_many({}, {"$unset" : {"id_str" : "", "in_reply_to_status_id_str" : "", "in_reply_to_user_id_str" : "", "geo" : "", 
    "coordinates" : "", "timestamp_ms" : "", "quoted_status_permalink" : "", "extended_entities" : "", "extended_tweet" : "",
    "display_text_range" : "", "possibly_sensitive" : "", "contributors" : "", "lang" : "", "truncated" : "", "source" : "", "quote_count" : "", "reply_count" : "", "retweet_count" : "",
    "favorite_count" : "", "favorited" : "", "retweeted" : ""}})

def retweeted_status_user_object_cleaning():

    tweet.update_many({}, {"$unset" : {"retweeted_status.user.id_str" : "", "retweeted_status.user.name" : "", 
    "retweeted_status.user.url" : "", "retweeted_status.user.translator_type" : "", "retweeted_status.user.utc_offset" : "", "retweeted_status.user.time_zone" : "", 
    "retweeted_status.user.geo_enabled": "", "retweeted_status.user.lang" : "", "retweeted_status.user.contributors_enabled" : "", "retweeted_status.user.is_translator" : "",
    "retweeted_status.user.profile_background_color" : "", "retweeted_status.user.profile_background_image_url" : "", "retweeted_status.user.profile_background_image_url_https" : "",
    "retweeted_status.user.profile_background_tile" : "", "retweeted_status.user.profile_link_color " : "", "retweeted_status.user.profile_sidebar_border_color " : "",
    "retweeted_status.user.profile_sidebar_fill_color" : "", "retweeted_status.user.profile_text_color" : "", "retweeted_status.user.profile_use_background_image" : "",
    "retweeted_status.user.profile_image_url" : "", "retweeted_status.user.profile_image_url_https" : "", "retweeted_status.user.profile_banner_url" : "", "retweeted_status.user.default_profile" : "",
    "retweeted_status.user.default_profile_image" : "", "retweeted_status.user.following" : "", "retweeted_status.user.follow_request_sent" : "", "retweeted_status.user.notifications" : "", 
    "retweeted_status.user.profile_link_color" : "", "retweeted_status.user.profile_sidebar_border_color" : "", "retweeted_status.user.listed_count" : "", "retweeted_status.user.description" : "", "retweeted_status.user.listed_count" : "", "retweeted_status.user.created_at" : ""}})

def retweeted_status_object_cleaning():

    tweet.update_many({}, {"$unset" : {"retweeted_status.id_str" : "", "retweeted_status.display_text_range" : "",
    "retweeted_status.in_reply_to_status_id_str" : "", "retweeted_status.in_reply_to_user_id_str" : "", "retweeted_status.geo" : "",
    "retweeted_status.coordinates" : "", "retweeted_status.extended_tweet" : "", "retweeted_status.quoted_status_permalink" : "", "retweeted_status.possibly_sensitive" : "",
    "retweeted_status.source" : "", "retweeted_status.truncated" : "", "retweeted_status.contributors" : ""}})

def retweeted_quoted_status_user():

    tweet.update_many({}, {"$unset" : {"retweeted_status.quoted_status.user.id_str" : "", "retweeted_status.quoted_status.user.name" : "", 
    "retweeted_status.quoted_status.user.url" : "", "retweeted_status.quoted_status.user.translator_type" : "", "retweeted_status.quoted_status.user.utc_offset" : "", "retweeted_status.quoted_status.user.time_zone" : "", 
    "retweeted_status.quoted_status.user.geo_enabled": "", "retweeted_status.quoted_status.user.lang" : "", "retweeted_status.quoted_status.user.contributors_enabled" : "", "retweeted_status.quoted_status.user.is_translator" : "",
    "retweeted_status.quoted_status.user.profile_background_color" : "", "retweeted_status.quoted_status.user.profile_background_image_url" : "", "retweeted_status.quoted_status.user.profile_background_image_url_https" : "",
    "retweeted_status.quoted_status.user.profile_background_tile" : "", "retweeted_status.quoted_status.user.profile_link_color " : "", "retweeted_status.quoted_status.user.profile_sidebar_border_color " : "",
    "retweeted_status.quoted_status.user.profile_sidebar_fill_color" : "", "retweeted_status.quoted_status.user.profile_text_color" : "", "retweeted_status.quoted_status.user.profile_use_background_image" : "",
    "retweeted_status.quoted_status.user.profile_image_url" : "", "retweeted_status.quoted_status.user.profile_image_url_https" : "", "retweeted_status.quoted_status.user.profile_banner_url" : "", "retweeted_status.quoted_status.user.default_profile" : "",
    "retweeted_status.quoted_status.user.default_profile_image" : "", "retweeted_status.quoted_status.user.following" : "", "retweeted_status.quoted_status.user.follow_request_sent" : "", "retweeted_status.quoted_status.user.notifications" : "", 
    "retweeted_status.quoted_status.user.profile_link_color" : "", "retweeted_status.quoted_status.user.profile_sidebar_border_color" : ""}})

def retweeted_quoted_status_cleaning():

    tweet.update_many({}, {"$unset" : {"retweeted_status.quoted_status.id_str" : "", 
    "retweeted_status.quoted_status.in_reply_to_status_id_str" : "", "retweeted_status.quoted_status.in_reply_to_user_id_str" : "", 
    "retweeted_status.quoted_status.geo" : "", "retweeted_status.quoted_status.coordinates" : "", "retweeted_status.quoted_status.extended_tweet" : "", 
    "retweeted_status.quoted_status.possibly_sensitive" : ""}})

def quoted_status_user_cleaning():

    tweet.update_many({}, {"$unset" : {"quoted_status.user.id_str" : "", "quoted_status.user.name" : "", 
    "quoted_status.user.url" : "", "quoted_status.user.translator_type" : "", "quoted_status.user.utc_offset" : "", "quoted_status.user.time_zone" : "", 
    "quoted_status.user.geo_enabled": "", "quoted_status.user.lang" : "", "quoted_status.user.contributors_enabled" : "", "quoted_status.user.is_translator" : "",
    "quoted_status.user.profile_background_color" : "", "quoted_status.user.profile_background_image_url" : "", "quoted_status.user.profile_background_image_url_https" : "",
    "quoted_status.user.profile_background_tile" : "", "quoted_status.user.profile_link_color " : "", "quoted_status.user.profile_sidebar_border_color " : "",
    "quoted_status.user.profile_sidebar_fill_color" : "", "quoted_status.user.profile_text_color" : "", "quoted_status.user.profile_use_background_image" : "",
    "quoted_status.user.profile_image_url" : "", "quoted_status.user.profile_image_url_https" : "", "quoted_status.user.profile_banner_url" : "", "quoted_status.user.default_profile" : "",
    "quoted_status.user.default_profile_image" : "", "quoted_status.user.following" : "", "quoted_status.user.follow_request_sent" : "", "quoted_status.user.notifications" : "", 
    "quoted_status.user.profile_link_color" : "", "quoted_status.user.profile_sidebar_border_color" : "", "quoted_status.user.listed_count" : ""}})

def quoted_status_cleaning():

    tweet.update_many({}, {"$unset" : {"quoted_status.id_str" : "", 
    "quoted_status.in_reply_to_status_id_str" : "", "quoted_status.in_reply_to_user_id_str" : "", "quoted_status.geo" : "", 
    "quoted_status.coordinates" : "", "quoted_status.extended_tweet" : "", "quoted_status.possibly_sensitive" : ""}})

def place_object_cleaning():

    tweet.update_many({}, {"$unset" : {"place.url" : "", "place.bounding_box" : "", "place.attributes" : ""}})

def tweet_entities_cleaning():

    tweet.update_many({}, {"$unset" : {"entities.urls" : "", "entities.media" : ""}})

def retweeted_status_entities():

    tweet.update_many({}, {"$unset" : {"retweeted_status.entities.urls" : "", "retweeted_status.entities.media" : ""}})

def quoted_status_entities():

    tweet.update_many({}, {"$unset" : {"quoted_status.entities.urls" : "", "quoted_status.entities.media" : ""}})

def delete_non_english_tweets():

    tweet.delete_many({"lang" : {"$ne" : "en"}})

def retweet_deletion():

    retweeted_null_tweets = tweet.find({"retweeted_status.in_reply_to_status_id" : None})

    for tweet_object in retweeted_null_tweets:
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status" : ""}})

def is_a_reply():

    null_tweets = tweet.find({"in_reply_to_status_id" : None})

    for tweet_object in null_tweets:
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"in_reply_to_status_id" : "", "in_reply_to_user_id" : "", "in_reply_to_screen_name" : ""}})
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$set" : {"is_a_reply" : False}})

def entities_cleaning():

    user_mention_tweets = tweet.find({"entities.user_mentions" : {"$ne" : None}})

    for tweet_object in user_mention_tweets:
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"entities.user_mentions.$[].name" : "", "entities.user_mentions.$[].indices" : "", "entities.user_mentions.$[].id_str" : ""}})

def retweeted_status_entities_cleaning():

    retweeted_tweets = tweet.find({"retweeted_status.entities.user_mentions" : {"$ne" : None}})

    for tweet_object in retweeted_tweets:
        tweet.update_one({"_id" : tweet_object["_id"]}, {"$unset" : {"retweeted_status.entities.user_mentions.$[].name" : "", "retweeted_status.entities.user_mentions.$[].indices" : "", "retweeted_status.entities.user_mentions.$[].id_str" : ""}})