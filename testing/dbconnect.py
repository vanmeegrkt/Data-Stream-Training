from pymongo import MongoClient

def mongodb_connect(db, collection):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client[db]
        collection = db[collection]
        return client, db, collection
    except Exception as e:
        print(e)

if __name__ == "__main__":
    client, db, collection = mongodb_connect("training", "students")
    print("Connected to:", db.name, collection.name)
    client.close()