import sqlite3

def load_database():
    with sqlite3.connect('SignTeach.db') as db:
        cursor = db.cursor()
        sql_UserAccount = '''
            CREATE TABLE IF NOT EXISTS UserAccounts(
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT,
                Password TEXT
            );
            '''
        cursor.execute(sql_UserAccount)
        sql_Answers = '''
                CREATE TABLE IF NOT EXISTS Answers(
                QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
                QuestionNo INTEGER,
                ModuleNo INTEGER,
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

if __name__ == '__main__':
    load_database()