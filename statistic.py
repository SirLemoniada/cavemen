import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet

def number_of_language(lang:str):
    """counts number of tweets with a certain language"""
    result = tweet.count_documents({"lang" : lang})
    return result

result = number_of_language("en") #fill in the abbreviation of the country (look at documentation of twitter api to see abbreviation)
print(result) #print result