import sqlite3
from createDatabase import load_database

class Validation():
    def __init__(self):
        load_database()

    def validate_edit(self, attri, newVal, table):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM '+table)
            attributes = list(map(lambda x: x[0], cursor.description))
            if attri in attributes and len(newVal) != 0:
                return True
            else:
                print('Failed Validation to edit')
                return False

    def validate_add(self, newData):
        for i in range(len(newData)):
            if len(newData[i]) == 0:
                print('Failed Validation to add')
                return False
        return True

    def validate_ID(self, ID, attriID):
        if ID <= len(attriID):
            return True
        else:
            print('Failed validation for ID')
            return False