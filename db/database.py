import json
import pymongo
import praw

from pymongo import MongoClient

client = MongoClient()
db = client.reddit
posts = db.data

print "AAAAA"

def save(obj):
    toInsert = {}
    toInsert["created_utc"] = obj.created_utc
    toInsert["subreddit"] = str(obj.subreddit)
    if type(obj) is praw.objects.Submission:
        toInsert["text"] = obj.title
        print "Saving a thread"
    else:
        toInsert["text"] = obj.body
        print "Saving a comment"
    posts.insert_one(toInsert)

# a = posts.find_one({"author": "Hellod"})
# print a
