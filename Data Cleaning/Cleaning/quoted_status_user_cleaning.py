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