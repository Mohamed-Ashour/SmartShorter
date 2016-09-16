from mongoframes import Frame

from pymongo import MongoClient

from src import app


@app.before_first_request
def initialize_db():
    URI = app.config['DATABASE_URI']
    Frame._client = MongoClient(URI)
