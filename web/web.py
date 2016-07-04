import json
import praw
import time
from db import database
from bson.json_util import dumps
from flask import Flask, request, jsonify

app = Flask(__name__)

print "Starting webserver"

@app.route("/posts/", methods=['GET', 'POST'])
def hello():
    params = {}
    params["subreddit"] = request.args.get('subreddit')
    params["from_time"] = request.args.get('from')
    params["to_time"] = request.args.get('to')

    if params["subreddit"] is None or params["from_time"] is None or params["to_time"] is None:
        return "{\"error\": Not all params set}"

    params["keyword"] = request.args.get('keyword')
    res = database.get(params)
    return "<pre>"+dumps(list(res), indent=2, separators=(',', ':'))+"</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
