import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

from index import tweets
from index import KLM_conversations


def dataframe_for_plot(time:list):
    mentions_per_week = tweets.aggregate([
        {"$match": {'is_a_reply':False, 'entities.user_mentions.id':56377143, 'sentiment':-1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}}},
    {"$group" : {"_id":{"year":{"$year":"$created_at"}, "week": {"$week":"$created_at"}}, "count": {"$sum":1}}},
    {"$sort":{"_id":1}}
    ])
    replies_per_week = KLM_conversations.aggregate([
        {"$match": {'depth_1.sentiment':-1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}}},
    {"$group" : {"_id":{"year":{"$year":"$created_at"}, "week": {"$week":"$created_at"}}, "count": {"$sum":1}}},
    {"$sort":{"_id":1}}
    ])

    list_cursor_mentions = list(mentions_per_week)
    df_mentions_reply = DataFrame(list_cursor_mentions)

    list_cursor_reply = list(replies_per_week)
    df_reply = DataFrame(list_cursor_reply)

    df_mentions_reply['year'] = [d.get('year') for d in df_mentions_reply._id]
    df_mentions_reply['week'] = [d.get('week') for d in df_mentions_reply._id]
    df_mentions_reply['week_yr'] = df_mentions_reply['year'].astype(str) + '-' + df_mentions_reply['week'].astype(str)
    df_mentions_reply['count2'] = df_reply['count']

    df_mentions_reply = df_mentions_reply.drop('_id', 1)
    df_mentions_reply = df_mentions_reply.drop('year', 1)
    df_mentions_reply = df_mentions_reply.drop('week', 1)

    return df_mentions_reply


def plot_amount_reply(df):
    ax = df[['week_yr','count']].plot.bar(x = 'week_yr', y = 'count', color = '#6259D8')
    df['count2'].plot(ax=ax, color = '#E53F08')
    
    ax.set_ylim(0,1000)
    ax.legend(["Responded", "Directed to KLM"], prop={'size': 15})
    ax.set_xlabel("Week of the year (year-week)", size = 15, weight = 'bold')
    ax.set_ylabel("Amount of tweets", size = 15, weight = 'bold')
    ax.set_title("Amount of tweets with a negative sentiment directed to KLM, compared to reponded", size = 17, weight = 'bold')
    plt.xticks(rotation = 90, size = 17)
    plt.yticks(size = 17)
    
    plt.savefig("Plots_for_demo/Extra_1.png")
    plt.close()