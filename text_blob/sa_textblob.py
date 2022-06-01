from textblob import TextBlob
import index
import re
tweet = index.tweets
sntm = index.sentiment_analysis

# tweet.update_many({"sentiment" : {"$exists" : True}}, {"$unset" : {"sentiment" : ""}})

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

    b += 1

    tweet.update_one({"id" : value}, {"$set" : {"sentiment" : sentiment_dict[value]}})
    tweet_object = tweet.find_one({"id" : value})
    sntm.insert_one(tweet_object)
    tweet.delete_one({"id" : value})

    print(b)



