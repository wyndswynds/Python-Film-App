#STEP 1

import sqlite3 as sql
#above commands import sqlite(sql) module

#line to connect to db file - sql connect method/ function. 
dbffCon = sql.connect("Film_Flix_DB/filmflix.db")
#connect relative file path with film flix db

# create cursor method alllowing Python code to execute PostgreSQL commands. 
# Creating a variable and connecting it to the cursor method. 
dbffCursor = dbffCon.cursor()
# The above command and invocation allows Python's connnection to the db. 

# This is an example of aactive decomposition