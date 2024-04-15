import mysql.connector

dataBase = mysql.connector.connect(host="127.0.0.1",
                                                user="root",
                                                passwd="password")
print(dataBase)
mycurso = dataBase.cursor()

#  show databases
mycurso.execute("show databases")
for i in mycurso:
    print(i)