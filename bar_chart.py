
"""{"airfrance" :0.02108433734939759,
"KLM" :0.12872304005477575,
"British_Airways": 0.1633288401052699,
"AmericanAir": 0.14675498375899623,
"lufthansa": 0.14061184395172607,
"easyJet" :0.15779145185431565,
"Ryanair" :0.10893137394778142,
"SingaporeAir" :0.21460552725027018,
"Qantas" :0.14218579234972678,
"etihad": 0.311046511627907,
"VirginAtlantic" :0.3016922471467926}"""

import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {"airfrance" :0.02108433734939759,
"KLM" :0.12872304005477575,
"British_Airways": 0.1633288401052699,
"AmericanAir": 0.14675498375899623,
"lufthansa": 0.14061184395172607,
"easyJet" :0.15779145185431565,
"Ryanair" :0.10893137394778142,
"SingaporeAir" :0.21460552725027018,
"Qantas" :0.14218579234972678,
"etihad": 0.311046511627907,
"VirginAtlantic" :0.3016922471467926}

data_sorted = dict(sorted(data.items(), key=lambda item: item[1]))
airlines = list(data_sorted.keys())
means = list(data_sorted.values())
#fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(airlines, means, color ='maroon',
        width = 0.6)
 
plt.xlabel("Airlines")
plt.ylabel("Mean sentiment between -1 and 1")
plt.title("Mean sentiment per airline")
#plt.xticks(rotation = 25)
plt.show()