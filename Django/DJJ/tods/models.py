from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.tods

uc = db.post
data = {"name": "python", "email": "python20@gamil.com" }
uc.insert_one(data)

# Create your models here.
