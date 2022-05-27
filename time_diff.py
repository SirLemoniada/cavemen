import index #import index.py file
tweet = index.tweets
import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt
l = tweet.find_one({"id":1243582262123339779})
k = tweet.find_one({"id":1243582505434914818})
# lst = [k["created_at"]-l["created_at"]]
# print(lst)
s = "123"
print(int(s))

lst = [1,3,5]
lst2 = [1,5,10]
plt.boxplot([lst,lst2],labels=['KLM','british'])
plt.show()
# print(DataFrame(lst))

def sb_klm_time():
    time_passed = []
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
        for reply_by_KLM in tweet.find({'user.id':56377143, "in_reply_to_status_id":{"$exists" : True}}):
            if reply_by_KLM['in_reply_to_status_id'] == init_tweet['id']:
                diff_in_min =  (int(reply_by_KLM["timestamp_ms"])-int(init_tweet["timestamp_ms"]))/1000/60
                time_passed.append(diff_in_min)
    return time_passed
print(sb_klm_time())

# list_cursor = list(test)
# df = DataFrame(list_cursor)
# #df2 = df.set_index("_id")
# print(df.head(10))
# def convertMillis():
#     seconds=(451851.0/1000)%60
#     minutes=(451851.0/(1000*60))%60
#     hours=(451851.0/(1000*60*60))%24

#     return print(hours,":",minutes,":",seconds)
# print(convertMillis())
# print(451851.0/1000/60)
