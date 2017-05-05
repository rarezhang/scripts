"""
insert json document into mongodb 
scince mongo import stop working when first error occurs
suppport multiprocessing
"""

import pymongo, io, json
#from multiprocessing import Pool


#############################################################
# connect to mongodb: local host
#pool_size = 4 
client = pymongo.MongoClient('127.0.0.1', 27017, maxPoolSize=200)
db = client.pima
collection = db.tweets
print(collection)


def insert_doc_mongo(doc):
    """
    insert a single document into mongodb
    """
    try:
        doc = json.loads(doc)
        collection.insert_one(doc)
        print("inserted: {}".format(doc['id']))
    except Exception as e:
        #print(e)
        pass


#############################################################
file_path = '/disk01/pimadata/vector_2016_05_20'
N = 5138798


if __name__ == "__main__":
    
    #pool = Pool(pool_size)

    with io.open(file=file_path, mode='r', encoding='utf-8', errors='ignore') as source_file:
        print("skipping lines..")
        for _ in range(N):
            next(source_file)
        print("start inserting...")
        for line in source_file:
            insert_doc_mongo(line)
        #pool.imap(insert_doc_mongo, source_file, pool_size)  # use imap: iterable is large enough that converting it to a list would cause you to run out of/use too much memory.| be able to start processing the results before all of them are completed.
    
    #pool.close()



