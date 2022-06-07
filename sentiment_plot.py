from index import tweets,cavemen
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

colls=cavemen.list_collection_names()
colls.remove('tweets')

def sentiment_plot():
    overall_sentiment={}
    tab=[0,0,0]
    for airline in colls:
        sentiment_negative_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1})
        sentiment_negative_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':-1})
        sentiment_neutral_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':0})
        sentiment_neutral_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':0})
        sentiment_positive_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':1})
        sentiment_positive_after=getattr(cavemen,airline).count_documents({'depth_3.sentiment':1})

        overall_sentiment[airline]=[sentiment_negative_after+sentiment_negative_before,sentiment_neutral_after+sentiment_neutral_before,sentiment_positive_after+sentiment_positive_before]
        if airline!='KLM':
            tab[0]+=sentiment_negative_after+sentiment_negative_before
            tab[1]+=sentiment_neutral_after+sentiment_neutral_before
            tab[2]+=sentiment_positive_after+sentiment_positive_before
    #sentiment-1 -> 1
    improvement={}
    for airline in colls:
        improvement[airline]=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':1})/getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':{"$exists":True}})
        
    x=improvement.keys()
    y=improvement.values()
    df=pd.DataFrame(y,x)
    df.columns=['percentage of improved tweets']
    airlines=['Etihad','Ryan','AirFr','KLM','AA','Luft','SinAir','BritAir','easyJet','Qantas','Virgin']
    df_sorted=df.sort_values('percentage of improved tweets')
    plt.figure(figsize=(10,7))
    plt.bar(list(df_sorted.index),height=list(df_sorted['percentage of improved tweets']),color=['blue','blue','blue','orange','blue','blue','blue','blue','blue','blue','blue'])
    plt.ylim(bottom=0.3)
    plt.xticks(ticks=np.arange(11),labels=airlines)
    plt.title('negative -> positive sentiment')
    plt.show()
    plt.savefig('improved')

sentiment_plot()