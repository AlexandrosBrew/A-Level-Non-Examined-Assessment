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
    #Edits the UserAccounts table
    def editUsersAccount(self, attri, userID, newVal):
        #Calls the validate_edit funciton to cherck if the entered value is alright to enter into the database
        if validate_edit(attri, newVal, userID, 'UserAccounts'):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute('UPDATE UserAccounts SET '+newVal+' WHERE UserID == ' +userID)
                print('Completed edit')
        else:
            print('Could not complete edit')
    
    def addUserAccount(self, attri, value):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute(f'INSERT INTO UserAccounts ({attri}) VALUES ({value});')
            cursor.commit()


