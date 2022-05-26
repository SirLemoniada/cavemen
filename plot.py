import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
klm = index.klm_conversations
British_Airways = index.British_Airways_conversations
import matplotlib.pyplot as plt

def reply_time_in_hours():
    reply_time_list_KLM = []
    reply_time_list_British_Airways = []
    for reply_time in klm.find({'reply':{'$exists':True}}):
        reply_time_list_KLM.append((int(reply_time['reply']['timestamp_ms']) - int(reply_time['timestamp_ms']))/1000/60/60)
        
    for reply_time in British_Airways.find({'reply':{'$exists':True}}):
        reply_time_list_British_Airways.append((int(reply_time['reply']['timestamp_ms']) - int(reply_time['timestamp_ms']))/1000/60/60)

    plt.boxplot([reply_time_list_KLM,reply_time_list_British_Airways], labels = ['KLM','British_Airways'], showmeans=True)
    plt.title('Reply time in hours')
    plt.ylabel('Hours')
    plt.ylim(0,3)
    plt.show()

def users_reply_to_airline_per_tweet():
    reply_to_KLM = []
    reply_to_British_Airways = []
    for init_tweets_from_KLM in tweet.find({'user.id':56377143, 'is_a_reply':False}):
        reply_to_KLM.append(tweet.count_documents({'in_reply_to_status_id':init_tweets_from_KLM['id']}))
    for init_tweets_from_British_Airways in tweet.find({'user.id':18332190, 'is_a_reply':False}):
        reply_to_British_Airways.append(tweet.count_documents({'in_reply_to_status_id':init_tweets_from_British_Airways['id']}))

    plt.boxplot([reply_to_KLM,reply_to_British_Airways], labels = ['KLM','British_Airways'], showmeans=True)
    plt.title('Number of users reply per tweet posted from different airlines')
    plt.ylabel('Users')
    plt.show()   
    
reply_time_in_hours()
