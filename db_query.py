import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client["naad's_db"]
collection = db["rfid_data"]

print(db, collection)