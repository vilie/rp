import pymongo
import json

from pymongo import MongoClient

client = MongoClient()
db = client.reddit

posts = db.data

post = {"author": "Hello",
        "text": "World"}

posts.insert_one(post)

a = posts.find_one()
print a
