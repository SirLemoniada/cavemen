import pandas as pd
from pandas import DataFrame
from logging.handlers import RotatingFileHandler
import matplotlib.pyplot as plt
import numpy as np
import string
import matplotlib.patches as mpatches
from index import tweets,cavemen
from index import KLM_conversations
from index import AirFrance_conversations
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

#Extra 1

def Extra_1_dataframe_for_plot(time:list):
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


def Extra_1_plot_amount_reply(df):
    ax = df[['week_yr','count']].plot.bar(x = 'week_yr', y = 'count', color = '#6259D8')
    df['count2'].plot(ax=ax, color = '#E53F08')
    
    ax.set_ylim(0,1000)
    ax.legend(["Responded", "Directed to KLM"], prop={'size': 15})
    ax.set_xlabel("Week of the year (year-week)", size = 15, weight = 'bold')
    ax.set_ylabel("Amount of tweets", size = 15, weight = 'bold')
    ax.set_title("Amount of tweets with a negative sentiment directed to KLM, compared to responded", size = 18, weight = 'bold')
    plt.xticks(rotation = 90, size = 17)
    plt.yticks(size = 17)
    plt.tight_layout()
    plt.savefig("Plots_for_demo/Extra_1.png")
    plt.close()

#Extra 2

def Extra_2_mean_success(time:list):
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


def Extra_2_plot_words(performance:list):
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
    plt.tight_layout()
    plt.xlabel("Words used in airlines' respones", size=24, weight='bold')
    plt.savefig("Plots_for_demo/Extra_2.png")

#Extra 3

def Extra_3_occurance_of_words(time:list):
    dct = {}
    stopwords_lst = ["klm", "0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz",]

    for tweet in KLM_conversations.find({"depth_1.sentiment" : -1, "$expr": { "$in": [{ "$month": "$created_at" }, time]}}):
        for word in tweet["depth_1"]["text"].translate(str.maketrans('', '', string.punctuation)).lower().split():
            if word not in dct:
                dct[word] = 1
            else:
                dct[word] += 1

    sorted_dct = dict(sorted(dct.items(), key=lambda item: item[1]))
    [sorted_dct.pop(x) for x in stopwords_lst if x in sorted_dct.keys()]

    return sorted_dct

def Extra_3_occurance_of_topics(time:list):
    luggage = ["bag", "bags", "baggage", "luggage", "suitcase"]
    lost = ["lost", "missing"]
    service = ["service", "staff", "contact", "care", "support"]
    delay = ["delayed", "delay", "long", "waiting", "late", "stuck", "wait"]
    cancel = ["cancelled", "cancel"]
    ticket_booking = ["ticket", "tickets", "booking", "booked", "rebook"]
    money = ["refund", "pay", "money", "paid", "claim", "compensation"]
    airport = ["schiphol", "airport", "gate"]
    checkin = ["checkin", "boarding", "board"]
    connection = ["connection"]
    account = ["account"]
    plane = ["seats", "plane", "passenger"]
    message = ["reply", "message"]
    missed = ["missed"]
    corona = ["coronavirus"]

    topic = {"luggage":[0,0,0], "lost":[0,0,0], "service": [0,0,0], "delay":[0,0,0], "cancel":[0,0,0], "ticket_booking":[0,0,0], "money":[0,0,0], "airport":[0,0,0], "checkin":[0,0,0], "connection":[0,0,0], "account":[0,0,0], "plane":[0,0,0], "message":[0,0,0], "missed":[0,0,0], "corona":[0,0,0]}

    for tweet in KLM_conversations.find({"depth_1.sentiment" : -1, "depth_3" : {"$exists" : True}, "$expr": { "$in": [{ "$month": "$created_at" }, time]}}):
        for word in tweet["depth_1"]["text"].translate(str.maketrans('', '', string.punctuation)).lower().split():
            for key in topic:
                if word in eval(key):
                    topic[key][0] += 1
                    if tweet["depth_3"]["sentiment"] == 1:
                        topic[key][1] += 1
                    elif tweet["depth_3"]["sentiment"] == 0:
                        topic[key][2] += 1

    sorted_topic = dict(sorted(topic.items(), key=lambda item: item[1], reverse = True))
    
    return sorted_topic


