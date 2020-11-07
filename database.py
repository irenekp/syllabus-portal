from flask import Flask
from flask_pymongo import pymongo
from app import app

conn_string = "mongodb+srv://scoopalot:scoopypassword@cluster0.5mijz.mongodb.net/SyllabusDb?retryWrites=true&w=majority"

client = pymongo.MongoClient(conn_string)
db = client.get_database('SyllabusDb')
user_collection = pymongo.collection.Collection(db, 'Resources')




