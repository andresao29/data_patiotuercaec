import pymongo
from dotenv import load_dotenv

import os
import certifi

ca = certifi.where()

load_dotenv()  # take environment variables from .env.

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@cluster0.w841zyn.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@cluster0.w841zyn.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.get_database('test3').get_collection('andres').insert_one(document={"marca": "opel", "modelo": "omega"})
