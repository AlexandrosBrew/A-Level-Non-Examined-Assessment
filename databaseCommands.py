import sqlite3
from createDatabase import load_database

#Compares the value that is going to be entered to the validation rules and returns True/False depending if it meets the requirements
def validate_edit(attri, newVal, ID, table):
    with sqlite3.connect('SignTeach.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM '+table)
        names = list(map(lambda x: x[0], cursor.description))
        cursor.execute('SELECT * FROM '+table+' WHERE '+attri+' == '+ID)
        IDs = cursor.fetchall()
        if attri in names and len(newVal) != 0 and ID in IDs:
            return True
        else:
            print('Failed Validation')
            return False

class GetDatabase:
    def __init__(self):
        load_database()
    
    def getUserAccount(self, attri, userID, value):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT '+attri+' FROM UserAccounts WHERE UserID == '+userID+' OR '+
            attri+' == '+value)
            results = cursor.fetchall()
            results = []
            for each in results:
                results += [each]
            return results

class EditDatabase:
    def __init__(self):
        load_database()
    
    def editUsers(self, attri, UserID, table, newVal):
        if validate_edit(attri, newVal, UserID, table):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute('UPDATE '+table+' SET '+newVal+' WHERE UserID == ' +UserID)
                print('Completed edit')

        else:
            print('Could not complete edit')

