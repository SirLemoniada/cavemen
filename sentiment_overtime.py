from pprint import pprint
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt
import pprint
from pandas import DataFrame
for_plot = tweet.aggregate([
    {"$match": {'is_a_reply':False, 'entities.user_mentions.id':56377143}},
   {"$group" : {"_id":{"year":{"$year":"$created_at"},'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}},"avg": {"$avg":"$sentiment"}}},
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 1, "avg":1}}
])
list_cursor = list(for_plot)
df = DataFrame(list_cursor)
df["avg"].plot()
plt.show()