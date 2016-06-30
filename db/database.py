import json
import pymongo
import praw

from pymongo import MongoClient

client = MongoClient()
db = client.reddit

posts = db.data

def save(obj):
    toInsert.utc_time = obj.utc_time
    toInsert.subreddit = obj.subreddit
    if type(base_thr) is praw.objects.Submission:
        
    else
    posts.insert(obj)

post = {"author": "Mamare",
        "text": "mere"}

posts.insert(post)

a = posts.find_one({"author":"Mamare"})
print a

a = posts.find_one({"author": "Hellod"})

print a
