from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.DJ

uc = db.User

# data = {"name": "c++", "age": 50, "email": "cpp@gmail.com"}
# uc.insert_one(data)

data={"name":"python","email":"python20@gamil.com",}
uc.insert_one(data)
