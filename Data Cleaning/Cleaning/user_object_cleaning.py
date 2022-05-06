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