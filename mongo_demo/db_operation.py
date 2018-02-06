from pymongo import MongoClient
import random

# connection db
client = MongoClient('localhost', 9090)

# print all databases
print('database_names:', client.database_names())

# select database    client['linkedin'] or client.linkedin
db = client['linkedin']

# print all key name
print('collection_names', db.collection_names())

# insert record
#result = db.col.insert({'name': 'vector'})
#print(result)

print(db.stutents.find().count())



# collection = db.linkedin
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# result = collection.insert(student)


for item in db.linkedins.find().pretty():
    print(item)






