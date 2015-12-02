from flask import Flask
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://infra01.server.com:27017")
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
            "date": datetime.now()
        }

    db.member.insert(data)

    return name;

@app.route('/list')
def list():
    print( db.member.find().count() )
    return "list"

if __name__ == '__main__':
    port=8808
    is_debug = False
    app.run(debug=is_debug, host="0.0.0.0", port=port, threaded=True)
