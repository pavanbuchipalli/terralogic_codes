# import mysql.connector
#
# # login to
# dataBase = mysql.connector.connect(host="127.0.0.1", user="root", passwd="password")
# print(dataBase)
# # creating cursor obj
# mycursor = dataBase.cursor()
# # creating database
# mycursor.execute("create database employee_data1")
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)
# #   using database
#
# mycursor.execute("use employee_data1")
#
# studentRecord = """CREATE TABLE emp_data (
#                    emp_id INT NOT NULL,
#                    emp_name  VARCHAR(20) NOT NULL,
#                    emp_exp INT NOT NULL,
#                    emp_pro VARCHAR(30)
#                    )"""
#
#
# mycursor.execute(studentRecord)
# mycursor.execute("Show tables")
# for i in mycursor:
#     print(i)
# data = int(input("send the number:-"))
# # insert data into database
# sql = "INSERT INTO emp_data (emp_id, emp_name, emp_exp, emp_pro)\
#           VALUES (%s, %s, %s, %s)"
#
#
#
#         # val = [("1", "pavan", "3", "rampup"),
#         #         ("2", "pavan2", "1", "rampup1"),
#         #         ("3", "pavan3", "2", "rampup2")]
#
#         # id = int(input("give id number:-"))
#         # name = input("send the name:-")
#         # exp = int(input("give no of exp:-"))
#         # project= input("project name:-")
#         # r = (id, name, exp, project)
#         # val.append(r)
# mycursor.executemany(sql, val)
# dataBase.commit()
# mycursor.execute("select * from emp_data")
# for i in mycursor:
#     print(i)


# sql = "UPDATE emp_data SET emp_name = 'pavan22' WHERE emp_id = input('emp_id')"
#
# mycursor.execute(sql)
#
# dataBase.commit()
# mycursor.execute("select * from emp_data")
# for i in mycursor:
#     print(i)
# sql = "DELETE FROM emp_data WHERE emp_id ="+str(k)+""
# mycursor.execute(sql)
#
# dataBase.commit()
# mycursor.execute("select * from emp_data")
# for i in mycursor:
#     print(i)
#
#
#
#
# mycursor.execute("drop database employee_data1")
# dataBase.close()


import mysql.connector


class database():
    def __init__(self):
        self.exp = None
        self.op = None
        self.sql = None
        self.table_name = None
        self.database_name = None
        self.name = None
        self.count = None
        self.mycurso = None
        self.dataBase = None
        self.val = []
    def options2(self):
        print("Options Available:\n"
              "1. Create database\n"
              "2. use already exisiting database")
        self.op2 = int(input("Select Option: "))
        if self.op2 == 1:
            self.create_database()
        elif self.op2 == 2:
            self.options()


    def options(self):
        print("Options Available:\n"
              "1. Create Table\n"
              "2. Insert Into Table\n"
              "3. Update Table\n"
              "4. Delete from Table\n"
              "5. Delete Whole Table\n"
              "6. Exit")
        self.op = int(input("Select Option: "))
        if self.op == 1:
            self.create_table()
        elif self.op == 2:
            self.insert_data()

        # elif self.op == 3:
        #     self.update_tb_data()
        elif self.op == 4:
            self.delete_database()

    def login(self):
        self.dataBase = mysql.connector.connect(host="127.0.0.1",
                                                user="root",
                                                passwd="password")
        print(self.dataBase)
        self.mycurso = self.dataBase.cursor()

    def create_database(self):
        self.login()
        self.database_name = input("provide a  database_name")
        self.mycurso.execute("create database {}".format(self.database_name))
        self.mycurso.execute("SHOW DATABASES")
        print("Here is the list of databases")
        for x in self.mycurso:
            print(x)
        self.mycurso.execute("use {}".format(self.database_name))

    def create_table(self):
        self.login()
        self.mycurso.execute("SHOW DATABASES")
        print("Here is the list of databases")
        for x in self.mycurso:
            print(x)
        c = int(input("selcrt"))
        if c == 1:
            self.database_name=input("")
            self.mycurso.execute("use ")
            self.table_name = input("provide table_name:-")


        self.table_name = input("provide table_name:-")
        studentRecord = """CREATE TABLE {} (
                           emp_id INT NOT NULL,
                           emp_name  VARCHAR(20) NOT NULL,
                           emp_exp INT NOT NULL,
                           emp_pro VARCHAR(30)
                           )""".format(self.table_name)

        self.mycurso.execute(studentRecord)
        self.mycurso.execute("Show tables")
        print("Here are the list of tables")
        for i in self.mycurso:
            print(i)

    def insert_data(self):
        self.count = int(input("No of emp_data:-"))
        self.sql = "INSERT INTO {} (emp_id, emp_name, emp_exp, emp_pro)\
                  VALUES (%s, %s, %s, %s)".format(self.table_name)

        for i in range(self.count):
            self.id = int(input("give id number:-"))
            self.name = input("send the name:-")
            self.exp = int(input("give no of exp:-"))
            self.project = input("project name:-")
            self.val.append((self.id, self.name, self.exp, self.project))

        self.mycurso.executemany(self.sql, self.val)
        self.dataBase.commit()
        self.mycurso.execute(f"select * from {self.table_name}")
        for i in self.mycurso:
            print(i)

    def data(self):
        self.mycurso.execute(f"select * from {self.table_name}")
        for i in self.mycurso:
            print(i)

    def delete_database(self):
        self.mycurso.execute("drop database {}".format(self.database_name))
        self.dataBase.close()


ss = database()
ss.options2()
# ss.login()
# ss.create_database()
# ss.create_table()
# ss.insert_data()
# ss.data()
# ss.delete_database()