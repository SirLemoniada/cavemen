from index import tweets,klm_conversations,cavemen
# import numpy as np

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
    klm_conversations.create_index('depth_1.sentiment')
    klm_conversations.create_index('depth_3.sentiment')

    klm_before_unhappy=klm_conversations.count_documents({'depth_1.sentiment':-1})
    print('done')
    klm_before_neutreal=klm_conversations.count_documents({'depth_1.sentiment':0})
    print('done')
    klm_before_happy=klm_conversations.count_documents({'depth_1.sentiment':1})
    print('done')
    klm_after_unhappy=klm_conversations.count_documents({'depth_3.sentiment':-1})
    print('done')
    klm_after_neutral=klm_conversations.count_documents({'depth_3.sentiment':0})
    print('done')
    klm_after_happy=klm_conversations.count_documents({'depth_3.sentiment':1})
    print('done')
    others_before_unhappy=0
    others_before_neutral=0
    others_before_happy=0
    others_after_unhappy=0
    others_after_neutral=0
    others_after_happy=0

    for airline in colls:
        airline=getattr(cavemen,airline)
        airline.create_index('depth_1.sentiment')
        airline.create_index('depth_3.sentiment')
        others_before_unhappy+=airline.count_documents({'depth_1.sentiment':-1})
        print('done')
        others_before_neutral+=airline.count_documents({'depth_1.sentiment':0})
        print('done')
        others_before_happy+=airline.count_documents({'depth_1.sentiment':1})
        print('done')
        others_after_unhappy+=airline.count_documents({'depth_3.sentiment':-1})
        print('done')
        others_after_neutral+=airline.count_documents({'depth_3.sentiment':0})
        print('done')
        others_after_happy+=airline.count_documents({'depth_3.sentiment':1})
    others=[others_before_unhappy,others_before_neutral,others_before_happy,others_after_unhappy,others_after_neutral,others_after_happy]
    klm=[klm_before_unhappy,klm_before_neutreal,klm_before_happy,klm_after_unhappy,klm_after_neutral,klm_after_happy]
    print(klm,others)

# def reply_times():
#     klm_times=np.array()
#     others_times=np.array()
#     klm=klm_conversations.find({'reply':{'$ne': None }})
#     print(klm[0])

# reply_times()
# sentiment_plot()
reply_plot()