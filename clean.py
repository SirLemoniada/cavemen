import index
tweet = index.tweets

def number_of_language(lang:str):
    """counts number of tweets with a certain language"""
    results = tweet.count_documents({"lang" : lang})
    return print(results)

#number_of_language("nl")

results = tweet.find({"truncated": True})

#for result in results:
#    print(result["id"])

#for result in results:
#    if result['truncated']:
#        print(result["extended_tweet"]["full_text"])

for result in results:
    tweet.update_one({"id" : result["id"]}, {"$set" : {"text" : result["extended_tweet"]["full_text"]}})
