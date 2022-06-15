import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet

from index import AirFrance_conversations
from index import KLM_conversations
from index import British_Airways_conversations
from index import AmericanAir_conversations
from index import Lufthansa_conversations
from index import easyJet_conversations
from index import RyanAir_conversations
from index import SingaporeAir_conversations
from index import Qantas_conversations
from index import EtihadAirways_conversations
from index import VirginAtlantic_conversations

airline_list = [AirFrance_conversations, KLM_conversations, British_Airways_conversations, AmericanAir_conversations, Lufthansa_conversations,
easyJet_conversations, RyanAir_conversations, SingaporeAir_conversations, Qantas_conversations, EtihadAirways_conversations,
 VirginAtlantic_conversations]

a = 0

for airline in airline_list:
    for value in airline.find({}):

        a += 1
        diff = (value["created_at"] - value["depth_1"]["created_at"]).total_seconds()
        airline.update_one({"id" : value["id"]}, {"$set" : {"diff_inn_to_rep" : diff}})
        print(a)