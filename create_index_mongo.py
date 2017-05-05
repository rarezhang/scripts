"""
create indexes for pymongo data base
"""

import pymongo
# connect to mongodb: local host
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.pima
collection = db.tweets
print(collection)

index_fields = ['id_str', 'coordinates', 'created_at', 'user.location', 'user.id_str', 'retweeted_status.id_str', 'retweeted_status.user.id_str']


for index in index_fields:
    try:
        print('creating index for: {} ...'.format(index))
        collection.create_index(index)
    except :
        print('faild to creat index for {}'.format(index))
        continue
