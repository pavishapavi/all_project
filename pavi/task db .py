


from pymongo import Mongoclient
client = Mongoclient("mongodb://localhost:27017")
db=client.task
col=db.post

