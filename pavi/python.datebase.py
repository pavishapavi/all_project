from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db=client.py_imtask
col=db.post


data={"whatis your name":"my name is python"}
col.insert_one(data)
