#!/usr/bin/env python3
""" Learning some pymongo """

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs.

    :param mongo_collection: PyMongo collection object.
    :param kwargs: Keyword arguments representing the document to be inserted.
    :return: The ObjectId of the inserted document.
    """
    return mongo_collection.insert_one(kwargs)

if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017/")
    db = client["your_database_name"]
    collection = db["your_collection_name"]

    inserted_id = insert_school(collection, name="Example School", topics=["Math", "Science"])

    print(f"Inserted document ObjectId: {inserted_id}")

    client.close()
