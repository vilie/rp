import praw
import time

r = praw.Reddit('Comment parser example by u/_Daimon_')
multi_reddits = r.get_subreddit('gif+pics')

base = multi_reddits.get_comments(limit=1).next()

print "Base=", base.fullname

time.sleep(4)


while True:
    mrc = multi_reddits.get_comments(limit=40, params={"before": base.fullname})
    for com in mrc:
        print com.fullname, com
        if com.created_utc > base.created_utc:
            base = com
    time.sleep(1)
