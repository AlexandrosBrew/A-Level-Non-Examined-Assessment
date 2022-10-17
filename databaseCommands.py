import sqlite3
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
    def editDatabase(self, attri, newVal, prevVal, table):
        #Calls the validate_edit funciton to cherck if the entered value is alright to enter into the database
        if validate_edit(attri, newVal, table):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("Update %s SET %s = '%s' WHERE %s = '%s'" % (table, attri, newVal, attri, prevVal))
                print('Completed edit')
        else:
            print('Could not complete edit')
    
    def addUserAccount(self, Username, Password):
        if validate_add((Username, Password)):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO UserAccounts (Username, Password) VALUES ('%s', '%s')"% (Username, Password))
    
    def addImage(self, imageLoc, imageAnswer):
        if validate_add((imageLoc, imageAnswer)):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO Images (Image, ImageAnswer) VALUES ('%s', '%s')" % (imageLoc, imageAnswer))
    
    def addAnswer(self, QuestNo, ModNo, UserAnswer):
        if validate_add((QuestNo, ModNo)):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("INSERT INTO Answers (QuestionNo, ModleNo, UserAnswer) VALUES ('%s', '%s', '%s')" % (QuestNo, ModNo, UserAnswer))
        
    def removeDatabase(self, remRecord, attri, table):
        if validate_add(remRecord):
            with sqlite3.connect('SignTeach.db') as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM %s WHERE %s = '%s'" % (table, attri, remRecord))

