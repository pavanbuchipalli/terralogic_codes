from multiprocessing.dummy import connection

import mysql.connector
dataBase = mysql.connector.connect(host="127.0.0.1",
                                        user="root",
                                        passwd="password",
                                   database="assignment")
print(dataBase)
mycurso = dataBase.cursor()


# to create table

mycurso.execute("CREATE DATABASE assignment")

# to show datatables

mycurso.execute("SHOW DATABASES")
for x in mycurso:
    print(x)

# create table

mycurso.execute("CREATE TABLE employee (EMPLOYEE_ID INT(5), FIRST_NAME VARCHAR(25),LAST_NAME VARCHAR(25),EMAIL VARCHAR(25),HIRE_DATE VARCHAR(25))")


 # to show tables

mycurso.execute("SHOW TABLES")
#
for x in mycurso:
  print(x)

#  to edit the table filed name positions

mycurso.execute("ALTER TABLE employee MODIFY EMPLOYEE_ID INT(5) AFTER HIRE_DATE")
mycurso.execute("ALTER TABLE employee MODIFY EMAIL VARCHAR(25) AFTER HIRE_DATE")


# to insert the valuse into the table

sql = "INSERT INTO employee (EMPLOYEE_ID, FIRST_NAME,LAST_NAME,EMAIL,HIRE_DATE) VALUES (%s,%s,%s,%s,%s)"
val = [
  (100,'Neena', 'Kochhar','neena@gmail.com','1987-07-23'),
  (200,'Bruce', 'Khoo','bruce@gmail.com','1987-06-30'),
  (300,'Valli', 'Himur','valli@gmail.com','1987-07-07'),
  (400,'Nancy', 'Ande','nanc@gmail.com',' 1987-10-01'),
  (500,'John', 'Kumar','john@gmail.com','1987-07-01')
]
#
mycurso.executemany(sql, val)

dataBase.commit()


mycurso.execute("select * from employee where MONTH(HIRE_DATE)='07'or DAY(HIRE_DATE)='07';")
for i in mycurso:
    print(i)

# to drop table

# sql = "DROP TABLE employee"
#
# mycurso.execute(sql)

