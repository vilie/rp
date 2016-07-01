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
        toInsert.text = obj.body
    else:
        toInsert.text = obj.title
    posts.insert(toInsert)

# a = posts.find_one({"author": "Hellod"})
# print a
