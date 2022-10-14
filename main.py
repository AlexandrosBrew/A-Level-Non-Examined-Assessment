from databaseCommands import *

# editdb.addUserAccount('Alex', 'greycourt')

editdb = EditDatabase()
editdb.removeUserAccount('Alex')
getdb = GetDatabase()
getdb.getUserAccount('Alex')
