import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet

KLM = index.KLM_conversations
British_Airways = index.British_Airways_conversations
AirFrance = index.AirFrance_conversations
AmericanAir = index.AmericanAir_conversations
Lufthansa = index.Lufthansa_conversations
AirBerlin = index.AirBerlin_conversations
AirBerlin_assist = index.AirBerlin_assist_conversations
easyJet = index.easyJet_conversations
RyanAir = index.RyanAir_conversations
SingaporeAir = index.SingaporeAir_conversations
Qantas = index.Qantas_conversations
EtihadAirways = index.EtihadAirways_conversations
VirginAtlantic = index.VirginAtlantic_conversations

def KLM_conversation_start_with_others_function():
    """Groups conversations that start with a random user, who mentions klm, klm responds to user and initial user responds to klm again (depth of 3).
    also contains tweets were KLM is mentioned, but didn't react."""
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':56377143}):
        KLM.insert_one(init_tweet) #insert all tweets that mention KLM
        reply = tweet.find_one({'user.id':56377143, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            KLM.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}}) #inserts reply from KLM as child object

    for replies in KLM.find({"depth_2" : {"$exists" : True}}):
        reply_to_KLM = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_KLM != None:
            KLM.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_KLM}}) #inserts reply to reply as child object

    # for replies in klm.find({"depth_3" : {"$exists" : True}}):
    #     reply = tweet.find_one({'user.id':56377143, "in_reply_to_status_id":replies["depth_3"]["id"]})
    #     if reply != None:
    #         klm.update_one({'id' : replies["id"]}, {"$set" : {"depth_4" : reply}})  

    # for replies in klm.find({"depth_4" : {"$exists" : True}}):
    #     reply_to_KLM = tweet.find_one({"in_reply_to_status_id":replies["depth_4"]["id"]})
    #     if reply_to_KLM != None:
    #         klm.update_one({'id' : replies["id"]}, {"$set" : {"depth_5" : reply}})    

def British_Airways_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':18332190}):
        British_Airways.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':18332190, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            British_Airways.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in British_Airways.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            British_Airways.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def AirFrance_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':106062176}):
        AirFrance.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':106062176, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            AirFrance.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in AirFrance.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            AirFrance.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def AmericanAir_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':22536055}):
        AmericanAir.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':22536055, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            AmericanAir.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in AmericanAir.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            AmericanAir.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def Lufthansa_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':124476322}):
        Lufthansa.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':124476322, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            Lufthansa.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in Lufthansa.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            Lufthansa.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def AirBerlin_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':26223583}):
        AirBerlin.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':26223583, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            AirBerlin.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in AirBerlin.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            AirBerlin.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def AirBerlin_assist_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':2182373406}):
        AirBerlin_assist.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':2182373406, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            AirBerlin_assist.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in AirBerlin_assist.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            AirBerlin_assist.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})
def easyJet_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':38676903}):
        easyJet.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':38676903, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            easyJet.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in easyJet.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            easyJet.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def RyanAir_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':1542862735}):
        RyanAir.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':1542862735, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            RyanAir.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in RyanAir.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            RyanAir.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def SingaporeAir_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':253340062}):
        SingaporeAir.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':253340062, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            SingaporeAir.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in SingaporeAir.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            SingaporeAir.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def Qantas_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':218730857}):
        Qantas.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':218730857, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            Qantas.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in Qantas.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            Qantas.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def EtihadAirways_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':45621423}):
        EtihadAirways.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':45621423, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            EtihadAirways.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in EtihadAirways.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            EtihadAirways.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

def VirginAtlantic_conversation_start_with_others_function():
    for init_tweet in tweet.find({'is_a_reply':False, 'entities.user_mentions.id':20626359}):
        VirginAtlantic.insert_one(init_tweet) 
        reply = tweet.find_one({'user.id':20626359, "in_reply_to_status_id":init_tweet['id']})
        if reply != None:
            VirginAtlantic.update_one({'id' : init_tweet['id']}, {"$set" : {"depth_2" : reply}})

    for replies in VirginAtlantic.find({"depth_2" : {"$exists" : True}}):
        reply_to_airline = tweet.find_one({"in_reply_to_status_id":replies["depth_2"]["id"]})
        if reply_to_airline != None:
            VirginAtlantic.update_one({'id' : replies["id"]}, {"$set" : {"depth_3" : reply_to_airline}})

AirBerlin_assist_conversation_start_with_others_function()