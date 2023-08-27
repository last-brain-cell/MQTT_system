# Testing if the local DB works

import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client["naad's_db"]
collection = db["testing"]

collection.insert_one(\
    {"test_params": {
        "param0": "test",
        "param1": "test",
        "param2": "test",
        "param3": "test",
        "param4": "test",
        "param5": "test",
        "param6": "test",
        "param7": "test",
        "param8": "test",
        "param9": "test"
    }
})

print(db, collection)
