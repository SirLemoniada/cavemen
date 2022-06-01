from unittest import skip
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
sentiment = index.sentiment

Airlines_reply = index.Airlines_reply_conversations
Users_reply_to_airlines = index.Users_reply_to_airlines_conversations
Init_from_others = index.Init_from_others_conversations
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


def airlines_reply():
    for posts in sentiment.find({'is_a_reply':True, 'user.id':{ '$in': [56377143,18332190,106062176,22536055,124476322,26223583,38676903,1542862735,253340062,218730857,45621423,20626359]}}):
        Airlines_reply.insert_one(posts)
        Airlines_reply.create_index('id')
        Airlines_reply.create_index('user.id')
        
def users_reply_to_airlines():
    for posts in sentiment.find({'in_reply_to_user_id':{'$in': [56377143,18332190,106062176,22536055,124476322,26223583,38676903,1542862735,253340062,218730857,45621423,20626359]}}):
        Users_reply_to_airlines.insert_one(posts)
        Users_reply_to_airlines.create_index('id')
        Users_reply_to_airlines.create_index('user.id')
        Users_reply_to_airlines.create_index('in_reply_to_status_id')
        Users_reply_to_airlines.create_index('in_reply_to_user_id')

def init_from_others():
    for posts in sentiment.find({'is_a_reply':False,'user.id': {'$nin': [56377143,18332190,106062176,22536055,124476322,26223583,38676903,1542862735,253340062,218730857,45621423,20626359]}}):
        Init_from_others.insert_one(posts)
        Init_from_others.create_index('id')
        Init_from_others.create_index('user.id')

def KLM_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':56377143}):

        KLM.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        KLM.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            KLM.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                KLM.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            KLM.delete_one({'id' : depth_2['id']}) 

def British_Airways_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':18332190, 'is_a_reply':True}):
        British_Airways.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        British_Airways.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            British_Airways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                British_Airways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            British_Airways.delete_one({'id' : depth_2['id']}) 

def AirFrance_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':106062176, 'is_a_reply':True}):
        AirFrance.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        AirFrance.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            AirFrance.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                AirFrance.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            AirFrance.delete_one({'id' : depth_2['id']})

def AmericanAir_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':22536055, 'is_a_reply':True}):
        AmericanAir.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        AmericanAir.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            AmericanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                AmericanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            AmericanAir.delete_one({'id' : depth_2['id']}) 

def Lufthansa_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':124476322, 'is_a_reply':True}):
        Lufthansa.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        Lufthansa.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            Lufthansa.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                Lufthansa.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            Lufthansa.delete_one({'id' : depth_2['id']})

def easyJet_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':38676903, 'is_a_reply':True}):
        easyJet.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        easyJet.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            easyJet.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                easyJet.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            easyJet.delete_one({'id' : depth_2['id']})

def RyanAir_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':1542862735, 'is_a_reply':True}):
        RyanAir.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        RyanAir.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            RyanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                RyanAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            RyanAir.delete_one({'id' : depth_2['id']})

def SingaporeAir_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':253340062, 'is_a_reply':True}):
        SingaporeAir.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        SingaporeAir.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            SingaporeAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                SingaporeAir.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            SingaporeAir.delete_one({'id' : depth_2['id']})

def Qantas_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':218730857, 'is_a_reply':True}):
        Qantas.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        Qantas.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            Qantas.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                Qantas.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            Qantas.delete_one({'id' : depth_2['id']})

def EtihadAirways_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':45621423, 'is_a_reply':True}):
        EtihadAirways.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        EtihadAirways.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            EtihadAirways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                EtihadAirways.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            EtihadAirways.delete_one({'id' : depth_2['id']})

def VirginAtlantic_conversation_start_with_others_function():
    for depth_2 in Airlines_reply.find({'user.id':20626359, 'is_a_reply':True}):
        VirginAtlantic.insert_one(depth_2)
        Airlines_reply.delete_one({'id' : depth_2['id']})
        VirginAtlantic.create_index('id')
        depth_1 = Init_from_others.find_one({"id":depth_2['in_reply_to_status_id']})
        depth_3 = Users_reply_to_airlines.find_one({'user.id':depth_2['in_reply_to_user_id'], "in_reply_to_status_id" : depth_2["id"]})
        if (depth_1 != None) :
            VirginAtlantic.update_one({'id' : depth_2['id']}, {"$set" : {"depth_1" : depth_1}})  
            Init_from_others.delete_one({'id' : depth_1['id']})
            if (depth_3 != None) :
                VirginAtlantic.update_one({'id' : depth_2['id']}, {"$set" : {"depth_3" : depth_3}})  
                Users_reply_to_airlines.delete_one({'id' : depth_3['id']})    
        else:
            VirginAtlantic.delete_one({'id' : depth_2['id']})