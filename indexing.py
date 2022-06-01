
import pymongo
import pandas as pd
import datetime
import pprint
from collections import OrderedDict
from pandas import DataFrame

import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt


pprint.pprint(tweet.find({"user.screen_name":"KLM"}).explain())