import Sprint_4

months = [6,7] #insert the numbers of the months you want to display

Sprint_4.Extra_1_plot_amount_reply(Sprint_4.Extra_1_dataframe_for_plot(months))
print('Extra_1 done')
Sprint_4.Extra_2_plot_words(Sprint_4.Extra_2_mean_success(months))
print('Extra_2 done')
Sprint_4.Extra_3_sentiment_change_per_topic(Sprint_4.Extra_3_occurance_of_topics(months))
print('Extra_3 done')

above_months = [8]
below_months = [9]
Sprint_4.sentiment_evolution_plot(above_months,below_months)
print('Sentiment_change done')
