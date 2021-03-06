from flask import Flask, json, jsonify, render_template, request
from bson import json_util
from datetime import datetime
from urlparse import urlparse, parse_qs

from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://t01.b.com:27017")
db = client.mydb
# db = client.test

@app.route('/')
def index():
    return "hello world!"

@app.route('/save/<name>')
def save(name):
    data = {
            "age":30,
            "name":name,
            "cdate": datetime.now()
        }

    db.member.insert(data)

    return name;

@app.route('/findAll')
def findAll():
    data = json_util.dumps( db.member.find() )
    # print( db.member.find().count() )

    # return render_template("user.html", users=data)
    return render_template("user.html", users=json.loads(data) )

@app.route('/find/<name>')
def findByName(name):
    data = json_util.dumps( db.member.find({
        'name': name }) )

    print(data)
    return render_template("user.html", users=json.loads(data) )


if __name__ == '__main__':
    port=8808
    is_debug = False
    app.run(debug=is_debug, host="0.0.0.0", port=port, threaded=True)
