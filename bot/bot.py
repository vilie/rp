import json
import praw

from pprint import pprint

with open('config.json') as data_file:
    conf = json.load(data_file)

r = praw.Reddit(user_agent='Internet Explorer 3.14')

for subs in conf["subreddits"]:
    print '\nSub ', subs
    topics = r.get_subreddit(subs).get_top(limit=3)
    for topic_it in topics:
        print '\nTopic ', topic_it.id, topic_it.title[:15]
        for comments in praw.helpers.flatten_tree(topic_it.comments):
            print comments.id, str(comments)[:15]

#submissions = r.get_subreddit('python').get_top(limit=10)

#for s in submissions:
#    print s
