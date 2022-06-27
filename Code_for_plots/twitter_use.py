from index import tweets,cavemen
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches


klm_obj={'screen_name':'KLM','id':56377143}

aa_obj={'screen_name':'AmericanAir','id':22536055}
afr_obj={'screen_name':'airfrance','id':106062176}
bra_obj={'screen_name':'British_Airways','id':18332190}
ala_obj={'screen_name':'AlaskaAir','id':13192972}
luf_obj={'screen_name':'lufthansa','id':124476322}
ezj_obj={'screen_name':'easyJet','id':38676903}
rya_obj={'screen_name':'Ryanair','id':1542862735}
sin_obj={'screen_name':'SingaporeAir','id':253340062}
qua_obj={'screen_name':'Qantas','id':218730857}
eti_obj={'screen_name':'EtihadAirways','id':45621423}
vir_obj={'screen_name':'VirginAtlantic','id':20626359}

others=[aa_obj,afr_obj,bra_obj,ala_obj,luf_obj,ezj_obj,rya_obj,sin_obj,qua_obj,eti_obj,vir_obj]
colls=cavemen.list_collection_names()
colls.remove('tweets')


def sentiment_evolution_plot(above_months:list,below_months:list):
    
    fig,ax=plt.subplots(4,3,sharex=True,sharey=True)
    i=0
    fig.suptitle("Compare negative sentiment improvement between first and last six months", fontsize=16, weight='bold')
    fig.supxlabel('Percentage')

    for airline in colls:
        d3_no_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':{"$exists":True}, "$expr": { "$in": [{ "$month": "$created_at" }, above_months]}})
        negative_d3_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':-1,"$expr": { "$in": [{ "$month": "$created_at" }, above_months]}})
        neutral_d3_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':0,"$expr": { "$in": [{ "$month": "$created_at" }, above_months]}})
        positive_d3_before=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':1,"$expr": { "$in": [{ "$month": "$created_at" }, above_months]}})

        d3_no_after=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':{"$exists":True}, "$expr": { "$in": [{ "$month": "$created_at" }, below_months]}})
        negative_d3_after=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':-1,"$expr": { "$in": [{ "$month": "$created_at" }, below_months]}})
        neutral_d3_after=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':0,"$expr": { "$in": [{ "$month": "$created_at" }, below_months]}})
        positive_d3_after=getattr(cavemen,airline).count_documents({'depth_1.sentiment':-1,'depth_3.sentiment':1,"$expr": { "$in": [{ "$month": "$created_at" }, below_months]}})

        negative_d3_before_perc=100*negative_d3_before/d3_no_before
        neutral_d3_before_perc=100*neutral_d3_before/d3_no_before
        positive_d3_before_perc=100*positive_d3_before/d3_no_before

        negative_d3_after_perc=100*negative_d3_after/d3_no_after
        neutral_d3_after_perc=100*neutral_d3_after/d3_no_after
        positive_d3_after_perc=100*positive_d3_after/d3_no_after

        ax[i%4,i//4].broken_barh([(0,negative_d3_before_perc),(negative_d3_before_perc,negative_d3_before_perc+neutral_d3_before_perc),(negative_d3_before_perc+neutral_d3_before_perc,negative_d3_before_perc+neutral_d3_before_perc+positive_d3_before_perc)],[3,1],facecolors=('#E53F08', '#FDB200','#6259D8'))
        ax[i%4,i//4].broken_barh([(0,negative_d3_after_perc),(negative_d3_after_perc,negative_d3_after_perc+neutral_d3_after_perc),(negative_d3_after_perc+neutral_d3_after_perc,negative_d3_after_perc+neutral_d3_after_perc+positive_d3_after_perc)],[1,1],facecolors=('#E53F08', '#FDB200','#6259D8'))

        ax[i%4,i//4].set_yticks([1.5,2.5,3.5])
        ax[i%4,i//4].set_yticklabels(['Nov. 2019 - Mar. 2020','change of neg. sent.','May - Oct. 2019'],weight="bold")
        ax[i%4,i//4].set_xticks([0, 25, 50, 75, 100])
        ax[i%4,i//4].set_xticklabels(['0%','25%','50%','75%','100%'])

        leg1 = mpatches.Patch(color='#E53F08', label='negative -> negative')
        leg2 = mpatches.Patch(color='#FDB200', label='negative -> neutral')
        leg3 = mpatches.Patch(color='#6259D8', label='negative -> positive')

        ax[i%4,i//4].set_title(airline,weight="bold")

        ax[i%4,i//4].text(negative_d3_before_perc/2-2,3.45,str(int(negative_d3_before_perc))+'%',weight="bold")
        ax[i%4,i//4].text((2*negative_d3_before_perc+neutral_d3_before_perc)/2-2,3.45,str(int(neutral_d3_before_perc))+'%',weight="bold")
        ax[i%4,i//4].text((negative_d3_before_perc*2+neutral_d3_before_perc*2+positive_d3_before_perc)/2-2,3.45,str(int(positive_d3_before_perc))+'%',weight="bold")

        ax[i%4,i//4].text(negative_d3_after_perc/2-2,1.45,str(int(negative_d3_after_perc))+'%',weight="bold")
        ax[i%4,i//4].text((2*negative_d3_after_perc+neutral_d3_after_perc)/2-2,1.45,str(int(neutral_d3_after_perc))+'%',weight="bold")
        ax[i%4,i//4].text((negative_d3_after_perc*2+neutral_d3_after_perc*2+positive_d3_after_perc)/2-2,1.45,str(int(positive_d3_after_perc))+'%',weight="bold")
        if(negative_d3_before_perc-negative_d3_after_perc>=0):
            ax[i%4,i//4].annotate(arrowprops={'arrowstyle': '->', 'lw': 2,'color':'green'},xy=(10,2.5),text=str(-(int(negative_d3_before_perc)-int(negative_d3_after_perc)))+'%',va='center',ha='center',xytext=(abs(negative_d3_before_perc-negative_d3_after_perc)+15,2.5))
        else:
            ax[i%4,i//4].annotate(arrowprops={'arrowstyle': '<-', 'lw': 2,'color':'red'},xy=(10,2.5),text='+'+str(-(int(negative_d3_before_perc)-int(negative_d3_after_perc)))+'%',va='center',ha='center',xytext=(abs(negative_d3_before_perc-negative_d3_after_perc)+15,2.5))

        ax[i%4,i//4].set_ylim(0, 5)
        ax[i%4,i//4].set_xlim(0,100)
        i+=1
    fig.legend(handles=[leg1,leg2,leg3],fontsize=13)
    plt.savefig("Plots_for_demo/Sentiment_change.png")
    plt.close()
