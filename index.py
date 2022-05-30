import pymongo

conn_str = 'mongodb://127.0.0.1:27017'

client = pymongo.MongoClient(conn_str)

cavemen=client.cavemen
tweets=cavemen.tweets
KLM_conversations = cavemen.KLM
British_Airways_conversations = cavemen.British_Airways 
AirFrance_conversations = cavemen.AirFrance
AmericanAir_conversations = cavemen.AmericanAir
Lufthansa_conversations = cavemen.Lufthansa
AirBerlin_conversations = cavemen.AirBerlin
AirBerlin_assist_conversations = cavemen.AirBerlin_assist
easyJet_conversations = cavemen.easyJet
RyanAir_conversations = cavemen.RyanAir
SingaporeAir_conversations = cavemen.SingaporeAir
Qantas_conversations = cavemen.Qantas
EtihadAirways_conversations = cavemen.EtihadAirways
VirginAtlantic_conversations = cavemen.VirginAtlantic


