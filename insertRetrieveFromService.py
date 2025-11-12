import mysql.connector

# connect to database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Super7898$$#",
    database="serviceDB"
)

def selectrecords():
    cursorObject = dataBase.cursor()
    # correct SQL syntax and parameter style
    sql = "SELECT * FROM tbl_service"
    # must be a tuple

    cursorObject.execute(sql)
    # printing all the recoords
   

    #  commit the change to actually save it
    #dataBase.commit()
    for i in cursorObject:
       print(i)
       
       #print(sql)
        #print("Records retrieved from tbl_service successfully")

        # close the connection
        # prepare a cursor object
def inserttables():
    print("enter new service")
    new=input()
    cursorObject = dataBase.cursor()
    #  correct SQL syntax and parameter style
    records = "INSERT INTO tbl_service (Services) VALUES (%s)"
    val = (new,)  # must be a tuple

    cursorObject.execute(records, val)
    dataBase.commit()
    print("Data inserted into tbl_service successfully")
    
    
inserttables()   
selectrecords()
dataBase.close()








