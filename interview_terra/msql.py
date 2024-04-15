
import pymysql
from mysql.connector import connection
import pymysql.cursors


def mysql_connect():
    conn=pymysql.connect(host='localhost',user='root',password='password')
    cur=conn.cursor()
    return cur,conn
def create_db():
        with connection.CursorBase as cursor:
            cursor.execute('CREATE DATABASE Employee')







cur,mdb=mysql_connect()
print(cur,mdb)


