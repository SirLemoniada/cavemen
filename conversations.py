import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
klm = index.klm_conversations

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

KLM_conversation_start_with_others_function()