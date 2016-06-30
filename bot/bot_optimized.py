import json
import praw
import time

with open('config.json') as data_file:
    conf = json.load(data_file)

r = praw.Reddit(user_agent='Internet Explorer 3.14')
reddits = r.get_subreddit("+".join(conf["subreddits"]))

base_com = reddits.get_comments(limit=1).next()
base_thr = reddits.get_new(limit=1).next()

print "Base com=", base_com.fullname, "Base thread=", base_thr.fullname

time.sleep(4)

while True:
    coms = reddits.get_comments(limit=42, params={"before": base_com.fullname})
    for com in coms:
        print "Com ", com.fullname, com
        if com.created_utc > base_com.created_utc:
            base_com = com
    thrs = reddits.get_new(limit=42, params={"before": base_thr.fullname})
    for thr in thrs:
        print "Thr", thr.fullname, thr
        if thr.created_utc > base_thr.created_utc:
            base_thr = thr
    time.sleep(1)
