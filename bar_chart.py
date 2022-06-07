import secrets

from matplotlib.ft2font import BOLD
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import pprint
import numpy as np
import matplotlib.pyplot as plt

  
# creating the dataset




#fig = plt.figure(figsize = (10, 5))
 

 
#plt.xlabel("Airlines")

#plt.xticks(rotation = 25)
#plt.show()


screen_names = ["KLM", "airfrance", "British_Airways", "AmericanAir", "lufthansa", 
"easyJet","Ryanair","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]
result = {}
for name in screen_names:
    for_plot = tweet.aggregate([
        {"$match": {'is_a_reply':False, 'entities.user_mentions.screen_name':name}},
        {"$group":{"_id": "$lang","avgsent":{"$avg":"$sentiment"}}},
    ])
    for doc in for_plot:
        result[name] = doc["avgsent"]

result_sorted = dict(sorted(result.items(), key=lambda item: item[1]))
airlines = list(result_sorted.keys())
means = list(result_sorted.values())

# creating the bar plot
font = {"family": "normal", "weight":"bold", 'size':12}
plt.rc("font", **font)
plt.figure(figsize=(10,7))
plt.bar(airlines, means,color=['maroon','maroon','maroon','maroon','maroon','maroon','maroon','orange','maroon','maroon','maroon'],
        width = 0.6)

plt.ylabel("Mean sentiment", size=18)
plt.title("Mean sentiment per airline", size = 18)
plt.xticks(rotation = 25)
plt.show()

