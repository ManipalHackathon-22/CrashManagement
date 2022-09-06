import os
import psycopg2


conn = psycopg2.connect(
        host="localhost",
        database="CrashDatabase",
        user="postgres",
        password="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()



def PutUserInfo(name, ph, location, crashconfirm):
    cur.execute("INSERT INTO crashtable (ID, NAME, PH, LOCATION, CRASHCONFIRM) VALUES(7, \'%s\' , %d  , \'%s\', %d);" %(name, ph, location, crashconfirm))
    #cur.execute("INSERT INTO crashtable (ID, NAME, PH, LOCATION, CRASHCONFIRM) VALUES(5, 'aMARTYA' , %d , 'AIFBSHDF', %d);" %( ph,crashconfirm))
    conn.commit()


def GetUserInfo():
    cur.execute('SELECT * FROM crashtable')
    userInfoCheck = cur.fetchall()
    return userInfoCheck
    print("put something here")
    print(userInfoCheck)

#PutUserInfo('Aravind', 32764823, 'FSHBDFHABDNF', 0)

