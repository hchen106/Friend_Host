import mysql.connector
import random
import sys
from mysql.connector import Error

def MySQL_Connect(host,port,user,password,database = None):
    if(database == None):
        mydb = mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = password
        )
        return mydb
    else:
        mydb = mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = database
        )
        return mydb

def MySQL_Cursor(database):
    mycursor = database.cursor()
    return mycursor

def MySQL_ShowDB(cursor):
    cursor.execute("SHOW DATABASES")


def MySQL_Create_DB(cursor,name):
    sentence = "CREATE DATABASE " + name
    #print(sentence)
    cursor.execute(sentence)

def DB_Create_Table(cursor, statement):
    sentence = "CREATE TABLE IF NOT EXISTS " + statement
    cursor.execute(sentence)

def DB_Alter_Table(cursor, statement):
    sentence = "ALTER TABLE " + statement
    cursor.execute(sentence)

def DB_Show_Tables(cursor):
    cursor.execute("SHOW TABLES")

def Table_Insert(cursor, database, statement, values):
    sentence = "INSERT INTO " + statement
    cursor.execute(sentence, values)
    database.commit()

def Table_Insert_many(cursor, database, statement, values):
    sentence = "INSERT INTO " + statement
    cursor.executemany(sentence, values)
    database.commit()

def Table_Select_All(cursor, statement, limit = sys.maxsize * 2 + 1, offest = 0):
    sentence = "SELECT * FROM " + statement + " LIMIT " + str(limit) + " OFFSET " + str(offest)
    cursor.execute(sentence)

def Table_Select_Column(cursor, statement1, statement2):
    sentence = "SELECT " + statement1 + " FROM " + statement2
    cursor.execute(sentence)

def Table_Select_Filter(cursor, statement1, statement2, statement3):
    sentence = "SELECT * FROM " + statement1 + " WHERE " + statement2 + " = %s"
    cursor.execute(sentence, statement3)

def Table_Select_Filter_Keyword(cursor, statement1, statement2, statement3):
    sentence = "SELECT * FROM " + statement1 + " WHERE " + statement2 + " LIKE " + statement3
    cursor.execute(sentence)

def Table_Select_All_Sort_ascending(cursor, statement, statement1):
    sentence = "SELECT * FROM " + statement + " ORDER BY " + statement1
    cursor.execute(sentence)

def Table_Select_All_Sort_descending(cursor, statement, statement1):
    sentence = "SELECT * FROM " + statement + " ORDER BY " + statement1 + " DESC"
    cursor.execute(sentence)

def Table_Row_Delete(cursor, database, statement, statement1, statement2):
    sentence = "DELETE FROM " + statement + " WHERE " + statement1 + " = %s"
    cursor.execute(sentence, statement2)
    database.commit()

def Table_Delete(cursor, statement):
    sentence = "DROP TABLE IF EXISTS " + statement
    cursor.execute(sentence)

def Table_Update(cursor, database, statement, statement1, statement2):
    sentence = "UPDATE " + statement + " SET " + statement1 + " = %s WHERE " + statement1 + " = %s"
    cursor.execute(sentence, statement2)
    database.commit()

#can have join function also, but not really needed right now

mydb = MySQL_Connect("localhost",3030, "nashdash00", "nashdash00", "test_db")

cursor = MySQL_Cursor(mydb)

#MySQL_Create_DB(cursor, "test_db")

MySQL_ShowDB(cursor)

print("-----------------------------------")
print("Databases avail:")
print("-----------------------------------")
for x in cursor:
    print(x)

DB_Create_Table(cursor, "cust (name VARCHAR(255), password VARCHAR(255), invitation_code VARCHAR(255))")

DB_Show_Tables(cursor)

print("-----------------------------------")
print("Tables in database:")
print("-----------------------------------")
for x in cursor:
    print(x)

#DB_Alter_Table(cursor, "users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# value = random.randint(0,1000000)
# print(value)
# insert = str(value)
# Table_Insert(cursor, mydb, "users (name, password, invitation_code) VALUES (%s, %s, %s)", ("nashdash00", "nashdash00", insert))
# print("-----------------------------------")
# print("Value in Table:")
# print("-----------------------------------")
# print(cursor.rowcount, "inserted")
# print("1 inserted, ID:", cursor.lastrowid)

# value = random.randint(0,1000000)
# value1 = random.randint(0,1000000)
# val = [("nashdash13", "nashdash", str(value)), ("nash", "dash", str(value1))]
# Table_Insert_many(cursor, mydb, "users (name, password, invitation_code) VALUES (%s, %s, %s)", val)
# print("-----------------------------------")
# print("Value in Table:")
# print("-----------------------------------")
# print(cursor.rowcount, "inserted")
# print("1 inserted, ID:", cursor.lastrowid)

Table_Select_All(cursor, "users")
print("-----------------------------------")
print("All value in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)

Table_Select_Column(cursor, "name, invitation_code", "users")
print("-----------------------------------")
print("Name and invitation code in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)

print("-----------------------------------")
print("First Name and invitation code in Table:")
print("-----------------------------------")
result = cursor.fetchone()
print(result)

Table_Select_Filter(cursor, "users", "name", ("nashdash00", ))
print("-----------------------------------")
print("Name in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)

Table_Select_Filter_Keyword(cursor, "users", "name", "'%nash%'")
print("-----------------------------------")
print("Name includes nash in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)

Table_Select_All_Sort_ascending(cursor, "users", "invitation_code")
print("-----------------------------------")
print("All value by order of code in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)

Table_Select_All_Sort_descending(cursor, "users", "invitation_code")
print("-----------------------------------")
print("All value by order of code des in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)

Table_Row_Delete(cursor, mydb, "users", "id", ("2", ))
print(cursor.rowcount, "column(s) deleted")

Table_Delete(cursor, "cust")

Table_Update(cursor, mydb, "users", "invitation_code", ("empty", "855560"))
print(cursor.rowcount, "column(s) affected")
Table_Select_All(cursor, "users")
print("-----------------------------------")
print("All value after change in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)


Table_Select_All(cursor, "users", "2")
print("-----------------------------------")
print("All value Limited in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)

Table_Select_All(cursor, "users", "2", "5")
print("-----------------------------------")
print("All value Limited with offset in Table:")
print("-----------------------------------")
result = cursor.fetchall()
for x in result:
    print(x)



