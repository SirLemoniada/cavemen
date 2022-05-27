import index #import index.py file
tweet = index.tweets
klm = index.klm_conversations
import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt
l = tweet.find_one({"id":1243582262123339779})
k = tweet.find_one({"id":1243582505434914818})
# lst = [k["created_at"]-l["created_at"]]
# print(lst)
s = "123"
print(int(s))

# lst = [1,3,5]
# lst2 = [1,5,10]
# plt.boxplot([lst,lst2],labels=['KLM','british'])
# plt.show()
# print(DataFrame(lst))


def sb_klm_time():
    time_passed = []
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
        for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
            if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
                diff_in_min =  (reply_by_KLM["timestamp_ms"])-(init_tweet["timestamp_ms"])/1000/60
                time_passed.append(diff_in_min)
    return time_passed
def reverse_klm_time():
    time_passed = []
    for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
        for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143, }):
            if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
                diff_in_min =  (reply_by_KLM["timestamp_ms"])-(init_tweet["timestamp_ms"])/1000/60
                time_passed.append(diff_in_min)
    return time_passed
#print(sb_klm_time())
# time_passed = []
# for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
#         for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
#             if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
#                 print((reply_by_KLM["timestamp_ms"])-(init_tweet["timestamp_ms"])/1000/60)
#                 #time_passed.append(diff_in_min)

# print(tweet.count_documents({'is_a_reply':False, 'entities.user_mentions.id':56377143}))
print(tweet.count_documents({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}))
#for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
    print(reply_by_KLM)
        # if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
        #     print(1)