import index #import index.py file
from index import tweets,cavemen
import pymongo
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

KLM = index.KLM_conversations
British_Airways = index.British_Airways_conversations
AirFrance = index.AirFrance_conversations
AmericanAir = index.AmericanAir_conversations
Lufthansa = index.Lufthansa_conversations
easyJet = index.easyJet_conversations
RyanAir = index.RyanAir_conversations
SingaporeAir = index.SingaporeAir_conversations
Qantas = index.Qantas_conversations
EtihadAirways = index.EtihadAirways_conversations
VirginAtlantic = index.VirginAtlantic_conversations

tweets.create_index([('is_a_reply',pymongo.ASCENDING),('entities.user_mentions.screen_name',pymongo.ASCENDING)],name='for_barchart')
KLM.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
KLM.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
British_Airways.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
British_Airways.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
AirFrance.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
AirFrance.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
AmericanAir.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
AmericanAir.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
Lufthansa.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
Lufthansa.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
easyJet.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
easyJet.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
RyanAir.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
RyanAir.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
SingaporeAir.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
SingaporeAir.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
Qantas.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
Qantas.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
EtihadAirways.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
EtihadAirways.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
VirginAtlantic.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
VirginAtlantic.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')

klm_obj={'screen_name':'KLM','id':56377143}
aa_obj={'screen_name':'AmericanAir','id':22536055}
afr_obj={'screen_name':'airfrance','id':106062176}
bra_obj={'screen_name':'British_Airways','id':18332190}
ala_obj={'screen_name':'AlaskaAir','id':13192972}
luf_obj={'screen_name':'lufthansa','id':124476322}
ezj_obj={'screen_name':'easyJet','id':38676903}
rya_obj={'screen_name':'Ryanair','id':1542862735}
sin_obj={'screen_name':'SingaporeAir','id':253340062}
qua_obj={'screen_name':'Qantas','id':218730857}
eti_obj={'screen_name':'EtihadAirways','id':45621423}
vir_obj={'screen_name':'VirginAtlantic','id':20626359}
others=[aa_obj,afr_obj,bra_obj,ala_obj,luf_obj,ezj_obj,rya_obj,sin_obj,qua_obj,eti_obj,vir_obj]
colls=cavemen.list_collection_names()
colls.remove('tweets')

