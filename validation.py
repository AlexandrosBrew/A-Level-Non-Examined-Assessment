import sqlite3

#Compares the value that is going to be entered to the validation rules and returns True/False depending if it meets the requirements
def validate_edit(attri, newVal, table):
    with sqlite3.connect('SignTeach.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM '+table)
        attributes = list(map(lambda x: x[0], cursor.description))
        cursor.execute('SELECT * FROM '+table)
        IDs = cursor.fetchall()
        if attri in attributes and len(newVal) != 0:
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