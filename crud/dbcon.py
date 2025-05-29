from pymongo import MongoClient

#Initialize MongoDB connection
client = MongoClient("mongodb+srv://viswa:viswa3925@cluster0.xdiuzsp.mongodb.net/")
db = client["datas"] #replace with your db name
col = db["users"] #this is your collection (not a function!)