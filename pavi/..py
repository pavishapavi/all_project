from pymongo import client
client = client("mongodb://localhost:27017")
db = client.goole
col = db.post



