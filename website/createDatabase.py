import sqlite3 #!Imports the sqlite3 library

#!Function to load the database file (or create one if it does not exitst)
def load_database():

    #!Connects to the database file so it can be manipulated.
    with sqlite3.connect('SignTeach.db') as db: 
        cursor = db.cursor() #!This cursor lets me navigate the database
        
        #!This last section creates the different tables that I will be utilising
        sql_UserAccount = '''
            CREATE TABLE IF NOT EXISTS UserAccounts(
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT,
                Password TEXT,
                Email TEXT
            );
            '''
        cursor.execute(sql_UserAccount)
        sql_Answers = '''
                CREATE TABLE IF NOT EXISTS Answers(
                QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
                QuestionNo INTEGER,
                UserAnswer TEXT
            );
            '''
        cursor.execute(sql_Answers)

        sql_Users = '''
            CREATE TABLE IF NOT EXISTS Users(
            UserID INTEGER,
            QuestionID INTEGER 
            );
            '''
        cursor.execute(sql_Users)

        sql_Images = '''
        CREATE TABLE IF NOT EXISTS Images(
        ImageID INTEGER PRIMARY KEY AUTOINCREMENT,
        ImageNo INTEGER,
        Image TEXT,
        ImageAnswer TEXT
        );
        '''
        cursor.execute(sql_Images)

if __name__ == '__main__': #!This executes the function if this file is run directly and not run from an import.
    load_database()