def Extra_3_sentiment_change_per_topic(topic_occurance_dct):
    first5pairs = {k: topic_occurance_dct[k] for k in list(topic_occurance_dct)[:5]}
    
    c = []
    v = []

    for key, val in first5pairs.items():
        c.append(key)
        v.append(val)

    v = np.array(v)

    fig, ax = plt.subplots()
    plot = ax.bar(range(len(c)), v[:,1]*100//v[:,0], color = '#6259D8')
    plt.xticks(range(len(c)), c, size = 15)

    plt.title("Improvement of sentiment for frequently adressed topics", size = 17, weight = 'bold')
    plt.xlabel("Topic", size = 15, weight = 'bold')
    plt.ylabel("Percentage of succes (in %)", size = 15, weight = 'bold')
    plt.legend(["negative to positive", "negative to neutral"], prop={'size': 15})
    plt.yticks(size = 15)

    for plot in ax.containers:
        ax.bar_label(plot, size=15)
    plt.tight_layout()
    plt.savefig("Plots_for_demo/Extra_3.png")
    plt.close()


# Sentiment change

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
def Sentiment_change_reply_plot():
    tweets.create_index('entities.user_mentions')
    tags={};conversations={};percentage={}
    others_tags=0
    others_conversations=0
    for airline in colls:
        tags[airline]=0
    for airline in colls:
        conversations[airline]=0

    tags['KLM']=tweets.count_documents({'entities.user_mentions':{'$in': [klm_obj]}})
    tags['AmericanAir']=tweets.count_documents({'entities.user_mentions':{'$in': [aa_obj]}})
    tags['AirFrance']=tweets.count_documents({'entities.user_mentions':{'$in': [afr_obj]}})
    tags['British_Airways']=tweets.count_documents({'entities.user_mentions':{'$in': [bra_obj]}})
    tags['EtihadAirways']=tweets.count_documents({'entities.user_mentions':{'$in': [eti_obj]}})
    tags['Lufthansa']=tweets.count_documents({'entities.user_mentions':{'$in': [luf_obj]}})
    tags['Qantas']=tweets.count_documents({'entities.user_mentions':{'$in': [qua_obj]}})
    tags['RyanAir']=tweets.count_documents({'entities.user_mentions':{'$in': [rya_obj]}})
    tags['SingaporeAir']=tweets.count_documents({'entities.user_mentions':{'$in': [sin_obj]}})
    tags['VirginAtlantic']=tweets.count_documents({'entities.user_mentions':{'$in': [vir_obj]}})
    tags['easyJet']=tweets.count_documents({'entities.user_mentions':{'$in': [ezj_obj]}})

    conversations['KLM']=getattr(cavemen,'KLM').count_documents({})
    conversations['AmericanAir']=getattr(cavemen,'AmericanAir').count_documents({})
    conversations['AirFrance']=getattr(cavemen,'AirFrance').count_documents({})
    conversations['British_Airways']=getattr(cavemen,'British_Airways').count_documents({})
    conversations['EtihadAirways']=getattr(cavemen,'EtihadAirways').count_documents({})
    conversations['Lufthansa']=getattr(cavemen,'Lufthansa').count_documents({})
    conversations['Qantas']=getattr(cavemen,'Qantas').count_documents({})
    conversations['RyanAir']=getattr(cavemen,'RyanAir').count_documents({})
    conversations['SingaporeAir']=getattr(cavemen,'SingaporeAir').count_documents({})
    conversations['VirginAtlantic']=getattr(cavemen,'VirginAtlantic').count_documents({})
    conversations['easyJet']=getattr(cavemen,'easyJet').count_documents({})

    for airline in tags.keys():
        percentage[airline]=conversations[airline]/tags[airline]
        if(airline!='KLM'):
            others_tags+=tags[airline]
            others_conversations+=conversations[airline]
    
    others_percentage=others_conversations/others_tags

    print(percentage,others_percentage)


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
   
