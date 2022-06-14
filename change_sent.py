import index #import index.py file
tweet = index.tweets #import tweets variable from index.py file and assign to tweet
klm = index.cavemen.KLM

print(klm.count_documents({"sentiment":-1, "depth_3.sentiment":1}))
print(klm.count_documents({}))
print(type(klm))
