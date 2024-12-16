from pymongo import MongoClient

# MongoDB connection
URL = "mongodb://localhost:27017/"

# MongoDB Client Connection
client = MongoClient(URL)
db = client['Skydash']