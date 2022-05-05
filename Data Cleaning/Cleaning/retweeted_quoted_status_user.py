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