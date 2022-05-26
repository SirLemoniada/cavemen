import pymongo

conn_str = 'mongodb://127.0.0.1:27017'

client = pymongo.MongoClient(conn_str)

cavemen=client.cavemen
tweets=cavemen.tweets
klm_conversations = cavemen.klm
British_Airways_conversations = cavemen.British_Airwaysgt 