from turtle import width
import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd

klm = index.cavemen.KLM
weeks1 = [*range(21,33)]
weeks3 = [*range(34,40)]
weeks4 = [*range(42,53)]
weeks5= [*range(1,13)]
weeks = weeks1 + weeks3 + weeks4 + weeks5

change_each_mon_klm_to_minus1 = []
change_each_mon_klm_to_zero = []
change_each_mon_klm_to_plus1 = []


for week in weeks:
    change_each_mon_klm_to_minus1.append(klm.count_documents({"depth_1.sentiment":-1, "depth_3.sentiment":-1,"$expr": { "$eq": [{ "$week": "$created_at" }, week] } })/klm.count_documents({"depth_1.sentiment":-1,"depth_3":{"$exists":True},"$expr": { "$eq": [{ "$week": "$created_at" }, week] }}))
    change_each_mon_klm_to_zero.append(klm.count_documents({"depth_1.sentiment":-1, "depth_3.sentiment":0,"$expr": { "$eq": [{ "$week": "$created_at" }, week] } })/klm.count_documents({"depth_1.sentiment":-1,"depth_3":{"$exists":True},"$expr": { "$eq": [{ "$week": "$created_at" }, week] }}))
    change_each_mon_klm_to_plus1.append(klm.count_documents({"depth_1.sentiment":-1, "depth_3.sentiment":1,"$expr": { "$eq": [{ "$week": "$created_at" }, week] } })/klm.count_documents({"depth_1.sentiment":-1,"depth_3":{"$exists":True},"$expr": { "$eq": [{ "$week": "$created_at" }, week] }}))
print(len(change_each_mon_klm_to_minus1), len(change_each_mon_klm_to_zero), len(change_each_mon_klm_to_plus1))

data={'week_number':weeks,'-1 to -1':change_each_mon_klm_to_minus1, "-1 to 0":change_each_mon_klm_to_zero, "-1 to 1":change_each_mon_klm_to_plus1}
df=pd.DataFrame(data)
df.set_index('week_number', inplace=True)
print(df)


df.plot(kind='bar',
                    stacked=True, 
                    colormap='coolwarm_r', 
                    figsize=(10, 6))

plt.legend(loc="upper left", ncol=2)
plt.xlabel("week of year")
plt.ylabel("Proportion")
plt.title("Change of sentiment throughout conversation over time")
plt.show()