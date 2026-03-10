from pymongo import MongoClient

uri = "mongodb+srv://krbhalani55_db_user:aCYt9fjJ0THVjPcw@cluster0.iq0en4f.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

db = client["adaptive_test"]

questions_collection = db["questions"]

sessions_collection = db["sessions"]