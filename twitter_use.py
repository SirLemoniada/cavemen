from matplotlib import collections
from index import tweets,klm_conversations,cavemen

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

def reply_plot():
    klm_tag_number=tweets.count_documents({'entities.user_mentions':{'$in': [klm_obj]}})
    others_tags_number=tweets.count_documents({'entities.user_mentions':{'$in': others}})
    klm_conversations_number=klm_conversations.count_documents({})

    colls=cavemen.list_collection_names()
    colls.remove('klm');colls.remove('tweets')
    others_conversations_number=0
    for airline in colls:
        airline=getattr(cavemen,airline)
        others_conversations_number+=airline.count_documents({})

    percentage_klm=klm_conversations_number/klm_tag_number
    percentage_others=others_conversations_number/others_tags_number
    