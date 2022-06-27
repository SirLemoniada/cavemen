
from logging.handlers import RotatingFileHandler
import matplotlib.pyplot as plt
from index import AirFrance_conversations
from index import KLM_conversations
from index import British_Airways_conversations
from index import AmericanAir_conversations
from index import Lufthansa_conversations
from index import easyJet_conversations
from index import RyanAir_conversations
from index import SingaporeAir_conversations
from index import Qantas_conversations
from index import EtihadAirways_conversations
from index import VirginAtlantic_conversations

airline_list = [AirFrance_conversations, KLM_conversations, British_Airways_conversations, AmericanAir_conversations, Lufthansa_conversations,
easyJet_conversations, RyanAir_conversations, SingaporeAir_conversations, Qantas_conversations, EtihadAirways_conversations,
 VirginAtlantic_conversations]

def mean_success(time:list):
    all_responses = 0
    all_responses_impr = 0
    for airline in airline_list:
        all_responses += airline.count_documents({"depth_1.sentiment":-1,"depth_3":{"$exists":True}, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    for airline in airline_list:
        all_responses_impr += airline.count_documents({ "depth_1.sentiment":-1,"depth_3.sentiment":1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    m = all_responses_impr/all_responses
    all_responses_great = 0
    all_responses_impr_great = 0
    for airline in airline_list:
        all_responses_great += airline.count_documents({"text": { "$regex": ".*great.*" },"depth_1.sentiment":-1,"depth_3":{"$exists":True}, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    for airline in airline_list:
        all_responses_impr_great += airline.count_documents({ "text": { "$regex": ".*great.*" },"depth_1.sentiment":-1,"depth_3.sentiment":1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    g = all_responses_impr_great/all_responses_great
    all_responses_hope = 0
    all_responses_impr_hope = 0
    for airline in airline_list:
        all_responses_hope += airline.count_documents({"text": { "$regex": ".*hope.*" },"depth_1.sentiment":-1,"depth_3":{"$exists":True}, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    for airline in airline_list:
        all_responses_impr_hope += airline.count_documents({ "text": { "$regex": ".*hope.*" },"depth_1.sentiment":-1,"depth_3.sentiment":1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    h = all_responses_impr_hope/all_responses_hope
    all_responses_hope = 0
    all_responses_impr_hope = 0
    for airline in airline_list:
        all_responses_hope += airline.count_documents({"text": { "$regex": ".*kindly.*" },"depth_1.sentiment":-1,"depth_3":{"$exists":True}, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    for airline in airline_list:
        all_responses_impr_hope += airline.count_documents({ "text": { "$regex": ".*kindly.*" },"depth_1.sentiment":-1,"depth_3.sentiment":1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    k = all_responses_impr_hope/all_responses_hope
    all_responses_hi = 0
    all_responses_impr_hi = 0
    for airline in airline_list:
        all_responses_hi += airline.count_documents({"text": { "$regex": ".*(Hi|Hello|Hey).*" },"depth_1.sentiment":-1,"depth_3":{"$exists":True}, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    for airline in airline_list:
        all_responses_impr_hi += airline.count_documents({ "text": { "$regex": ".*(Hi|Hello|Hey).*" },"depth_1.sentiment":-1,"depth_3.sentiment":1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}})
    hi = all_responses_impr_hi/all_responses_hi
    return [k,m,hi,h,g]


def plot_words(performance:list):
    words = ["'kindly'", 'all responses', "'Hi', 'Hey', Hello'", "'hope'","'great'"]
    rounded = []
    for i in performance:
        rounded.append(round(i, 2))

    fig, ax = plt.subplots()
    plot = ax.bar(words, rounded, color = ['#E53F08', '#FDB200', '#6259D8', '#6259D8' ,'#6259D8'])
    for plot in ax.containers:
        ax.bar_label(plot,size=24)
    plt.ylabel("Succes rate - neg. to pos. sentiment", size=24, weight='bold')
    plt.title("Succes rate in changing sentiment when using specific words", size = 24, weight='bold')
    plt.xticks(size=24, rotation = 10)
    plt.yticks(size=24)
    plt.xlabel("Words used in airlines' respones", size=24, weight='bold')
    #plt.savefig("Plots_for_demo/Extra2.png")
    plt.show()
plot_words(mean_success([1,2]))
