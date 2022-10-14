import sqlite3
from unittest import result
from createDatabase import load_database

#Compares the value that is going to be entered to the validation rules and returns True/False depending if it meets the requirements
def validate_edit(attri, newVal, table):
    with sqlite3.connect('SignTeach.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM '+table)
        names = list(map(lambda x: x[0], cursor.description))
        cursor.execute('SELECT * FROM '+table)
        IDs = cursor.fetchall()
        if attri in names and len(newVal) != 0:
            return True
        else:
            print('Failed Validation')
            return False

def validate_add(newData):
    for i in range(len(newData)):
        if len(newData[i]) == 0:
            print('Failed Validation')
            return False
    return True

class GetDatabase:
    def __init__(self):
        load_database()
    
    def getUserAccount(self, Username):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM UserAccounts')
            results = cursor.fetchall()
            for i in range(len(results)):
                if results[i][1] == Username:
                    print(results[i])
                    return results[i]
            print('User not found')

class EditDatabase:
    def __init__(self):
        load_database()

    #Edits the UserAccounts table
    def editUsersAccount(self, attri, newVal, Username):
        #Calls the validate_edit funciton to cherck if the entered value is alright to enter into the database
        if validate_edit(attri, newVal, 'UserAccounts'):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("Update UserAccounts SET %s = '%s' WHERE Username = '%s'" % (attri, newVal, Username))
                print('Completed edit')
        else:
            print('Could not complete edit')
    
    def addUserAccount(self, Username, Password):
        if validate_add((Username, Password)):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO UserAccounts (Username, Password) VALUES ('%s', '%s')"% (Username, Password))
        
    def removeUserAccount(self, Username):
        if validate_add(Username):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM UserAccounts WHERE Username = '%s'" % (Username))

