from textblob import TextBlob
import index
import re
tweet = index.tweets

tweet_text = tweet.find({})

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

for tweet_object in tweet_text:

    clean_text = clean_tweet(tweet_object["text"])

    if TextBlob(clean_text).polarity > 0:
        tweet.update_one({"id" : tweet_object["id"]}, {"$set" : {"sentiment" : "Positive"}})

    elif TextBlob(clean_text).polarity < 0:
        tweet.update_one({"id" : tweet_object["id"]}, {"$set" : {"sentiment" : "Negative"}})

    else:
        tweet.update_one({"id" : tweet_object["id"]}, {"$set" : {"sentiment" : "Neutral"}})
    
    