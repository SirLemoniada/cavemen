
from statistics import variance
from tkinter import Variable
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
klm = index.klm_conversations
British_Airways = index.British_Airways_conversations
import matplotlib.pyplot as plt
from pprint import pprint


    
# init_users_to_KLM = tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143})
# reply_to_KLM = tweet.find({"in_reply_to_user_id":56377143})
# tweets_by_KLM = tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}})

conversation_start_with_KLM = {}
conversation_start_with_British_Airways = {}


def conversation_start_with_KLM_function():
    for init_tweets_from_KLM in tweet.find({'user.id':56377143, 'is_a_reply':False}):
        for reply_to_KLM in tweet.find({"in_reply_to_user_id":56377143}):
            for tweets_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
                if (init_tweets_from_KLM['id'] == reply_to_KLM['in_reply_to_status_id']) & (tweets_by_KLM['in_reply_to_status_id'] == reply_to_KLM['id']):
                    conversation_start_with_KLM[init_tweets_from_KLM['id']] = {reply_to_KLM['id']:tweets_by_KLM['id']}
    return(conversation_start_with_KLM)   


def conversation_start_with_British_Airways_function():
    for init_tweets_from_KLM in tweet.find({'user.id':18332190, 'is_a_reply':False}):
        for reply_to_KLM in tweet.find({"in_reply_to_user_id":18332190}):
            for tweets_by_KLM in tweet.find({'user.id':18332190, "in_reply_to_status_id":{"$exists" : True}}):
                if (init_tweets_from_KLM['id'] == reply_to_KLM['in_reply_to_status_id']) & (tweets_by_KLM['in_reply_to_status_id'] == reply_to_KLM['id']):
                    conversation_start_with_British_Airways[init_tweets_from_KLM['id']] = {reply_to_KLM['id']:tweets_by_KLM['id']}
    return(conversation_start_with_British_Airways) 


def KLM_conversation_start_with_others_function():
    """Groups conversations that start with a random user, who mentions klm, klm responds to user and initial user responds to klm again (depth of 3).
    also contains tweets were KLM is mentioned, but didn't react."""
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
        klm.insert_one(init_tweet) #insert all tweets that mention KLM
        for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
            if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
                klm.update_one({'id' : reply_by_KLM["in_reply_to_status_id"]}, {"$set" : {"reply" : reply_by_KLM}}) #inserts reply from KLM as child object

    for replies in klm.find({"reply" : {"$exists" : True}}):
        for reply_to_KLM in tweet.find({"in_reply_to_user_id":56377143}):
            if (reply_to_KLM["in_reply_to_status_id"] == replies["reply"]["id"]) & (reply_to_KLM['user']['id'] == replies['user']['id']):
                klm.update_one({'reply.id' : reply_to_KLM["in_reply_to_status_id"]}, {"$set" : {"reply_to_reply" : reply_to_KLM}}) #inserts reply to reply as child object


def British_Airways_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':18332190}):
        British_Airways.insert_one(init_tweet) #insert all tweets that mention KLM
        for reply_by_British_Airways in tweet.find({'user.id':18332190, "in_reply_to_status_id":{"$exists" : True}}):
            if reply_by_British_Airways['in_reply_to_status_id'] == init_tweet['id']:
                British_Airways.update_one({'id' : reply_by_British_Airways["in_reply_to_status_id"]}, {"$set" : {"reply" : reply_by_British_Airways}}) #inserts reply from KLM as child object

    for replies in British_Airways.find({"reply" : {"$exists" : True}}):
        for reply_to_British_Airways in tweet.find({"in_reply_to_user_id":18332190}):
            if (reply_to_British_Airways["in_reply_to_status_id"] == replies["reply"]["id"]) & (reply_to_British_Airways['user']['id'] == replies['user']['id']):
                British_Airways.update_one({'reply.id' : reply_to_British_Airways["in_reply_to_status_id"]}, {"$set" : {"reply_to_reply" : reply_to_British_Airways}}) #inserts reply to reply as child object 
British_Airways_conversation_start_with_others_function()