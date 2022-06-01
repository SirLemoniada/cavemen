from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import index
import re
tweet = index.tweets

tweet_text = tweet.find({})

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

for tweet_object in tweet_text:

    clean_text = clean_tweet(tweet_object["text"])
    sentiment_dict = SentimentIntensityAnalyzer().polarity_scores(clean_text)

    if sentiment_dict["compound"] >= 0.05:
        tweet.update_one({"id" : tweet_object["id"]}, {"$set" : {"sentiment" : "Positive"}})

    elif sentiment_dict['compound'] <= -0.05:
        tweet.update_one({"id" : tweet_object["id"]}, {"$set" : {"sentiment" : "Negative"}})

    else:
        tweet.update_one({"id" : tweet_object["id"]}, {"$set" : {"sentiment" : "Neutral"}})
    
    