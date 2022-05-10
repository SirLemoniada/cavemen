import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet

def number_of_language(lang:str):
    """counts number of tweets with a certain language"""
    result = tweet.count_documents({"lang" : lang})
    return result

result = number_of_language("en") #fill in the abbreviation of the country (look at documentation of twitter api to see abbreviation)
 #print result
screen_names = ["KLM", "AirFrance", "British_Airways", "AmericanAir", "Lufthansa", "AirBerlin", "AirBerlin assist", 
"easyJet"," RyanAir","SingaporeAir", "Qantas", "EtihadAirways", "VirginAtlantic"]

def percent_per_airline(tweet):
    num_of_tweets_of_airlines = tweet.count_documents({'user.screen_name':{"$in":screen_names}})
    airline_dict = {}   

    for airline in screen_names:
        airline_count = tweet.count_documents({'user.screen_name' : airline})
        airline_dict[airline] = (airline_count/num_of_tweets_of_airlines)*100
    return airline_dict
print(tweet.count_documents({"created_at": {"$exists": False}}))