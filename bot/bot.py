import json
import praw
import time

from pprint import pprint

with open('config.json') as data_file:
    conf = json.load(data_file)

r = praw.Reddit(user_agent='Internet Explorer 3.14')

sleepTime = 5
postID = {}
print "Finding latest post in each sub"

for sub in conf["subreddits"]:
    postID[sub] = r.get_subreddit(sub).get_new(limit=1).next().fullname
    print sub, postID[sub]

while True:
    for subs in conf["subreddits"]:
        topics = r.get_subreddit(subs).get_new(limit=50, params={"before": postID[subs]})
        for topic_it in topics:
            print 'Sub', subs, 'Topic ', topic_it.id, topic_it.title[:15]
            for comments in praw.helpers.flatten_tree(topic_it.comments):
                print 'Sub', subs, 'Comment ', comments.id, str(comments)[:15]
    time.sleep(sleepTime)
