import json
import pymongo
import praw

from pymongo import MongoClient

client = MongoClient()
db = client.reddit
posts = db.data
posts.create_index([("text", pymongo.TEXT),
                    ("subreddit", pymongo.ASCENDING),
                    ("created_utc", pymongo.DESCENDING)]);

print "Configuring database"

def save(obj):
    toInsert = {}
    toInsert["id"] = obj.id
    toInsert["created_utc"] = obj.created_utc
    toInsert["subreddit"] = str(obj.subreddit)
    if type(obj) is praw.objects.Submission:
        toInsert["text"] = obj.title
        print "Saving a thread"
    else:
        toInsert["text"] = obj.body
        print "Saving a comment"
    posts.insert_one(toInsert)

def get(obj):
    subreddit = obj["subreddit"]
    from_time = int(obj["from_time"])
    to_time = int(obj["to_time"])
    keyword = obj["keyword"]
    query =  {"subreddit": subreddit,
                       "created_utc": {"$gte": from_time, "$lte": to_time}};

    if not keyword is None:
        query["$text"] = {"$search": keyword}

    return posts.find(query)