def reply_time_in_hours():
    
    reply_time_list_KLM = []
    reply_time_list_British_Airways = []
    reply_time_list_AirFrance = []
    reply_time_list_AmericanAir = []
    reply_time_list_Lufthansa = []
    reply_time_list_easyJet = []
    reply_time_list_RyanAir = []
    reply_time_list_SingaporeAir = []
    reply_time_list_Qantas = []
    reply_time_list_EtihadAirways = []
    reply_time_list_VirginAtlantic = []
    for reply_time in KLM.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_KLM.append(time)
        
    for reply_time in British_Airways.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_British_Airways.append(time)

    for reply_time in AirFrance.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_AirFrance.append(time)

    for reply_time in AmericanAir.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_AmericanAir.append(time)

    for reply_time in Lufthansa.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_Lufthansa.append(time)

    for reply_time in easyJet.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_easyJet.append(time)

    for reply_time in RyanAir.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_RyanAir.append(time)

    for reply_time in SingaporeAir.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_SingaporeAir.append(time)

    for reply_time in Qantas.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_Qantas.append(time)

    for reply_time in EtihadAirways.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_EtihadAirways.append(time)

    for reply_time in VirginAtlantic.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_VirginAtlantic.append(time)         

    fig, axes = plt.subplots(4, 3, sharex = True)
    fig.suptitle('Airlines reply to users in hours', size = 17, weight ='bold')
    fig.supylabel('Tweets', size = 15, weight ='bold')
    fig.supxlabel('Hours', size = 15, weight ='bold')
    fig.tight_layout() 
    axes[0,0].hist(reply_time_list_KLM, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[0,0].set_title('KLM', size = 15)
    axes[0,1].hist(reply_time_list_British_Airways, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[0,1].set_title('British_Airways', size = 15)
    axes[0,2].hist(reply_time_list_AirFrance, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[0,2].set_title('AirFrance', size = 15)
    axes[1,0].hist(reply_time_list_AmericanAir, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[1,0].set_title('AmericanAir', size = 15)
    axes[1,1].hist(reply_time_list_Lufthansa, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[1,1].set_title('Lufthansa', size = 15)
    axes[1,2].hist(reply_time_list_easyJet, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[1,2].set_title('easyJet', size = 15)
    axes[2,0].hist(reply_time_list_RyanAir, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[2,0].set_title('RyanAir', size = 15)
    axes[2,1].hist(reply_time_list_SingaporeAir, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[2,1].set_title('SingaporeAir', size = 15)
    axes[2,2].hist(reply_time_list_Qantas, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[2,2].set_title('Qantas', size = 15)
    axes[3,0].hist(reply_time_list_EtihadAirways, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[3,0].set_title('EtihadAirways', size = 15)
    axes[3,1].hist(reply_time_list_VirginAtlantic, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[3,1].set_title('VirginAtlantic', size = 15)
    plt.xticks([0,2,4,6,8,10,12,14,16,18,20,22,24])
    plt.show()

def Relation_between_sentiment_and_reply_time():
    
    reply_sentiment_list_KLM_4 = []
    reply_sentiment_list_KLM_8 = []
    reply_sentiment_list_KLM_12 = []
    reply_sentiment_list_KLM_16 = []
    reply_sentiment_list_KLM_20 = []
    reply_sentiment_list_KLM_24 = []
    reply_sentiment_list_KLM_greater = []

    reply_sentiment_list_British_Airways_4 = []
    reply_sentiment_list_British_Airways_8 = []
    reply_sentiment_list_British_Airways_12 = []
    reply_sentiment_list_British_Airways_16 = []
    reply_sentiment_list_British_Airways_20 = []
    reply_sentiment_list_British_Airways_24 = []
    reply_sentiment_list_British_Airways_greater = []

    reply_sentiment_list_AirFrance_4 = []
    reply_sentiment_list_AirFrance_8 = []
    reply_sentiment_list_AirFrance_12 = []
    reply_sentiment_list_AirFrance_16 = []
    reply_sentiment_list_AirFrance_20 = []
    reply_sentiment_list_AirFrance_24 = []
    reply_sentiment_list_AirFrance_greater = []

    reply_sentiment_list_AmericanAir_4 = []
    reply_sentiment_list_AmericanAir_8 = []
    reply_sentiment_list_AmericanAir_12 = []
    reply_sentiment_list_AmericanAir_16 = []
    reply_sentiment_list_AmericanAir_20 = []
    reply_sentiment_list_AmericanAir_24 = []
    reply_sentiment_list_AmericanAir_greater = []

    reply_sentiment_list_Lufthansa_4 = []
    reply_sentiment_list_Lufthansa_8 = []
    reply_sentiment_list_Lufthansa_12 = []
    reply_sentiment_list_Lufthansa_16 = []
    reply_sentiment_list_Lufthansa_20 = []
    reply_sentiment_list_Lufthansa_24 = []
    reply_sentiment_list_Lufthansa_greater = []

    reply_sentiment_list_easyJet_4 = []
    reply_sentiment_list_easyJet_8 = []
    reply_sentiment_list_easyJet_12 = []
    reply_sentiment_list_easyJet_16 = []
    reply_sentiment_list_easyJet_20 = []
    reply_sentiment_list_easyJet_24 = []
    reply_sentiment_list_easyJet_greater = []

    reply_sentiment_list_RyanAir_4 = []
    reply_sentiment_list_RyanAir_8 = []
    reply_sentiment_list_RyanAir_12 = []
    reply_sentiment_list_RyanAir_16 = []
    reply_sentiment_list_RyanAir_20 = []
    reply_sentiment_list_RyanAir_24 = []
    reply_sentiment_list_RyanAir_greater = []

    reply_sentiment_list_SingaporeAir_4 = []
    reply_sentiment_list_SingaporeAir_8 = []
    reply_sentiment_list_SingaporeAir_12 = []
    reply_sentiment_list_SingaporeAir_16 = []
    reply_sentiment_list_SingaporeAir_20 = []
    reply_sentiment_list_SingaporeAir_24 = []
    reply_sentiment_list_SingaporeAir_greater = []

    reply_sentiment_list_Qantas_4 = []
    reply_sentiment_list_Qantas_8 = []
    reply_sentiment_list_Qantas_12 = []
    reply_sentiment_list_Qantas_16 = []
    reply_sentiment_list_Qantas_20 = []
    reply_sentiment_list_Qantas_24 = []
    reply_sentiment_list_Qantas_greater = []

    reply_sentiment_list_EtihadAirways_4 = []
    reply_sentiment_list_EtihadAirways_8 = []
    reply_sentiment_list_EtihadAirways_12 = []
    reply_sentiment_list_EtihadAirways_16 = []
    reply_sentiment_list_EtihadAirways_20 = []
    reply_sentiment_list_EtihadAirways_24 = []
    reply_sentiment_list_EtihadAirways_greater = []

    reply_sentiment_list_VirginAtlantic_4 = []
    reply_sentiment_list_VirginAtlantic_8 = []
    reply_sentiment_list_VirginAtlantic_12 = []
    reply_sentiment_list_VirginAtlantic_16 = []
    reply_sentiment_list_VirginAtlantic_20 = []
    reply_sentiment_list_VirginAtlantic_24 = []
    reply_sentiment_list_VirginAtlantic_greater = []

    for sentiment in KLM.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_KLM_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_KLM_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_KLM_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_KLM_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_KLM_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_KLM_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_KLM_greater.append(sentiment['depth_3']['sentiment'])
    KLM_positive = [
        sum(i for i in reply_sentiment_list_KLM_4 if i == 1)/len(reply_sentiment_list_KLM_4),
        sum(i for i in reply_sentiment_list_KLM_8 if i == 1)/len(reply_sentiment_list_KLM_8),
        sum(i for i in reply_sentiment_list_KLM_12 if i == 1)/len(reply_sentiment_list_KLM_12),
        sum(i for i in reply_sentiment_list_KLM_16 if i == 1)/len(reply_sentiment_list_KLM_16),
        sum(i for i in reply_sentiment_list_KLM_20 if i == 1)/len(reply_sentiment_list_KLM_20),
        sum(i for i in reply_sentiment_list_KLM_24 if i == 1)/len(reply_sentiment_list_KLM_24),
        sum(i for i in reply_sentiment_list_KLM_greater if i == 1)/len(reply_sentiment_list_KLM_greater)
    ]
    

    for sentiment in British_Airways.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_British_Airways_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_British_Airways_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_British_Airways_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_British_Airways_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_British_Airways_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_British_Airways_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_British_Airways_greater.append(sentiment['depth_3']['sentiment'])
    
    British_Airways_positive = [
        sum(i for i in reply_sentiment_list_British_Airways_4 if i == 1)/len(reply_sentiment_list_British_Airways_4),
        sum(i for i in reply_sentiment_list_British_Airways_8 if i == 1)/len(reply_sentiment_list_British_Airways_8),
        sum(i for i in reply_sentiment_list_British_Airways_12 if i == 1)/len(reply_sentiment_list_British_Airways_12),
        sum(i for i in reply_sentiment_list_British_Airways_16 if i == 1)/len(reply_sentiment_list_British_Airways_16),
        sum(i for i in reply_sentiment_list_British_Airways_20 if i == 1)/len(reply_sentiment_list_British_Airways_20),
        sum(i for i in reply_sentiment_list_British_Airways_24 if i == 1)/len(reply_sentiment_list_British_Airways_24),
        sum(i for i in reply_sentiment_list_British_Airways_greater if i == 1)/len(reply_sentiment_list_British_Airways_greater)
    ]

    for sentiment in AirFrance.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_AirFrance_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_AirFrance_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_AirFrance_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_AirFrance_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_AirFrance_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_AirFrance_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_AirFrance_greater.append(sentiment['depth_3']['sentiment'])
    AirFrance_positive = [
        sum(i for i in reply_sentiment_list_AirFrance_4 if i == 1)/len(reply_sentiment_list_AirFrance_4),
        sum(i for i in reply_sentiment_list_AirFrance_8 if i == 1)/len(reply_sentiment_list_AirFrance_8),
        sum(i for i in reply_sentiment_list_AirFrance_12 if i == 1)/len(reply_sentiment_list_AirFrance_12),
        sum(i for i in reply_sentiment_list_AirFrance_16 if i == 1)/len(reply_sentiment_list_AirFrance_16),
        sum(i for i in reply_sentiment_list_AirFrance_20 if i == 1)/len(reply_sentiment_list_AirFrance_20),
        sum(i for i in reply_sentiment_list_AirFrance_24 if i == 1)/len(reply_sentiment_list_AirFrance_24),
        sum(i for i in reply_sentiment_list_AirFrance_greater if i == 1)/len(reply_sentiment_list_AirFrance_greater)
    ]

    for sentiment in AmericanAir.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_AmericanAir_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_AmericanAir_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_AmericanAir_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_AmericanAir_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_AmericanAir_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_AmericanAir_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_AmericanAir_greater.append(sentiment['depth_3']['sentiment'])
    AmericanAir_positive = [
        sum(i for i in reply_sentiment_list_AmericanAir_4 if i == 1)/len(reply_sentiment_list_AmericanAir_4),
        sum(i for i in reply_sentiment_list_AmericanAir_8 if i == 1)/len(reply_sentiment_list_AmericanAir_8),
        sum(i for i in reply_sentiment_list_AmericanAir_12 if i == 1)/len(reply_sentiment_list_AmericanAir_12),
        sum(i for i in reply_sentiment_list_AmericanAir_16 if i == 1)/len(reply_sentiment_list_AmericanAir_16),
        sum(i for i in reply_sentiment_list_AmericanAir_20 if i == 1)/len(reply_sentiment_list_AmericanAir_20),
        sum(i for i in reply_sentiment_list_AmericanAir_24 if i == 1)/len(reply_sentiment_list_AmericanAir_24),
        sum(i for i in reply_sentiment_list_AmericanAir_greater if i == 1)/len(reply_sentiment_list_AmericanAir_greater)
    ]

    for sentiment in Lufthansa.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_Lufthansa_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_Lufthansa_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_Lufthansa_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_Lufthansa_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_Lufthansa_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_Lufthansa_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_Lufthansa_greater.append(sentiment['depth_3']['sentiment'])
    Lufthansa_positive = [
        sum(i for i in reply_sentiment_list_Lufthansa_4 if i == 1)/len(reply_sentiment_list_Lufthansa_4),
        sum(i for i in reply_sentiment_list_Lufthansa_8 if i == 1)/len(reply_sentiment_list_Lufthansa_8),
        sum(i for i in reply_sentiment_list_Lufthansa_12 if i == 1)/len(reply_sentiment_list_Lufthansa_12),
        sum(i for i in reply_sentiment_list_Lufthansa_16 if i == 1)/len(reply_sentiment_list_Lufthansa_16),
        sum(i for i in reply_sentiment_list_Lufthansa_20 if i == 1)/len(reply_sentiment_list_Lufthansa_20),
        sum(i for i in reply_sentiment_list_Lufthansa_24 if i == 1)/len(reply_sentiment_list_Lufthansa_24),
        sum(i for i in reply_sentiment_list_Lufthansa_greater if i == 1)/len(reply_sentiment_list_Lufthansa_greater)
    ]

    for sentiment in easyJet.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_easyJet_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_easyJet_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_easyJet_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_easyJet_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_easyJet_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_easyJet_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_easyJet_greater.append(sentiment['depth_3']['sentiment'])
    easyJet_positive = [
        sum(i for i in reply_sentiment_list_easyJet_4 if i == 1)/len(reply_sentiment_list_easyJet_4),
        sum(i for i in reply_sentiment_list_easyJet_8 if i == 1)/len(reply_sentiment_list_easyJet_8),
        sum(i for i in reply_sentiment_list_easyJet_12 if i == 1)/len(reply_sentiment_list_easyJet_12),
        sum(i for i in reply_sentiment_list_easyJet_16 if i == 1)/len(reply_sentiment_list_easyJet_16),
        sum(i for i in reply_sentiment_list_easyJet_20 if i == 1)/len(reply_sentiment_list_easyJet_20),
        sum(i for i in reply_sentiment_list_easyJet_24 if i == 1)/len(reply_sentiment_list_easyJet_24),
        sum(i for i in reply_sentiment_list_easyJet_greater if i == 1)/len(reply_sentiment_list_easyJet_greater)
    ]

    for sentiment in RyanAir.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_RyanAir_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_RyanAir_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_RyanAir_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_RyanAir_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_RyanAir_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_RyanAir_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_RyanAir_greater.append(sentiment['depth_3']['sentiment'])
    RyanAir_positive = [
        sum(i for i in reply_sentiment_list_RyanAir_4 if i == 1)/len(reply_sentiment_list_RyanAir_4),
        sum(i for i in reply_sentiment_list_RyanAir_8 if i == 1)/len(reply_sentiment_list_RyanAir_8),
        sum(i for i in reply_sentiment_list_RyanAir_12 if i == 1)/len(reply_sentiment_list_RyanAir_12),
        sum(i for i in reply_sentiment_list_RyanAir_16 if i == 1)/len(reply_sentiment_list_RyanAir_16),
        sum(i for i in reply_sentiment_list_RyanAir_20 if i == 1)/len(reply_sentiment_list_RyanAir_20),
        sum(i for i in reply_sentiment_list_RyanAir_24 if i == 1)/len(reply_sentiment_list_RyanAir_24),
        sum(i for i in reply_sentiment_list_RyanAir_greater if i == 1)/len(reply_sentiment_list_RyanAir_greater)
    ]

    for sentiment in SingaporeAir.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_SingaporeAir_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_SingaporeAir_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_SingaporeAir_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_SingaporeAir_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_SingaporeAir_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_SingaporeAir_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_SingaporeAir_greater.append(sentiment['depth_3']['sentiment'])
    SingaporeAir_positive = [
        sum(i for i in reply_sentiment_list_SingaporeAir_4 if i == 1)/len(reply_sentiment_list_SingaporeAir_4),
        sum(i for i in reply_sentiment_list_SingaporeAir_8 if i == 1)/len(reply_sentiment_list_SingaporeAir_8),
        sum(i for i in reply_sentiment_list_SingaporeAir_12 if i == 1)/len(reply_sentiment_list_SingaporeAir_12),
        sum(i for i in reply_sentiment_list_SingaporeAir_16 if i == 1)/len(reply_sentiment_list_SingaporeAir_16),
        sum(i for i in reply_sentiment_list_SingaporeAir_20 if i == 1)/len(reply_sentiment_list_SingaporeAir_20),
        sum(i for i in reply_sentiment_list_SingaporeAir_24 if i == 1)/len(reply_sentiment_list_SingaporeAir_24),
        sum(i for i in reply_sentiment_list_SingaporeAir_greater if i == 1)/len(reply_sentiment_list_SingaporeAir_greater)
    ]

    for sentiment in Qantas.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_Qantas_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_Qantas_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_Qantas_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_Qantas_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_Qantas_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_Qantas_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_Qantas_greater.append(sentiment['depth_3']['sentiment'])
    Qantas_positive = [
        sum(i for i in reply_sentiment_list_Qantas_4 if i == 1)/len(reply_sentiment_list_Qantas_4),
        sum(i for i in reply_sentiment_list_Qantas_8 if i == 1)/len(reply_sentiment_list_Qantas_8),
        sum(i for i in reply_sentiment_list_Qantas_12 if i == 1)/len(reply_sentiment_list_Qantas_12),
        sum(i for i in reply_sentiment_list_Qantas_16 if i == 1)/len(reply_sentiment_list_Qantas_16),
        sum(i for i in reply_sentiment_list_Qantas_20 if i == 1)/len(reply_sentiment_list_Qantas_20),
        sum(i for i in reply_sentiment_list_Qantas_24 if i == 1)/len(reply_sentiment_list_Qantas_24),
        sum(i for i in reply_sentiment_list_Qantas_greater if i == 1)/len(reply_sentiment_list_Qantas_greater)
    ]

    for sentiment in EtihadAirways.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_EtihadAirways_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_EtihadAirways_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_EtihadAirways_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_EtihadAirways_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_EtihadAirways_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_EtihadAirways_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_EtihadAirways_greater.append(sentiment['depth_3']['sentiment'])
    EtihadAirways_positive = [
        sum(i for i in reply_sentiment_list_EtihadAirways_4 if i == 1)/len(reply_sentiment_list_EtihadAirways_4),
        sum(i for i in reply_sentiment_list_EtihadAirways_8 if i == 1)/len(reply_sentiment_list_EtihadAirways_8),
        sum(i for i in reply_sentiment_list_EtihadAirways_12 if i == 1)/(len(reply_sentiment_list_EtihadAirways_12)+1),
        sum(i for i in reply_sentiment_list_EtihadAirways_16 if i == 1)/(len(reply_sentiment_list_EtihadAirways_16)+1),
        sum(i for i in reply_sentiment_list_EtihadAirways_20 if i == 1)/(len(reply_sentiment_list_EtihadAirways_20)+1),
        sum(i for i in reply_sentiment_list_EtihadAirways_24 if i == 1)/(len(reply_sentiment_list_EtihadAirways_24)+1),
        sum(i for i in reply_sentiment_list_EtihadAirways_greater if i == 1)/(len(reply_sentiment_list_EtihadAirways_greater)+1)
    ]

    for sentiment in VirginAtlantic.find({'depth_3':{'$exists':True}}):
        time = (int(sentiment['timestamp_ms']) -int(sentiment['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 4:
            reply_sentiment_list_VirginAtlantic_4.append(sentiment['depth_3']['sentiment'])
        elif (time > 4) & (time <= 8):
            reply_sentiment_list_VirginAtlantic_8.append(sentiment['depth_3']['sentiment'])
        elif (time > 8) & (time <= 12):
            reply_sentiment_list_VirginAtlantic_12.append(sentiment['depth_3']['sentiment'])
        elif (time > 12) & (time <= 16):
            reply_sentiment_list_VirginAtlantic_16.append(sentiment['depth_3']['sentiment'])
        elif (time > 16) & (time <= 20):
            reply_sentiment_list_VirginAtlantic_20.append(sentiment['depth_3']['sentiment'])
        elif (time > 20) & (time <= 24):
            reply_sentiment_list_VirginAtlantic_24.append(sentiment['depth_3']['sentiment'])
        else:
            reply_sentiment_list_VirginAtlantic_greater.append(sentiment['depth_3']['sentiment'])
    VirginAtlantic_positive = [
        sum(i for i in reply_sentiment_list_VirginAtlantic_4 if i == 1)/len(reply_sentiment_list_VirginAtlantic_4),
        sum(i for i in reply_sentiment_list_VirginAtlantic_8 if i == 1)/len(reply_sentiment_list_VirginAtlantic_8),
        sum(i for i in reply_sentiment_list_VirginAtlantic_12 if i == 1)/len(reply_sentiment_list_VirginAtlantic_12),
        sum(i for i in reply_sentiment_list_VirginAtlantic_16 if i == 1)/len(reply_sentiment_list_VirginAtlantic_16),
        sum(i for i in reply_sentiment_list_VirginAtlantic_20 if i == 1)/len(reply_sentiment_list_VirginAtlantic_20),
        sum(i for i in reply_sentiment_list_VirginAtlantic_24 if i == 1)/len(reply_sentiment_list_VirginAtlantic_24),
        sum(i for i in reply_sentiment_list_VirginAtlantic_greater if i == 1)/len(reply_sentiment_list_VirginAtlantic_greater)
    ]       

    reply_time = ['4','8','12','16','20','24','24+']
    fig, axes = plt.subplots(4, 3, sharey = True, sharex = True)
    fig.suptitle('Relation between airlines replying time and getting positive sentiment', size=18, weight = 'bold')
    fig.supylabel('Positive sentiment', size=15, weight = 'bold')
    fig.supxlabel('Hours', size=15, weight = 'bold')
    fig.tight_layout() 
    axes[0,0].plot(reply_time,KLM_positive)
    axes[0,0].set_title('KLM', size=15)
    axes[0,1].plot(reply_time,British_Airways_positive)
    axes[0,1].set_title('British_Airways', size=15)
    axes[0,2].plot(reply_time, AirFrance_positive)
    axes[0,2].set_title('AirFrance', size=15)
    axes[1,0].plot(reply_time, AmericanAir_positive)
    axes[1,0].set_title('AmericanAir', size=15)
    axes[1,1].plot(reply_time, Lufthansa_positive)
    axes[1,1].set_title('Lufthansa', size=15)
    axes[1,2].plot(reply_time, easyJet_positive)
    axes[1,2].set_title('easyJet', size=15)
    axes[2,0].plot(reply_time, RyanAir_positive)
    axes[2,0].set_title('RyanAir', size=15)
    axes[2,1].plot(reply_time, SingaporeAir_positive)
    axes[2,1].set_title('SingaporeAir', size=15)
    axes[2,2].plot(reply_time, Qantas_positive)
    axes[2,2].set_title('Qantas', size=15)
    axes[3,0].plot(reply_time, EtihadAirways_positive)
    axes[3,0].set_title('EtihadAirways', size=15)
    axes[3,1].plot(reply_time, VirginAtlantic_positive)
    axes[3,1].set_title('VirginAtlantic', size=15)
    plt.show() 

def How_many_conversations_per_airline():

    total_tweets_dict = {'KLM':KLM.count_documents({}), 'British_Airways':British_Airways.count_documents({}), 'AirFrance':AirFrance.count_documents({}), 'AmericanAir':AmericanAir.count_documents({}), 'Lufthansa':Lufthansa.count_documents({}), 'easyJet':easyJet.count_documents({}), 'RyanAir':RyanAir.count_documents({}), 'SingaporeAir':SingaporeAir.count_documents({}), 'Qantas':Qantas.count_documents({}), 'EtihadAirways':EtihadAirways.count_documents({}), 'VirginAtlantic':VirginAtlantic.count_documents({})}
    total_tweets_dict = dict(sorted(total_tweets_dict.items(), key=lambda x:x[1]))
    fig, ax = plt.subplots()
    plot = ax.bar(*zip(*total_tweets_dict.items()), color = ['orange','orange','orange','orange','orange','orange','blue','orange','orange','orange','orange'])
    for plot in ax.containers:
        ax.bar_label(plot)
    plt.title('Conversations per airline', size = 17, weight = 'bold')
    plt.ylabel('Coversations', size = 15, weight = 'bold')
    plt.xlabel('Airlines', size = 15, weight = 'bold')
    plt.xticks(size = 12, rotation=15)
    plt.show()

def sentiment_analysis_for_each_airline():
    Airlines = ['KLM','British_Airways', 'AirFrance','AmericanAir','Lufthansa', 'easyJet','RyanAir','SingaporeAir','Qantas','EtihadAirways','VirginAtlantic']
    KLM_depth_1_sentiment_1 = KLM.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    KLM_depth_1_sentiment_0 = KLM.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    KLM_depth_1_sentiment_n1 = KLM.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    KLM_depth_3_sentiment_1 = KLM.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    KLM_depth_3_sentiment_0 = KLM.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    KLM_depth_3_sentiment_n1 = KLM.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    British_Airways_depth_1_sentiment_1 = British_Airways.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    British_Airways_depth_1_sentiment_0 = British_Airways.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    British_Airways_depth_1_sentiment_n1 = British_Airways.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    British_Airways_depth_3_sentiment_1 = British_Airways.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    British_Airways_depth_3_sentiment_0 = British_Airways.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    British_Airways_depth_3_sentiment_n1 = British_Airways.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    AirFrance_depth_1_sentiment_1 = AirFrance.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    AirFrance_depth_1_sentiment_0 = AirFrance.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    AirFrance_depth_1_sentiment_n1 = AirFrance.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    AirFrance_depth_3_sentiment_1 = AirFrance.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    AirFrance_depth_3_sentiment_0 = AirFrance.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    AirFrance_depth_3_sentiment_n1 = AirFrance.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    AmericanAir_depth_1_sentiment_1 = AmericanAir.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    AmericanAir_depth_1_sentiment_0 = AmericanAir.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    AmericanAir_depth_1_sentiment_n1 = AmericanAir.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    AmericanAir_depth_3_sentiment_1 = AmericanAir.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    AmericanAir_depth_3_sentiment_0 = AmericanAir.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    AmericanAir_depth_3_sentiment_n1 = AmericanAir.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    Lufthansa_depth_1_sentiment_1 = Lufthansa.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    Lufthansa_depth_1_sentiment_0 = Lufthansa.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    Lufthansa_depth_1_sentiment_n1 = Lufthansa.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    Lufthansa_depth_3_sentiment_1 = Lufthansa.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    Lufthansa_depth_3_sentiment_0 = Lufthansa.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    Lufthansa_depth_3_sentiment_n1 = Lufthansa.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    easyJet_depth_1_sentiment_1 = easyJet.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    easyJet_depth_1_sentiment_0 = easyJet.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    easyJet_depth_1_sentiment_n1 = easyJet.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    easyJet_depth_3_sentiment_1 = easyJet.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    easyJet_depth_3_sentiment_0 = easyJet.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    easyJet_depth_3_sentiment_n1 = easyJet.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    RyanAir_depth_1_sentiment_1 = RyanAir.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    RyanAir_depth_1_sentiment_0 = RyanAir.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    RyanAir_depth_1_sentiment_n1 = RyanAir.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    RyanAir_depth_3_sentiment_1 = RyanAir.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    RyanAir_depth_3_sentiment_0 = RyanAir.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    RyanAir_depth_3_sentiment_n1 = RyanAir.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    SingaporeAir_depth_1_sentiment_1 = SingaporeAir.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    SingaporeAir_depth_1_sentiment_0 = SingaporeAir.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    SingaporeAir_depth_1_sentiment_n1 = SingaporeAir.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    SingaporeAir_depth_3_sentiment_1 = SingaporeAir.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    SingaporeAir_depth_3_sentiment_0 = SingaporeAir.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    SingaporeAir_depth_3_sentiment_n1 = SingaporeAir.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    Qantas_depth_1_sentiment_1 = Qantas.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    Qantas_depth_1_sentiment_0 = Qantas.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    Qantas_depth_1_sentiment_n1 = Qantas.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    Qantas_depth_3_sentiment_1 = Qantas.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    Qantas_depth_3_sentiment_0 = Qantas.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    Qantas_depth_3_sentiment_n1 = Qantas.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    EtihadAirways_depth_1_sentiment_1 = EtihadAirways.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    EtihadAirways_depth_1_sentiment_0 = EtihadAirways.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    EtihadAirways_depth_1_sentiment_n1 = EtihadAirways.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    EtihadAirways_depth_3_sentiment_1 = EtihadAirways.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    EtihadAirways_depth_3_sentiment_0 = EtihadAirways.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    EtihadAirways_depth_3_sentiment_n1 = EtihadAirways.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})

    VirginAtlantic_depth_1_sentiment_1 = VirginAtlantic.count_documents({'depth_1.sentiment':1, 'depth_3':{'$exists':True}})
    VirginAtlantic_depth_1_sentiment_0 = VirginAtlantic.count_documents({'depth_1.sentiment':0, 'depth_3':{'$exists':True}})
    VirginAtlantic_depth_1_sentiment_n1 = VirginAtlantic.count_documents({'depth_1.sentiment':-1, 'depth_3':{'$exists':True}})
    VirginAtlantic_depth_3_sentiment_1 = VirginAtlantic.count_documents({'depth_3.sentiment':1, 'depth_3':{'$exists':True}})
    VirginAtlantic_depth_3_sentiment_0 = VirginAtlantic.count_documents({'depth_3.sentiment':0, 'depth_3':{'$exists':True}})
    VirginAtlantic_depth_3_sentiment_n1 = VirginAtlantic.count_documents({'depth_3.sentiment':-1, 'depth_3':{'$exists':True}})
   
    fig, axes = plt.subplots(3, 1)
    fig.suptitle('Sentiment analysis per airline')
    fig.supylabel('Tweets')
    fig.supxlabel('Airlines')
    fig.tight_layout()    
    X_axis = np.arange(len(Airlines))
    axes[0].bar(X_axis-0.2, [KLM_depth_1_sentiment_1,British_Airways_depth_1_sentiment_1,AirFrance_depth_1_sentiment_1,AmericanAir_depth_1_sentiment_1,Lufthansa_depth_1_sentiment_1,easyJet_depth_1_sentiment_1,RyanAir_depth_1_sentiment_1,SingaporeAir_depth_1_sentiment_1,Qantas_depth_1_sentiment_1,EtihadAirways_depth_1_sentiment_1,VirginAtlantic_depth_1_sentiment_1], 0.4, label = 'Before_reply')
    axes[0].bar(X_axis+0.2, [KLM_depth_3_sentiment_1,British_Airways_depth_3_sentiment_1,AirFrance_depth_3_sentiment_1,AmericanAir_depth_3_sentiment_1,Lufthansa_depth_3_sentiment_1,easyJet_depth_3_sentiment_1,RyanAir_depth_3_sentiment_1,SingaporeAir_depth_3_sentiment_1,Qantas_depth_3_sentiment_1,EtihadAirways_depth_3_sentiment_1,VirginAtlantic_depth_3_sentiment_1], 0.4, label = 'After_reply')
    axes[1].bar(X_axis-0.2, [KLM_depth_1_sentiment_0,British_Airways_depth_1_sentiment_0,AirFrance_depth_1_sentiment_0,AmericanAir_depth_1_sentiment_0,Lufthansa_depth_1_sentiment_0,easyJet_depth_1_sentiment_0,RyanAir_depth_1_sentiment_0,SingaporeAir_depth_1_sentiment_0,Qantas_depth_1_sentiment_0,EtihadAirways_depth_1_sentiment_0,VirginAtlantic_depth_1_sentiment_0], 0.4)
    axes[1].bar(X_axis+0.2, [KLM_depth_3_sentiment_0,British_Airways_depth_3_sentiment_0,AirFrance_depth_3_sentiment_0,AmericanAir_depth_3_sentiment_0,Lufthansa_depth_3_sentiment_0,easyJet_depth_3_sentiment_0,RyanAir_depth_3_sentiment_0,SingaporeAir_depth_3_sentiment_0,Qantas_depth_3_sentiment_0,EtihadAirways_depth_3_sentiment_0,VirginAtlantic_depth_3_sentiment_0], 0.4)
    axes[2].bar(X_axis-0.2, [KLM_depth_1_sentiment_n1,British_Airways_depth_1_sentiment_n1,AirFrance_depth_1_sentiment_n1,AmericanAir_depth_1_sentiment_n1,Lufthansa_depth_1_sentiment_n1,easyJet_depth_1_sentiment_n1,RyanAir_depth_1_sentiment_n1,SingaporeAir_depth_1_sentiment_n1,Qantas_depth_1_sentiment_n1,EtihadAirways_depth_1_sentiment_n1,VirginAtlantic_depth_1_sentiment_n1], 0.4)
    axes[2].bar(X_axis+0.2, [KLM_depth_3_sentiment_n1,British_Airways_depth_3_sentiment_n1,AirFrance_depth_3_sentiment_n1,AmericanAir_depth_3_sentiment_n1,Lufthansa_depth_3_sentiment_n1, easyJet_depth_3_sentiment_n1,RyanAir_depth_3_sentiment_n1,SingaporeAir_depth_3_sentiment_n1,Qantas_depth_3_sentiment_n1,EtihadAirways_depth_3_sentiment_n1,VirginAtlantic_depth_3_sentiment_n1], 0.4)
    axes[0].set_title('Positive')
    axes[1].set_title('Neutral')
    axes[2].set_title('Negative')
    fig.legend()
    axes[0].set_xticks(X_axis, Airlines)
    axes[1].set_xticks(X_axis, Airlines)
    axes[2].set_xticks(X_axis, Airlines)
    plt.show()

def reply_plot():
    tweets.create_index('entities.user_mentions')
    tags={};conversations={};percentage={}
    others_tags=0
    others_conversations=0
    for airline in colls:
        tags[airline]=0
    for airline in colls:
        conversations[airline]=0

    tags['KLM']=tweets.count_documents({'entities.user_mentions':{'$in': [klm_obj]}})
    tags['AmericanAir']=tweets.count_documents({'entities.user_mentions':{'$in': [aa_obj]}})
    tags['AirFrance']=tweets.count_documents({'entities.user_mentions':{'$in': [afr_obj]}})
    tags['British_Airways']=tweets.count_documents({'entities.user_mentions':{'$in': [bra_obj]}})
    tags['EtihadAirways']=tweets.count_documents({'entities.user_mentions':{'$in': [eti_obj]}})
    tags['Lufthansa']=tweets.count_documents({'entities.user_mentions':{'$in': [luf_obj]}})
    tags['Qantas']=tweets.count_documents({'entities.user_mentions':{'$in': [qua_obj]}})
    tags['RyanAir']=tweets.count_documents({'entities.user_mentions':{'$in': [rya_obj]}})
    tags['SingaporeAir']=tweets.count_documents({'entities.user_mentions':{'$in': [sin_obj]}})
    tags['VirginAtlantic']=tweets.count_documents({'entities.user_mentions':{'$in': [vir_obj]}})
    tags['easyJet']=tweets.count_documents({'entities.user_mentions':{'$in': [ezj_obj]}})

    conversations['KLM']=getattr(cavemen,'KLM').count_documents({})
    conversations['AmericanAir']=getattr(cavemen,'AmericanAir').count_documents({})
    conversations['AirFrance']=getattr(cavemen,'AirFrance').count_documents({})
    conversations['British_Airways']=getattr(cavemen,'British_Airways').count_documents({})
    conversations['EtihadAirways']=getattr(cavemen,'EtihadAirways').count_documents({})
    conversations['Lufthansa']=getattr(cavemen,'Lufthansa').count_documents({})
    conversations['Qantas']=getattr(cavemen,'Qantas').count_documents({})
    conversations['RyanAir']=getattr(cavemen,'RyanAir').count_documents({})
    conversations['SingaporeAir']=getattr(cavemen,'SingaporeAir').count_documents({})
    conversations['VirginAtlantic']=getattr(cavemen,'VirginAtlantic').count_documents({})
    conversations['easyJet']=getattr(cavemen,'easyJet').count_documents({})

    for airline in tags.keys():
        percentage[airline]=conversations[airline]/tags[airline]
        if(airline!='KLM'):
            others_tags+=tags[airline]
            others_conversations+=conversations[airline]
    
    others_percentage=others_conversations/others_tags

    print(percentage,others_percentage)

def sentiment_plot():
    overall_sentiment={}
    tab=[0,0,0]
    for airline in colls:
        sentiment_negative_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1})
        sentiment_negative_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':-1})
        sentiment_neutral_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':0})
        sentiment_neutral_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':0})
        sentiment_positive_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':1})
        sentiment_positive_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':1})

        overall_sentiment[airline]=[sentiment_negative_after+sentiment_negative_before,sentiment_neutral_after+sentiment_neutral_before,sentiment_positive_after+sentiment_positive_before]
        if airline!='KLM':
            tab[0]+=sentiment_negative_after+sentiment_negative_before
            tab[1]+=sentiment_neutral_after+sentiment_neutral_before
            tab[2]+=sentiment_positive_after+sentiment_positive_before
    #sentiment-1 -> 1
    improvement={}
    for airline in colls:
        improvement[airline]=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':1})/getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':{"$exists":True}})
    
    x=improvement.keys()
    y=improvement.values()
    df=pd.DataFrame(y,x)
    df.columns=['percentage of improved tweets']
    airlines=['EtihadAirways','RyanAir','AirFrance','KLM','AmericanAir','Lufthansa','SingaporeAir','British_Airways','easyJet','Qantas','VirginAtlantic']
    df_sorted=df.sort_values('percentage of improved tweets')
    fig, ax=plt.subplots()
    plot=ax.bar(list(df_sorted.index),height=list(df_sorted['percentage of improved tweets']),color=['orange','orange','orange','blue','orange','orange','orange','orange','orange','orange','orange'])
    plt.ylim(bottom=0.3)
    plt.ylabel('% '+'of conversations',size=15, weight='bold')
    plt.xlabel('Airlines',size=15, weight='bold')
    plt.xticks(ticks=np.arange(11),labels=airlines,rotation=18,size=12)
    plt.title('percentage of people with improved sentiment throught conversation',size=17, weight='bold')
    for plot in ax.containers:
        ax.bar_label(plot)
    plt.show()

def Mean_sentiment_per_airline():
    screen_names = ["KLM", "airfrance", "British_Airways", "AmericanAir", "lufthansa", 
    "easyJet","Ryanair","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]
    result = {}
    for name in screen_names:
        for_plot = tweets.aggregate([
            {"$match": {'is_a_reply':False, 'entities.user_mentions.screen_name':name}},
            {"$group":{"_id": "$lang","avgsent":{"$avg":"$sentiment"}}},
        ])
        for doc in for_plot:
            result[name] = doc["avgsent"]

    result_sorted = dict(sorted(result.items(), key=lambda item: item[1]))
    airlines = list(result_sorted.keys())
    means = list(result_sorted.values())

    fig, ax = plt.subplots()
    plot = ax.bar(airlines, means,color=['orange','orange','orange','orange','orange','orange','orange','blue','orange','orange','orange'])
    for plot in ax.containers:
        ax.bar_label(plot)
    plt.ylabel("Mean sentiment", size=15, weight='bold')
    plt.title("Mean sentiment per airline", size = 17, weight='bold')
    plt.xticks(size=12, rotation = 15)
    plt.xlabel("Airlines", size=15, weight='bold')
    plt.show()

# reply_time_in_hours()
# Relation_between_sentiment_and_reply_time()
# How_many_conversations_per_airline()
# sentiment_analysis_for_each_airline()
# reply_plot()
# sentiment_plot()
# Mean_sentiment_per_airline()