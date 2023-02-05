import sqlite3
from .createDatabase import load_database
from .validation import *

valid = Validation()

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
    
    def getAllUsers(self):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM UserAccounts')
            results = cursor.fetchall()
            return results

    def getAnswers(self, answerID):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Answers")
            results = cursor.fetchall()
            for i in range(len(results)):
                if results[i][0] == answerID:
                    return results[i]
            print('Search invalid')
    
    def getImages(self, ImageNo):
        with sqlite3.connect('SignTeach.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Images")
            results = cursor.fetchall()
            for i in range(len(results)):
                if results[i][0] == ImageNo:
                    return results[i]
            print('Image does not exist')

class EditDatabase:
    def __init__(self):
        load_database()

    def editDatabase(self, attri, newVal, attriID, ID, table):
        if valid.validate_edit(attri, newVal, table) and valid.validate_ID(ID, attriID):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("Update %s SET %s = '%s' WHERE %s = '%s'" % (table, attri, newVal, attriID, ID))
                print('Completed edit')
        else:
            print('Could not complete edit')
    
    def addUserAccount(self, Username, Password, Email):
        if valid.validate_add((Username, Password)):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO UserAccounts (Username, Password, Email) VALUES ('%s', '%s', '%s')" % (Username, Password, Email))
    
    def addImage(self, imageLoc, imageAnswer, imageNo):
        if valid.validate_add((imageLoc, imageAnswer)):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO Images (Image, ImageAnswer) VALUES ('%s', '%s')" % (imageLoc, imageAnswer))
    
    def addAnswer(self, QuestNo, ModNo, UserAnswer):
        if valid.validate_add((QuestNo, ModNo)):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO Answers (QuestionNo, ModleNo, UserAnswer) VALUES ('%s', '%s', '%s')" % (QuestNo, ModNo, UserAnswer))
        
    def removeDatabase(self, attriID, ID, table):
        if valid.validate_ID(ID, attriID, table):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM %s WHERE  %s = '%s'" % (table, attriID, ID))

if __name__ == "__main__":
    edit = EditDatabase()
    get = GetDatabase()
    edit.addImage("C:/Users/vali\Documents/GitHubRepos/ALevelNEA/website/static/images/Question1.png", 'A', 1)
    print(get.getImages(1))