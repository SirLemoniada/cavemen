import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
from pandas import DataFrame
import datetime
import pandas as pd
#index = pd.date_range(start='5/22/2019', end='3/30/2020')
# index2 = pd.date_range(start='5/22/2019', end='5/23/2019')
# print(type(index2))
print(tweet.find({"user.screen_name":"KLM"}).explain())