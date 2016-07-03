import json
import praw
import time
from db import database
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    subreddit = request.args.get('subreddit')
    from_time = request.args.get('from')
    to_time = request.args.get('to')
    keyword = request.args.get('keyword')
    return "Hello World! " + request.args.get('msg')

if __name__ == "__main__":
    app.run()
