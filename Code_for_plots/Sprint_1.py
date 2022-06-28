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

    plt.bar(key,value)
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

def Tweets_sent_by_each_airline_per_week_in_June():
    KLM_week = {22:0, 23:0, 24:0, 25:0}
    British_Airways_week = {22:0, 23:0, 24:0, 25:0}
    American_Airlines_week = {22:0, 23:0, 24:0, 25:0}

    for week in range(22,26):
        for each_tweet in tweet.find({"$expr": { "$eq": [{ "$week": "$created_at" }, week]}, "user.id": {"$in" : [56377143,18332190,22536055]}}):
            if each_tweet['user']['id'] == 56377143:
                KLM_week[week] += 1
            elif each_tweet['user']['id'] == 18332190:
                British_Airways_week[week] += 1
            elif each_tweet['user']['id'] == 22536055:
                American_Airlines_week[week] += 1

    fig, axes = plt.subplots(3, 1, sharex = True)
    axes[0].bar(*zip(*KLM_week.items()))
    axes[0].set_title('KLM', size = 15)
    axes[1].bar(*zip(*British_Airways_week.items()))
    axes[1].set_title('British_Airways', size = 15)
    axes[2].bar(*zip(*American_Airlines_week.items()), label = 'American Airlines')
    axes[2].set_title('American Airlines', size = 15)
    fig.suptitle("Tweets sent by each airline per week in June")
    fig.supxlabel("Week")
    fig.supylabel("Number of tweets")
    plt.show()