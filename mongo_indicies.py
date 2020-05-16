import os
import pymongo

mongo_uri = os.environ.get("MONGO_URI_WAITER_CALLER")
client = pymongo.MongoClient(mongo_uri)
db = client['waitercaller']

print (db.users.create_index("email", unique=True))
print (db.requests.create_index("table_id", unique=True))