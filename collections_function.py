from unittest import skip
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet

KLM = index.KLM_conversations
British_Airways = index.British_Airways_conversations
AirFrance = index.AirFrance_conversations
AmericanAir = index.AmericanAir_conversations
Lufthansa = index.Lufthansa_conversations
AirBerlin = index.AirBerlin_conversations
easyJet = index.easyJet_conversations
RyanAir = index.RyanAir_conversations
SingaporeAir = index.SingaporeAir_conversations
Qantas = index.Qantas_conversations
EtihadAirways = index.EtihadAirways_conversations
VirginAtlantic = index.VirginAtlantic_conversations

def KLM_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':56377143, 'is_a_reply':True}):

        KLM.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            KLM.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                KLM.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            KLM.delete_one({'id' : depth_2['id']}) 

def British_Airways_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':18332190, 'is_a_reply':True}):
        British_Airways.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            British_Airways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                British_Airways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            British_Airways.delete_one({'id' : depth_2['id']}) 

def AirFrance_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':106062176, 'is_a_reply':True}):
        AirFrance.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            AirFrance.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                AirFrance.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            AirFrance.delete_one({'id' : depth_2['id']}) 

def AmericanAir_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':22536055, 'is_a_reply':True}):
        AmericanAir.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            AmericanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                AmericanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            AmericanAir.delete_one({'id' : depth_2['id']}) 

def Lufthansa_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':124476322, 'is_a_reply':True}):
        Lufthansa.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            Lufthansa.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                Lufthansa.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            Lufthansa.delete_one({'id' : depth_2['id']}) 

def AirBerlin_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':26223583, 'is_a_reply':True}):
        AirBerlin.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            AirBerlin.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                AirBerlin.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            AirBerlin.delete_one({'id' : depth_2['id']})

def easyJet_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':38676903, 'is_a_reply':True}):
        easyJet.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            easyJet.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                easyJet.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            easyJet.delete_one({'id' : depth_2['id']})

def RyanAir_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':1542862735, 'is_a_reply':True}):
        RyanAir.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            RyanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                RyanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            RyanAir.delete_one({'id' : depth_2['id']})

def SingaporeAir_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':253340062, 'is_a_reply':True}):
        SingaporeAir.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            SingaporeAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                SingaporeAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            SingaporeAir.delete_one({'id' : depth_2['id']})

def Qantas_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':218730857, 'is_a_reply':True}):
        Qantas.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            Qantas.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                Qantas.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            Qantas.delete_one({'id' : depth_2['id']})

def EtihadAirways_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':45621423, 'is_a_reply':True}):
        EtihadAirways.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            EtihadAirways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                EtihadAirways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            EtihadAirways.delete_one({'id' : depth_2['id']})

def VirginAtlantic_conversation_start_with_others_function():
    for depth_2 in tweet.find({'user.id':20626359, 'is_a_reply':True}):
        VirginAtlantic.insert_one(depth_2)
        depth_1 = tweet.find_one({"id":depth_2['in_reply_to_status_id'], 'is_a_reply':False})
        depth_3 = tweet.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            VirginAtlantic.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            if (depth_3 != None) :
                VirginAtlantic.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})      
        else:
            VirginAtlantic.delete_one({'id' : depth_2['id']})