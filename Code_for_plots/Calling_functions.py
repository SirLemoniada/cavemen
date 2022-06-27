import Extra_1
import Extra_3
import Extra2
import twitter_use

months = [1,2,3,4,5,6,7,8,9,10,11,12] #insert the numbers of the months you want to display

Extra_1.plot_amount_reply(Extra_1.dataframe_for_plot(months))
Extra_3.sentiment_change_per_topic(Extra_3.occurance_of_topics(months))
Extra2.plot_words(Extra2.mean_success(months))
above_months = [5,6,7,8,9,10]
below_months = [11,12,1,2,3]
twitter_use.sentiment_evolution_plot(above_months,below_months)