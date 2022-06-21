from index import tweets,cavemen
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches


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
    overall_sentiment={}
    tab=[0,0,0]
    conversations={}
    for airline in colls:
        sentiment_negative_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':{"$exists":True}})
        sentiment_negative_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':-1})
        sentiment_neutral_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':0,'depth_3.sentiment':{"$exists":True}})
        sentiment_neutral_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':0})
        sentiment_positive_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':1,'depth_3.sentiment':{"$exists":True}})
        sentiment_positive_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':1})
        conversations[airline]=getattr(cavemen,airline).count_documents({'depth_3.sentiment':{'$exists':True}})

        negative_before=100*sentiment_negative_before/conversations[airline]
        neutral_before=100*sentiment_neutral_before/conversations[airline]
        positive_before=100*sentiment_positive_before/conversations[airline]

        negative_after=100*sentiment_negative_after/conversations[airline]
        neutral_after=100*sentiment_neutral_after/conversations[airline]
        positive_after=100*sentiment_positive_after/conversations[airline]

        fig,ax=plt.subplots()
        ax.broken_barh([(0,negative_before),(negative_before,negative_before+neutral_before),(neutral_before+negative_before,negative_before+neutral_before+positive_before)],[3,1],facecolors=('#6259D8', '#E53F08', '#FDB200'))
        ax.broken_barh([(0,negative_after),(negative_after,negative_after+neutral_after),(neutral_after+negative_after,negative_after+neutral_after+positive_after)],[1,1],facecolors=('#6259D8', '#E53F08', '#FDB200'))

        ax.set_yticks([1.5,3.5])
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.set_xticklabels(['0%','25%','50%','75%','100%'])
        ax.set_yticklabels(['after','before'])
        ax.set_axisbelow(True)
        leg1 = mpatches.Patch(color='#6259D8', label='negative')
        leg2 = mpatches.Patch(color='#E53F08', label='neutral')
        leg3 = mpatches.Patch(color='#FDB200', label='positive')
        ax.set_title(airline)
        #before
        ax.text(negative_before/2-2,3.45,str(int(negative_before))+'%')
        ax.text((2*negative_before+neutral_before)/2-2,3.45,str(int(neutral_before))+'%')
        ax.text((negative_before*2+neutral_before*2+positive_before)/2-2,3.45,str(int(positive_before))+'%')
        #after
        ax.text(negative_after/2-2,1.45,str(int(negative_after))+'%')
        ax.text((2*negative_after+neutral_after)/2-2,1.45,str(int(neutral_after))+'%')
        ax.text((negative_after*2+neutral_after*2+positive_after)/2-2,1.45,str(int(positive_after))+'%')


        ax.legend(handles=[leg1, leg2, leg3], ncol=3)






        ax.set_ylim(0, 5)
        ax.set_xlim(0,100)
        plt.show()
        break

    
    #     overall_sentiment[airline]=[sentiment_negative_after+sentiment_negative_before,sentiment_neutral_after+sentiment_neutral_before,sentiment_positive_after+sentiment_positive_before]
    #     if airline!='KLM':
    #         tab[0]+=sentiment_negative_after+sentiment_negative_before
    #         tab[1]+=sentiment_neutral_after+sentiment_neutral_before
    #         tab[2]+=sentiment_positive_after+sentiment_positive_before
    # #sentiment-1 -> 1
    # improvement={}
    # for airline in colls:
    #     improvement[airline]=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':1})/getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':{"$exists":True}})
        
    # x=improvement.keys()
    # y=improvement.values()
    # df=pd.DataFrame(y,x)
    # df.columns=['percentage of improved tweets']
    # airlines=['Etihad','Ryan','AirFr','KLM','AA','Luft','SinAir','BritAir','easyJet','Qantas','Virgin']
    # df_sorted=df.sort_values('percentage of improved tweets')
    # plt.figure(figsize=(10,7))
    # plt.bar(list(df_sorted.index),height=list(df_sorted['percentage of improved tweets']),color=['blue','blue','blue','orange','blue','blue','blue','blue','blue','blue','blue'])
    # plt.ylim(bottom=0.3)
    # plt.xticks(ticks=np.arange(11),labels=airlines)
    # plt.title('negative -> positive sentiment')
    # plt.show()
    # plt.savefig('improved')

sentiment_plot()