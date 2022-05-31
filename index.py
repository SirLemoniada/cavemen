import pymongo

conn_str='mongodb://127.0.0.1:27017'

client = pymongo.MongoClient(conn_str)

cavemen=client.cavemen
tweets=cavemen.tweets
klm_conversations=cavemen.klm

screen_names = ["KLM", "AirFrance", "British_Airways", "AmericanAir", "Lufthansa", "AirBerlin", "AirBerlin assist", 
"easyJet"," RyanAir","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]

for_plot = tweets.aggregate([
    {"$match": {"user.screen_name":{"$in":screen_names}}},
   {"$group" : {"_id":{"user":"$user.screen_name",'month':{"$month":"$created_at"}, 'dayofmon':{"$dayOfMonth":"$created_at"}},"count": {"$sum":1}}},
   #{"$group" : {"_id":"$lang", "count": {"$sum":1}}},
   #{ "$push": { "created_at": <value1>, ... } }
   {"$sort": {"_id": 1}},
   {"$project": {"_id": 1, "count":1}}
])
for doc in for_plot:
    print(doc)