from cmath import log
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import pymongo

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
import matplotlib.pyplot as plt
import numpy as np 

def reply_time_in_hours():
    
    KLM.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
    KLM.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
    British_Airways.create_index([('timestamp_ms',pymongo.ASCENDING)],name='d1')
    British_Airways.create_index([('depth_1',pymongo.ASCENDING),('timestamp_ms',pymongo.ASCENDING)],name='d3')
    reply_time_list_KLM = []
    reply_time_list_British_Airways = []
    for reply_time in KLM.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_KLM.append(time)
        
    for reply_time in British_Airways.find({}):
        time = (int(reply_time['timestamp_ms']) -int(reply_time['depth_1']['timestamp_ms']))/1000/60/60
        if time <= 24:
            reply_time_list_British_Airways.append(time)

    fig, axes = plt.subplots(2, 2, sharey=True)
    fig.suptitle('Airlines reply to users in hours')
    fig.tight_layout() 
    axes[0,0].hist(reply_time_list_KLM, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[0,0].set_title('KLM')
    axes[0,0].set_ylabel('tweets')
    axes[0,1].hist(reply_time_list_British_Airways, bins = [0,2,4,6,8,10,12,14,16,18,20,22,24])
    axes[0,1].set_title('British_Airways')
    plt.show()

reply_time_in_hours()
def users_reply_to_init_airline():
    reply_to_KLM = []
    reply_to_British_Airways = []
    for init_tweets_from_KLM in tweet.find({'user.id':56377143, 'is_a_reply':False}):
        reply_to_KLM.append(tweet.count_documents({'in_reply_to_status_id':init_tweets_from_KLM['id']}))
    for init_tweets_from_British_Airways in tweet.find({'user.id':18332190, 'is_a_reply':False}):
        reply_to_British_Airways.append(tweet.count_documents({'in_reply_to_status_id':init_tweets_from_British_Airways['id']}))

    plt.boxplot([reply_to_KLM,reply_to_British_Airways], labels = ['KLM','British_Airways'], showmeans=True)
    plt.title('Number of tweets reply to each airline initial post')
    plt.ylabel('Tweets')
    plt.show()   

def total_tweets_in_each_collection():
    total_tweets_lst = [KLM.count_documents({}), British_Airways.count_documents({})]
    airlines = ['KLM', 'British_Airways']
    plt.bar(airlines, total_tweets_lst, color = ['Blue', 'Darkorange'])
    plt.title('Total number of tweets in each airline collection')
    plt.ylabel('Number of tweets')
    plt.show()

def conversation_length():
    length = ['Two', 'Three']
    KLM_total = KLM.count_documents({})
    KLM_depth_3 = KLM.count_documents({'depth_3':{'$exists':True}})
    KLM_depth_1 = (KLM.count_documents({'depth_1':{'$exists':True}}) - KLM_depth_3)
    KLM_length = [KLM_depth_1,KLM_depth_3]
    
    BA_total = British_Airways.count_documents({})
    BA_depth_3 = British_Airways.count_documents({'depth_3':{'$exists':True}})
    BA_depth_1 = (British_Airways.count_documents({'depth_1':{'$exists':True}}) - BA_depth_3)
    BA_length = [BA_depth_1,BA_depth_3]
    
    X_axis = np.arange(len(length))
    plt.bar(X_axis-0.2, KLM_length, 0.4, label = 'KLM')
    plt.bar(X_axis+0.2, BA_length, 0.4, label = 'British_Airways')
    plt.xticks(X_axis, length)
    plt.xlabel("Conversation length")
    plt.ylabel("Tweets")
    plt.title("Counting conversation length for each airline")
    plt.legend()
    plt.show()

def sentiment_analysis_for_each_airline_compare_with_depth():
    sentiments = ['positive','neutral','negative']
    KLM_depth_3 = []
    KLM_depth_1 = []
    BA_depth_3 = []
    BA_depth_1 = []
    for sentiment in sentiments:
        KLM_depth_3.append(KLM.count_documents({'reply_to_reply':{'sentmemt':sentiment}}))
        KLM_depth_1.append(KLM.count_documents({'sentmemt':sentiment}))
        BA_depth_3.append(British_Airways.count_documents({'reply_to_reply':{'sentmemt':sentiment}}))
        BA_depth_1.append(British_Airways.count_documents({'sentmemt':sentiment}))

    fig, axes = plt.subplots(2, 2)
    fig.suptitle('Sentiment analysis per depth')
    fig.legend(sentiments) 
    fig.tight_layout()   
    axes[0,0].pie(KLM_depth_1, autopct='%1.1f%%')
    axes[1,0].pie(KLM_depth_3, autopct='%1.1f%%')
    axes[0,1].pie(BA_depth_1, autopct='%1.1f%%')
    axes[1,1].pie(BA_depth_3, autopct='%1.1f%%')
    axes[0,0].set_ylabel('Depth one')
    axes[1,0].set_ylabel('Depth three')
    axes[0,0].set_title('KLM')
    axes[0,1].set_title('British_Airways')
    plt.show()

def conversation_sentiment_analysis_for_each_airline():
    depth = ['One', 'Three']
    sentiments = ['positive','neutral','negative']
    KLM_depth_3 = []
    KLM_depth_1 = []
    BA_depth_3 = []
    BA_depth_1 = []
    for sentiment in sentiments:
        KLM_depth_3.append(KLM.count_documents({'reply_to_reply':{'sentmemt':sentiment}}))
        KLM_depth_1.append(KLM.count_documents({'reply_to_reply':{'$exists':True}, 'sentmemt':sentiment}))
        BA_depth_3.append(British_Airways.count_documents({'reply_to_reply':{'sentmemt':sentiment}}))
        BA_depth_1.append(British_Airways.count_documents({'reply_to_reply':{'$exists':True},'sentmemt':sentiment}))
    fig, axes = plt.subplots(2, 1,sharex=True, sharey=True)
    fig.suptitle('Sentiment analysis per airline')
    fig.tight_layout()    
    X_axis = np.arange(len(sentiments))
    axes[0].bar(X_axis-0.2, KLM_depth_1, 0.4, label = 'Depth one')
    axes[0].bar(X_axis+0.2, KLM_depth_3, 0.4, label = 'Depth Three')
    axes[1].bar(X_axis-0.2, BA_depth_1, 0.4)
    axes[1].bar(X_axis+0.2, BA_depth_3, 0.4)
    axes[0].set_title('KLM')
    axes[1].set_title('British_Airways')
    fig.legend()
    plt.xticks(X_axis, sentiments)
    plt.ylabel('Sentiment count')
    plt.xlabel('Sentiment')
    plt.show()
