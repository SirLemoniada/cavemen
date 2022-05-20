import index #import index.py file
tweet = index.tweets
l = tweet.find_one({"id":1243582262123339779})
k = tweet.find_one({"id":1243582505434914818})
lst = [k["created_at"]-l["created_at"]]
print(lst)



# def sb_klm_time():
#     time_diff_list = []
#     count = 0
#     suma = 0
#     for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
#         for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
#             if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
#                 count += 1
#                 suma += reply_by_KLM["created_at"]-init_tweet["created_at"]
#     return suma/count
# print(sb_klm_time())
            
