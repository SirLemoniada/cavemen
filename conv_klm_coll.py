import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
klm = index.klm_conversations

def KLM_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
        klm.insert_one(init_tweet)
        for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
            if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
                klm.update_one({'id' : reply_by_KLM["in_reply_to_status_id"]}, {"$set" : {"reply" : reply_by_KLM}})

    for replies in klm.find({"reply" : {"$exists" : True}}):
        for reply_to_KLM in tweet.find({"in_reply_to_user_id":56377143}):
            if (reply_to_KLM["in_reply_to_status_id"] == replies["reply"]["id"]) & (reply_to_KLM['user']['id'] == replies['user']['id']):
                klm.update_one({'reply.id' : reply_to_KLM["in_reply_to_status_id"]}, {"$set" : {"reply_to_reply" : reply_to_KLM}})

#tweet.update_many({}, [{ "$set": { "timestamp_ms": int("timestamp_ms")}}])
#tweet.update_many({}, [{ "$set": { "timestamp_ms": {"$toDouble": "$timestamp_ms"}}}])
lst = []
lst.append((tweet.find_one({})["timestamp_ms"])/100)
lst.append(tweet.find_one({})["timestamp_ms"])
print(lst)
#tweet.update_many({}, [{ "$set": { "created_at": { "$toDate" : "$created_at" }}}])

