from textblob import TextBlob
import index
import re
import pymongo
from index import tweets
tweet = index.tweets

tweets.create_index([('id',pymongo.ASCENDING)], name='sentiment_id')

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

def sentiment_analysis(text):
    if TextBlob(clean_tweet(text)).polarity > 0:
        return (1)

    elif TextBlob(clean_tweet(text)).polarity < 0:
        return (-1)
    else:
        return (0)

a = 0
b = 0
sentiment_dict = {}

found_tweets = tweet.find()

for tweet_object in found_tweets:

    output = sentiment_analysis(tweet_object["text"])
    sentiment_dict[tweet_object["id"]] = (output)

    a += 1
    print(a)

for value in sentiment_dict:
    
    tweet.update_one({"id" : value}, {"$set" : {"sentiment" : sentiment_dict[value]}})

    b += 1
    print(b)
