import sqlite3
from  createDatabase import load_database

class GetDatabase:
    def __init__(self):
        load_database()
    
    def getUserAccount(self):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor