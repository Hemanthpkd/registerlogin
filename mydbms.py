 
import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='hemanth6@mYsql'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE registerlogin")
print("All Done")