import mysql.connector

def conDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="vegamilo",
        password="abcd",
        database="vegamilo",
        )
    return mydb

class Con:
    def getHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    
    def getnameHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT name FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall
        mycursor.close()
        mydb.close()
        return data
    
    def insertHW(name, hw_name):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hard_ware (name,hw_name, status, value) VALUES ('{}', '{}','OFF', 8)".format(name,hw_name)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID
    
    def updateHW(status, value):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hard_ware SET (status, value) = '{}', '{}'  WHERE id = {}".format(status, val)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
      
    def selectminidHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE id = SELECT MIN(id) FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall
        mycursor.close()
        mydb.close()
        return data
    
    def selectidHW(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hard_ware WHERE ID = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    
    def deleteHW(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hard_ware WHERE ID = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data    
    