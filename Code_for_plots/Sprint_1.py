import index 
tweet = index.tweets 
import matplotlib.pyplot as plt
from numpy import mean

def Number_of_tweets_per_language():
    lang_dict = {}
    for language in tweet.distinct('lang'):
        language_count = tweet.count_documents({"lang" : language})
        lang_dict[language] = language_count

    sorted_lang_dict = dict(sorted(lang_dict.items(), key=lambda item: item[1],reverse=True))
    key = []
    value = []
    for x, y in sorted_lang_dict.items():
        key.append(x)
        value.append(y)
    first_four_key = key[0:4]
    first_four_value = value[0:4]
    first_four_value.append(sum(value[5:]))
    first_four_key.append('others')

    plt.pie(first_four_value, labels=first_four_key, autopct='%1.1f%%', colors = ['tab:orange', 'tab:cyan', 'tab:green', 'tab:purple', 'tab:gray'])
    plt.title("Tweets per language")
    plt.show()

def Number_of_tweets_sent_by_each_airline():
    airline_dict = {}
    for airline in tweet.distinct('user.id'):
        if airline == 56377143:
            airline_count = tweet.count_documents({"user.id" : airline})
            airline_dict['KLM'] = airline_count
        elif airline == 106062176:
            airline_count = tweet.count_documents({"user.id" : airline})
            airline_dict['Air France'] = airline_count
        elif airline == 18332190:
            airline_count = tweet.count_documents({"user.id" : airline})
            airline_dict['British Airways'] = airline_count
        elif airline == 22536055:
            airline_count = tweet.count_documents({"user.id" : airline})
            airline_dict['American Airlines'] = airline_count
    sorted_retweet_airline_dict = dict(sorted(airline_dict.items(), key=lambda item: item[1],reverse=True))

    plt.bar(*zip(*sorted_retweet_airline_dict.items()))
    plt.title("Number of tweets sent by each airline")
    plt.xlabel("Airlines")
    plt.ylabel("Number of tweets")
    plt.show()

def Number_of_followers_for_each_airline():
    KLM_followers = []
    Air_France_followers = []
    British_Airways_followers = []
    American_Airlines_followers = []
    for date in tweet.find({"user.followers_count": {'$exists':True}}):
        if date['user']['id'] == 56377143:
            KLM_followers.append(date['user']['followers_count'])
        elif date['user']['id'] == 106062176:
            Air_France_followers.append(date['user']['followers_count'])
        elif date['user']['id'] == 18332190:
            British_Airways_followers.append(date['user']['followers_count'])     
        elif date['user']['id'] == 22536055:
            American_Airlines_followers.append(date['user']['followers_count'])   
    like_dict = {'KLM':mean(KLM_followers), 'Air France':mean(Air_France_followers), 'British Airways':mean(British_Airways_followers), 'American Airlines':mean(American_Airlines_followers)}
    sorted_like_dict = dict(sorted(like_dict.items(), key=lambda item: item[1],reverse=True))

    plt.bar(*zip(*sorted_like_dict.items()))
    plt.title("Number of followers by each airline")
    plt.xlabel("Airline")
    plt.ylabel("Number of followers")
    plt.show()

def Tweets_sent_by_each_airline_per_day_in_June():
    KLM_day_list_tmp=[]
    British_Airways_day_list_tmp=[]
    American_Airlines_day_list_tmp=[]
    KLM_day_list = []
    British_Airways_day_list=[]
    American_Airlines_day_list=[]
    Days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
    Days_int = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    for date in tweet.find({"created_at": {"$exists" : True}}):
        if date['created_at'].split()[1] == 'Jun':
            if date['user']['id'] == 56377143:
                splited_string = date['created_at'].split()
                KLM_day_list_tmp.append(splited_string[2])
            elif date['user']['id'] == 18332190:
                splited_string = date['created_at'].split()
                British_Airways_day_list_tmp.append(splited_string[2])
            elif date['user']['id'] == 22536055:
                splited_string = date['created_at'].split()
                American_Airlines_day_list_tmp.append(splited_string[2])

    for day in Days:
        KLM_day_list.append(KLM_day_list_tmp.count(day))
        British_Airways_day_list.append(British_Airways_day_list_tmp.count(day))
        American_Airlines_day_list.append(American_Airlines_day_list_tmp.count(day))

    plt.plot(Days_int, KLM_day_list, label = 'KLM')
    plt.plot(Days_int, British_Airways_day_list, label = 'British Airways')
    plt.plot(Days_int, American_Airlines_day_list, label = 'American Airlines', color = 'purple')
    plt.title("Tweets sent by each airline per day in June")
    plt.legend()
    plt.xlabel("Day")
    plt.ylabel("Number of tweets")
    plt.show()