from flask import Flask
from flask_pymongo import PyMongo
import database

app = Flask(__name__)

@app.route("/")
def default():
	return "Go to /test to add something to the database!"

@app.route("/test")
def test():
    database.db.Resources.insert_one({"name": "John"})
    return "Connected to the data base!"

if __name__ == '__main__':
    app.run(port=8000)


