import pymongo

conn_str = 'mongodb://127.0.0.1:27017'

client = pymongo.MongoClient(conn_str)

cavemen=client.cavemen
tweets=cavemen.tweets
sentiment = cavemen.sentiment

Airlines_reply_conversations = cavemen.Airlines_reply
Users_reply_to_airlines_conversations = cavemen.Users_reply_to_airlines
Init_from_others_conversations = cavemen.Init_from_others
KLM_conversations = cavemen.KLM
British_Airways_conversations = cavemen.British_Airways 
AirFrance_conversations = cavemen.AirFrance
AmericanAir_conversations = cavemen.AmericanAir
Lufthansa_conversations = cavemen.Lufthansa
easyJet_conversations = cavemen.easyJet
RyanAir_conversations = cavemen.RyanAir
SingaporeAir_conversations = cavemen.SingaporeAir
Qantas_conversations = cavemen.Qantas
EtihadAirways_conversations = cavemen.EtihadAirways
VirginAtlantic_conversations = cavemen.VirginAtlantic


