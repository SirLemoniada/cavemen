from numpy import mean
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt

##Language

# lang_dict = {}
# for language in tweet.distinct('lang'):
#     language_count = tweet.count_documents({"lang" : language})
#     lang_dict[language] = language_count

# sorted_lang_dict = dict(sorted(lang_dict.items(), key=lambda item: item[1],reverse=True))
# key = []
# value = []
# for x, y in sorted_lang_dict.items():
#     key.append(x)
#     value.append(y)
# first_four_key = key[0:4]
# first_four_value = value[0:4]
# first_four_value.append(sum(value[5:]))
# first_four_key.append('others')

# plt.pie(first_four_value, labels=first_four_key, autopct='%1.1f%%', colors = ['tab:orange', 'tab:cyan', 'tab:green', 'tab:purple', 'tab:gray'])
# plt.title("Tweets per language")
# plt.show()





## Airline tweets count

# airline_dict = {}
# for airline in tweet.distinct('user.id'):
#     if airline == 56377143:
#         airline_count = tweet.count_documents({"user.id" : airline})
#         airline_dict['KLM'] = airline_count
#     elif airline == 106062176:
#         airline_count = tweet.count_documents({"user.id" : airline})
#         airline_dict['Air France'] = airline_count
#     elif airline == 18332190:
#         airline_count = tweet.count_documents({"user.id" : airline})
#         airline_dict['British Airways'] = airline_count
#     elif airline == 22536055:
#         airline_count = tweet.count_documents({"user.id" : airline})
#         airline_dict['American Airlines'] = airline_count
# sorted_retweet_airline_dict = dict(sorted(airline_dict.items(), key=lambda item: item[1],reverse=True))

# plt.bar(*zip(*sorted_retweet_airline_dict.items()))
# plt.title("Number of tweets send by each airline")
# plt.xlabel("Airlines")
# plt.ylabel("Number of tweets")
# plt.show()





## Followers count

# KLM_followers = []
# Air_France_followers = []
# British_Airways_followers = []
# American_Airlines_followers = []
# for date in tweet.find({"user.followers_count": {'$exists':True}}):
#     if date['user']['id'] == 56377143:
#         KLM_followers.append(date['user']['followers_count'])
#     elif date['user']['id'] == 106062176:
#         Air_France_followers.append(date['user']['followers_count'])
#     elif date['user']['id'] == 18332190:
#         British_Airways_followers.append(date['user']['followers_count'])     
#     elif date['user']['id'] == 22536055:
#         American_Airlines_followers.append(date['user']['followers_count'])   
# like_dict = {'KLM':mean(KLM_followers), 'Air France':mean(Air_France_followers), 'British Airways':mean(British_Airways_followers), 'American Airlines':mean(American_Airlines_followers)}
# sorted_like_dict = dict(sorted(like_dict.items(), key=lambda item: item[1],reverse=True))

# plt.bar(*zip(*sorted_like_dict.items()))
# plt.title("Number of followers by each airline")
# plt.xlabel("Airline")
# plt.ylabel("Number of followers")
# plt.show()




## Tweets send by each airline per day in June

# KLM_day_list_tmp=[]
# British_Airways_day_list_tmp=[]
# American_Airlines_day_list_tmp=[]
# KLM_day_list = []
# British_Airways_day_list=[]
# American_Airlines_day_list=[]
# Days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
# Days_int = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

# for date in tweet.find({"created_at": {"$exists" : True}}):
#     if date['created_at'].split()[1] == 'Jun':
#         if date['user']['id'] == 56377143:
#             splited_string = date['created_at'].split()
#             KLM_day_list_tmp.append(splited_string[2])
#         elif date['user']['id'] == 18332190:
#             splited_string = date['created_at'].split()
#             British_Airways_day_list_tmp.append(splited_string[2])
#         elif date['user']['id'] == 22536055:
#             splited_string = date['created_at'].split()
#             American_Airlines_day_list_tmp.append(splited_string[2])


# for day in Days:
#     KLM_day_list.append(KLM_day_list_tmp.count(day))
#     British_Airways_day_list.append(British_Airways_day_list_tmp.count(day))
#     American_Airlines_day_list.append(American_Airlines_day_list_tmp.count(day))

