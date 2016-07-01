import json
import praw
import time
from db import database
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World! " + request.args.get('msg')

if __name__ == "__main__":
    app.run()
