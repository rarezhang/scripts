"""
import all files in a directory into mongodb 
"""


from pymongo import MongoClient
import json

from os import listdir
from os.path import isfile, join

client = MongoClient('localhost', 27017)
db = client.asthma
collection = db.tweets


def insert_doc_mongo(doc):
    """
    insert a single document into mongodb 
    """
    try:
        doc = json.loads(doc)
        collection.insert_one(doc)
        #print("inserted: {}".format(doc['id']))
    except Exception as e:
        pass

        
### !!! modify directory path here !!!        
dir_path = 'test'

files = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f))]

for path in files:
    print(path)

    # N = 0

    # count = 1
    with open(path, 'r', encoding='utf-8', errors='ignore') as infile:
        # print("skipping lines..")
        # for _ in range(N):
            # next(infile)
        print("inserting..")    
        for line in infile:
            insert_doc_mongo(line)
            # print(count)
            # count += 1
        print('done!')    