# plt.plot(Days_int, KLM_day_list, label = 'KLM')
# plt.plot(Days_int, British_Airways_day_list, label = 'British Airways')
# plt.plot(Days_int, American_Airlines_day_list, label = 'American Airlines', color = 'purple')
# plt.title("Tweets send by each airline per day in June")
# plt.legend()
# plt.xlabel("Day")
# plt.ylabel("Number of tweets")
# plt.show()



##I didn't use any of the codes below for the presentation



##Tweets send by each airline by month

# KLM_month_list_tmp=[]
# Air_France_month_list_tmp=[]
# British_Airways_month_list_tmp=[]
# American_Airlines_month_list_tmp=[]
# KLM_month_list = []
# Air_France_month_list=[]
# British_Airways_month_list=[]
# American_Airlines_month_list=[]
# months = ['May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']

# for date in tweet.find({"created_at": {"$exists" : True}}):
#     if date['user']['id'] == 56377143:
#         splited_string = date['created_at'].split()
#         KLM_month_list_tmp.append(splited_string[1])
#     elif date['user']['id'] == 106062176:
#         splited_string = date['created_at'].split()
#         Air_France_month_list_tmp.append(splited_string[1])
#     elif date['user']['id'] == 18332190:
#         splited_string = date['created_at'].split()
#         British_Airways_month_list_tmp.append(splited_string[1])
#     elif date['user']['id'] == 22536055:
#         splited_string = date['created_at'].split()
#         American_Airlines_month_list_tmp.append(splited_string[1])

# for month in months:
#     KLM_month_list.append(KLM_month_list_tmp.count(month))
#     Air_France_month_list.append(Air_France_month_list_tmp.count(month))
#     British_Airways_month_list.append(British_Airways_month_list_tmp.count(month))
#     American_Airlines_month_list.append(American_Airlines_month_list_tmp.count(month))

# plt.plot(months, KLM_month_list, label = 'KLM')
# plt.plot(months, Air_France_month_list, label = 'Air France')
# plt.plot(months, British_Airways_month_list, label = 'British Airways')
# plt.plot(months, American_Airlines_month_list, label = 'American Airlines', color = 'purple')
# plt.title("Tweets send by each airline by month")
# plt.legend()
# plt.xlabel("Month")
# plt.ylabel("Number of tweets")
# plt.show()






##Tweets send by KLM by month

# month_list=[]
# month_dict = {}
# for date in tweet.find({"created_at": {"$exists" : True}}):
#     if date['user']['id'] == 56377143:
#         splited_string = date['created_at'].split()
#         month_list.append(splited_string[1])

# for month in ['May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']:
#     month_dict[month] = month_list.count(month)

# plt.bar(*zip(*month_dict.items()))
# plt.title("Tweets send by KLM by month")
# plt.xlabel("Month")
# plt.ylabel("Number of tweets")
# plt.show()





##Tweets send from KLM by day

# day_list=[]
# day_dict = {}
# for date in tweet.find({"user.created_at": {"$exists" : True}}):
#     if date['user']['id'] == 56377143:
#         splited_string = date['user']['created_at'].split()
#         day_list.append(splited_string[0])

# for day in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
#     day_dict[day] = day_list.count(day)
# plt.bar(*zip(*day_dict.items()))
# plt.title("Tweets send from KLM by day")
# plt.xlabel("Day")
# plt.ylabel("Number of tweets")
# plt.show()




##Tweets send by KLM by year

month_list=[]
list_2019 = []
list_2020 = []
for date in tweet.find({"created_at": {"$exists" : True}}):
    if date['user']['id'] == 56377143:
        splited_string = date['created_at'].split()
        month_list.append(splited_string[1])

for month in ['May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
    list_2019.append(month_list.count(month))
for month in ['Jan','Feb','Mar']:
    list_2020.append(month_list.count(month))

plt.boxplot([list_2019, list_2020], labels=['2019', '2020'])
plt.title("Tweets send by KLM by year")
plt.xlabel("Year")
plt.ylabel("Number of tweets")
plt.show()