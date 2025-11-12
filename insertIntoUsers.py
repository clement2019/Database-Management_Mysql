import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customerdb"
)

cursorObject = dataBase.cursor()
def selectrecords():
    cursorObject = dataBase.cursor()
    # correct SQL syntax and parameter style
    sql = "SELECT * FROM users"
    # must be a tuple

    cursorObject.execute(sql)
    # printing all the recoords
   

    #  commit the change to actually save it
    #dataBase.commit()
    for i in cursorObject:
       print(i)
       
      
        # prepare a cursor object
# Correct SQL syntax
records = "INSERT INTO users (Id, Username, Email) VALUES (%s, %s, %s)"
value = (1, 'John Doe', 'johndoe@yahoo.com')  # single tuple

cursorObject.execute(records, value)

# Commit changes
dataBase.commit()
selectrecords()
print("Data inserted into table successfully.")
dataBase.close()