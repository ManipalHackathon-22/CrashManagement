import os
import psycopg2
import random


conn = psycopg2.connect(
        host="localhost",
        database="CrashDatabase",
        user="postgres",
        password="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()



def PutUserInfo(name, ph, location, crashconfirm):
    print(name + ", " + location)
    cur.execute("INSERT INTO crashtable (ID, NAME, PH, LOCATION, CRASHCONFIRM) VALUES(%d, \'%s\' , %d  , \'%s\', %d);" %(random.randint(1000, 5000), name, ph, location, crashconfirm))
    #cur.execute("INSERT INTO crashtable (ID, NAME, PH, LOCATION, CRASHCONFIRM) VALUES(5, 'aMARTYA' , %d , 'AIFBSHDF', %d);" %( ph,crashconfirm))
    conn.commit()


def GetUserInfo():
    cur.execute('SELECT * FROM crashtable WHERE crashconfirm = 1 AND location LIKE \'%true%\'')
    userInfoCheck = cur.fetchall()
    return userInfoCheck
    print("put something here")
    print(userInfoCheck)

#PutUserInfo('Aravind', 32764823, 'FSHBDFHABDNF', 0)

