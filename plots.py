import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
klm = index.klm_conversations
British_Airways = index.British_Airways_conversations
import matplotlib.pyplot as plt
import numpy as np 

for tweet_object in klm.find({}):
        tweet.update_one({}, {"$set" : {"timestap_ms" : int(tweet_object["timestamp_ms"])}})

def reply_time_in_hours():
    reply_time_list_KLM = []
    reply_time_list_British_Airways = []
    for reply_time in klm.find({'reply':{'$exists':True}}):
        reply_time_list_KLM.append((reply_time['reply']['timestamp_ms'] -reply_time['timestamp_ms'])/1000/60/60)
        
    for reply_time in British_Airways.find({'reply':{'$exists':True}}):
        reply_time_list_British_Airways.append((reply_time['reply']['timestamp_ms'] -reply_time['timestamp_ms'])/1000/60/60)

    plt.boxplot([reply_time_list_KLM,reply_time_list_British_Airways], labels = ['KLM','British_Airways'], showmeans=True)
    plt.title('Reply time in hours')
    plt.ylabel('Hours')
    # plt.ylim(0,3)
    plt.show()

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
    total_tweets_lst = [klm.count_documents({}), British_Airways.count_documents({})]
    airlines = ['KLM', 'British_Airways']
    plt.bar(airlines, total_tweets_lst, color = ['Blue', 'Darkorange'])
    plt.title('Total number of tweets in each airline collection')
    plt.ylabel('Number of tweets')
    plt.show()

def conversation_length():
    length = ['One', 'Two', 'Three']
    KLM_total = klm.count_documents({})
    KLM_depth_3 = klm.count_documents({'reply_to_reply':{'$exists':True}})
    KLM_depth_2 = (klm.count_documents({'reply':{'$exists':True}}) - KLM_depth_3)
    KLM_depth_1 = klm.count_documents({'reply':{'$exists':False}})
    KLM_length = [KLM_depth_1/KLM_total,KLM_depth_2/KLM_total,KLM_depth_3/KLM_total]
    
    BA_total = British_Airways.count_documents({})
    BA_depth_3 = British_Airways.count_documents({'reply_to_reply':{'$exists':True}})
    BA_depth_2 = (British_Airways.count_documents({'reply':{'$exists':True}}) - BA_depth_3)
    BA_depth_1 = British_Airways.count_documents({'reply':{'$exists':False}})
    BA_length = [BA_depth_1/BA_total,BA_depth_2/BA_total,BA_depth_3/BA_total]
    
    X_axis = np.arange(len(length))
    plt.bar(X_axis-0.2, KLM_length, 0.4, label = 'KLM')
    plt.bar(X_axis+0.2, BA_length, 0.4, label = 'British_Airways')
    plt.xticks(X_axis, length)
    plt.xlabel("Conversation length")
    plt.ylabel("Tweets proportion")
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
        KLM_depth_3.append(klm.count_documents({'reply_to_reply':{'sentmemt':sentiment}}))
        KLM_depth_1.append(klm.count_documents({'sentmemt':sentiment}))
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
        KLM_depth_3.append(klm.count_documents({'reply_to_reply':{'sentmemt':sentiment}}))
        KLM_depth_1.append(klm.count_documents({'reply_to_reply':{'$exists':True}, 'sentmemt':sentiment}))
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
reply_time_in_hours()