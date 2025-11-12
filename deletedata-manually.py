import mysql.connector

# connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)
def showtablerecords():
   sql = "SELECT * FROM tbl_service"
    # must be a tuple

   cursorObject.execute(sql)
   for i in cursorObject:
       print(i)
    


# prepare a cursor object
cursorObject = dataBase.cursor()

# correct SQL syntax and parameter style
sql = "DELETE FROM tbl_service WHERE Id=10"
  # must be a tuple

cursorObject.execute(sql)

#  commit the change to actually save it
dataBase.commit()

print("Data deleted from tbl_service successfully")
showtablerecords()
# close the connection
dataBase.close()