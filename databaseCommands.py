import sqlite3

from matplotlib.backend_bases import cursors
from werkzeug import run_simple
from createDatabase import load_database
from validation import *

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

    def getAnswers(self, ModNo):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Answers")
            results = cursor.fetchall()
            for i in range(len(results)):
                if results[i][2] == ModNo:
                    return results[i]
            print('Search invalid')
    
    def getImages(self, ImageID):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Images")
            results = cursor.fetchall()
            for i in range(len(results)):
                if results[i][0] == ImageID:
                    return results[i]
            print('Image does not exist')

class EditDatabase:
    def __init__(self):
        load_database()

    #!Edits the UserAccounts table
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

