import index 
import time
tweet = index.tweets
all_tweets = tweet.find({})
import datetime

def delete_non_english_tweets():

    tweet.delete_many({"lang" : {"$ne" : "en"}})

def removing_duplicates():

    duplicates = tweet.aggregate([
    {"$group": {"_id":{"id":"$id"},"count": {"$sum":1}}},
    {"$sort": {"count": -1}},
    {"$match":{"count":{"$gt":1}}}
    ], allowDiskUse = True)
    for doc in duplicates:
        for i in range(doc["count"]-1):
            tweet.delete_one({"id": doc["_id"]["id"]})

def data_preparation():

    tweet.delete_many({"id": {"$exists" : False}})

    tweet.update_many({"truncated": True}, [{"$set" : {"text" : "$extended_tweet.full_text", 
        "entities" : "$extended_tweet.entities"}}])

    tweet.update_many({"retweeted_status": {"$exists" : True}}, {"$set" : {"is_a_retweet" : True}})
    tweet.update_many({"retweeted_status.truncated" : True}, [{"$set" : {"text" : "$retweeted_status.extended_tweet.full_text"}}])
    tweet.update_many({"retweeted_status.truncated" : False}, [{"$set" : {"text" : "$retweeted_status.text"}}])

def is_a_reply():

    tweet.update_many({"in_reply_to_status_id" : None}, {"$unset" : {"in_reply_to_status_id" : "", "in_reply_to_user_id" : "", 
    "in_reply_to_screen_name" : ""}, "$set" : {"is_a_reply" : False}})

def tweet_object_cleaning():

    tweet.update_many({}, {"$unset" : {"id_str" : "", "in_reply_to_status_id_str" : "", "in_reply_to_user_id_str" : "", "geo" : "", 
    "coordinates" : "", "quoted_status_permalink" : "", "extended_entities" : "", "extended_tweet" : "",
    "display_text_range" : "", "possibly_sensitive" : "", "contributors" : "", "truncated" : "", "source" : "", "quote_count" : "", "reply_count" : "", "retweet_count" : "",
    "favorite_count" : "", "favorited" : "", "retweeted" : "", "retweeted_status" : "", "quoted_status" : "", "quoted_status_id_str" : ""}})

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

def place_object_cleaning():

    tweet.update_many({}, {"$unset" : {"place.url" : "", "place.bounding_box" : "", "place.attributes" : ""}})

def tweet_entities_cleaning():

    tweet.update_many({}, {"$unset" : {"entities.urls" : "", "entities.media" : ""}})

def entities_cleaning():
    
    tweet.update_many({"entities.user_mentions" : {"$ne" : None}}, {"$unset" : {"entities.user_mentions.$[].name" : "", 
    "entities.user_mentions.$[].indices" : "", "entities.user_mentions.$[].id_str" : ""}})

def time_to_timestamp():
    
    for tweet_object in all_tweets:
        
        tweet.update_one({"_id" : tweet_object["_id"]},{ "$set": { 'created_at': datetime.datetime.strptime(str(tweet_object["created_at"]), '%a %b %d %X %z %Y')}})


