import collections_function
from index import tweets
import pymongo

tweets.create_index([('id',pymongo.ASCENDING),('is_a_reply',pymongo.ASCENDING)],name='d1')
tweets.create_index([('user.id',pymongo.ASCENDING),('is_a_reply',pymongo.ASCENDING)],name='d3')

print('airlines_reply start')
collections_function.airlines_reply()
print('airlines_reply done')
print('users_reply_to_airlines start')
collections_function.users_reply_to_airlines()
print('users_reply_to_airlines done')
print('init_from_others start')
collections_function.init_from_others()
print('init_from_others done')
print('KLM start')
collections_function.KLM_conversation_start_with_others_function()
print('KLM done')
print('British Airways start')
collections_function.British_Airways_conversation_start_with_others_function()
print('British Airways done')
print('Air France start')
collections_function.AirFrance_conversation_start_with_others_function()
print('Air France done')
print('American Air start')
collections_function.AmericanAir_conversation_start_with_others_function()
print('American Air done')
print('Lufthansa start')
collections_function.Lufthansa_conversation_start_with_others_function()
print('Lufthansa done')
print('easyJet start')
collections_function.easyJet_conversation_start_with_others_function()
print('easyJet done')
print('RyanAir start')
collections_function.RyanAir_conversation_start_with_others_function()
print('RyanAir done')
print('Singapore Air start')
collections_function.SingaporeAir_conversation_start_with_others_function()
print('Singapore Air done')
print('Quantas start')
collections_function.Qantas_conversation_start_with_others_function()
print('Quantas done')
print('Etihad start')
collections_function.EtihadAirways_conversation_start_with_others_function()
print('Etihad done')
print('Virgin start')
collections_function.VirginAtlantic_conversation_start_with_others_function()
print('Virgin done')