# # c = [i for i in range(1,10) if i%2==0]
# # print(c)
# #
# # a = {"pavan":22,'age':26}
# # a["pavan"]=33
# # print(a)

# d = { v: k for k, v in a.items()}
# print(d)
# from functools import reduce
# #
# numbers = [1, 2, 3, 4, 5,6]
#
# # Use reduce to calculate the sum of the numbers with a lambda function
# result = reduce(lambda x, y: x * y, numbers)
# print(result)
#
#
#
# a  ="pavan is pavan"
# v =""
# # for i in a.split(" "):
# #     if i not in v:
# #         v += i + " "
# # print(v.strip())
# # b =a.split(" ")
# # coutn = {}.fromkeys(b,0)
# # for i in b:
# #     if i in coutn:
# #         coutn[i] += 1
# #
# # print(coutn)
#
#
# v = "pavan is pavan"
# d ={}

# for i in v:
#     if i !=" ":
#
#         if i not in d :
#             d[i] = 1
#         else:
#             d[i]= d[i]+1
# print(d)
#
#
# a =[1,-10,11,12,14,17]
# mi = 0
# ma = 0
# for i in a:
#     if i < mi :
#         mi = i
#     elif i > ma :
#         ma = i
#
# print(mi,ma)

# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] < a[j]:
#             a[i],a[j] = a[j],a[i]
# print(a)

# #
# str="abcabcdafsweraumbrelzy"
# op =""
# new =""
# for i in range(len(str)):
#     if str[i] not in op:
#         op = op + str[i]
#         if i == len(str) - 1:
#             if len(op) > len(new):
#                 new = op
#     else:
#         if len(op) >len(new):
#             new = op
#             op = str[i]
#         else:
#             op = str[i]
#     # print(str[i])
#
# print(new)
#
#
# # n =6
# # v = 1
# # for i in range(1,n+1):
# #     v = v *i
# #
# #
# # print(v)
#


# class hemanth():
#     def __int__(self):
#         print("hello it is hemanth")
#
#
# class pavan(hemanth):
#     def name(self):
#         print("hello it is pavan")
#
# class mhhh(pavan):
#     def name(self):
#         print("hello it is mmh")
#
#
# obj =mhhh()
#
# obj.name()
# obj.name()
# obj.__int__()


# class hemanth():
#     def __int__(self):
#         print("hello it is hemanth")
#
#
# class pavan(hemanth):
#     def name(self):
#         print("hello it is pavan")
#
# class mhhh(pavan):
#     def name(self):
#         print("hello it is mmh")
#
#
# obj =mhhh()
#
# obj.name()
# # obj.name()
# obj.__int__()


#
# class hemanth():
#     def __int__(self):
#         print("hello it is hemanth")
#
#
# class pavan():
#     def name(self):
#         print("hello it is pavan")
#
# class mhhh(pavan,hemanth):
#     def name2(self):
#         print("hello it is mmh")
#
#
# obj =mhhh()
# onb2 =pavan()
#
# obj.name2()
# obj.name()
# obj.__int__()
# onb2.__int__()


# num =10
# flag = 0
# for i in range(2,num):
#     if num % i == 0:
#
#         flag = 1
# if flag == 0:
#     print("yes prime ")
#
# else:
#     print("no")

# for k in range(2, 100):
#     flag = 0
#     for i in range(2, k - 1):
#         if (k % i) == 0:
#             flag = 1
#
#     if flag == 0:
#         print("{} is  prime number".format(k))
#     else:
#         print("{} is  a not prime number".format(k))


# d = {"pavan":1,"hemanth":2}
# dd = {}
# for k ,v  in d.items():
#     dd[v]=k
# print(dd)


# Sample dictionary
# my_dict = {
#     'banana': 3,
#     'apple': 1,
#     'cherry': 5,
#     'date': 2
# }

# list1 =list(my_dict.keys())
# values =list(my_dict.values())
# print(list1)
# lenth= len(values)
# for i in range(lenth):
#     for j in range(0,lenth-i-1):
#         if values[j] > values[j+1]:
#             values[j] ,values[j + 1] =values[j+1], values[j]
            # values[j],values[j+1] = values[j+1],values[j]
# print(list1)
# print(values)
# sorted_dict={}
#     # for  k in list1:
#     #     sorted_dict[k]= my_dict[k]
#
# for i in range(len(values)):
#     for k, v in my_dict.items():
#         # print(values[i])
#         if v == values[i]:
#             sorted_dict[k] = values[i]


# print(list1)
# print(my_dict)
# print(sorted_dict)

# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)  # Output: 15 (1 + 2 + 3 + 4 + 5)

#
# for i in range(1,100,2):
#     if i % 3 == 0:
# #         print(i)
# def decorators(func):
#     def wrapper():
#         print("hi")
#         func()
#         print("hello")
#     return wrapper
#
# @decorators
# def new():
#     print("middle")
#
# @decorators
# def new2():
#     print("newwww")
#
# new()
# new2()
#
# r = [1,2,3,4]
#
#+
# v = list(map(lambda a : a*2,[x for x in r]))
# print(v)
#
# y = lambda a : a*2
# c = [[i for i in range(1,9)]for j in range(1,10)]
# print(c)
#
# c = [{x:y} for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
# print(c)


# c = [{x:x**2} for x  in range(1,5)]
# print(c)
# from functools import reduce
# listt = [1,2,23,33]
# def squtre(a):
#     return a >2
# a = reduce(lambda x,y: x+y ,listt)
#
# print(a)


#
# class Student:
#     def __init__(self, name, age):
#         self.__name = name  # Private attribute
#         self.__age = age    # Private attribute
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         if len(name) > 2:
#             self.__name = name
#         else:
#             print("Name should be at least 3 characters long.")
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if 0 < age < 150:
#             self.__age = age
#         else:
#             print("Age should be between 1 and 149.")
#
# # Create a Student object
# student1 = Student("Alice", 25)
#
# # Accessing attributes through getter methods
# print("Name:", student1.get_name())
# print("Age:", student1.get_age())
#
# # Trying to modify attributes directly
# # This will not work due to encapsulation
# # student1.__name = "Bob"  # This does not modify the private attribute
# # student1.__age = 30       # This does not modify the private attribute
# #
# # # Modifying attributes using setter methods
# student1.set_name("Bob")
# student1.set_age(30)
#
# # # Accessing attributes through getter methods
# print("Name:", student1.get_name())
# print("Age:", student1.get_age())
# import pandas as pd
# data=["1",2,"three",4.0]
# series=pd.Series(data)
# print(series)
# print(type(series))

# test = []
# a = "abc"
# for i in range(len(a)):
#     test1= ""
#     for j in range(len(a)):
#         if a[i] == a[j]:
#             continue
#         else:
#             test1+=a[i]
#             test1+=a[j]
#     test.append(test1)
#
# print(test)


# import numpy as np
# n1=np.array([10,20,30,40,50])
# n2=np.array([50,60,70,80,90])
# print(np.vstack((n1,n2)))



# a = [23,6,8,43,5,3,678]
# for i in range(len(a)):
#     if i % 2 ==0:
#         # print(a[i])
#         a.insert(i,a[i])
#
#     else:
#         # print("even",a[i])
#         a.insert(i+1, a[i])
#
# # print(a)
#
# li = []
# n = 4
# for i in range(1,2*n):
#     if i >= n+1:
#         # n=i
#         n = n-1
#         li.append(n)
#     # elif i==n:
#     #     li.append(i)
#     else:
#         li.append(i)


# # print(li)
#
# # Create a list of tuples
# data = [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 22)]
#
# # Access the values inside each tuple
# # for item in data:
# #     id, name, age = item
# #     print(f"ID: {id}, Name: {name}, Age: {age}")
# for i in range(len(data)):
#     v = data[i][0] +data[i][2]
#     data[i][0]=v
# print(data)


# d = [{x:x**2} for x in range(1,10)]
#
# print(d)

# dict1 = {}
# for i in range(1,10):
#     dict1[i]= i**2
# print(dict1)


#
# import re
# 	# i ="127.112.293.44"
# ips = ["127.112.299.44","127.512.293.44","127.112.253.44","127.112.233.44","827.112.293.44"]
# for i in ips:
#     p1 = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}"
#          # r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
#     c = re.search(p1, i)
#      # print(c)
#     if c:
#       print(i,"yes it is a valid ip")
#     else:
#           print(i,"No it is not a valid ip")

# from collections import OrderedDict
#
# my_dict = OrderedDict()
# my_dict['one'] = 2
# my_dict['two'] = 1
# my_dict['three'] = 3
#
# print(my_dict)
# Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)])
# num = 4
# if (num & 1)==0:
#     print("even")
# else:
#     print("odd")


# def count(n):
#     for i in range(n):
#         yield i
#
# c = count(5)
# for i in c:
#     print(i)
# from collections import *
# li=[1,22,2,2,2,1,222,222]
# count1 = Counter(li)
# print(count1)





# class terra():
#     def bench(self,a):
#         print("{} u r on bench".format(a))
#
#
#     def project(self,a):
#         print("{} u r on project".format(a))
#
# obj = terra()
# obj.project("pavan")




# class Animal:
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# class Bird(Animal):
#     def speak(self):
#         return "Tweet!"
#
# # Function that takes any Animal object and calls its speak() method
# def animal_sound(animal):
#     print(animal.speak())
#
# # Create instances of different animals
# dog = Dog()
# cat = Cat()
# bird = Bird()
#
# # Call the function with different animal objects
# animal_sound(dog)   # Output: Woof!
# animal_sound(cat)   # Output: Meow!
# animal_sound(bird)  # Output: Tweet!


#
# with open("new.txt","r+")as pavan:
#    v =pavan.write("pavan this is first line ")
#    print(pavan.read())


# Decorator

# def my_deco(func):
#     def wrappe():
#         print("before")
#         func()
#         print("after")
#     return wrappe()
# @my_deco
# def animal():
#     print("it make sounds")
#
#
# new_list = [10,22,33,1,2,42,111,232,0]
#
#
# for i in range(len(new_list)):
#     for j in range(len(new_list)-1):
#         if new_list[j] > new_list[j+1]:
#             new_list[j],new_list[j+1] = new_list[j+1],new_list[j]
#
#
# print(new_list)
#
# d = {}
#
# string_2 ="this is my string test"
#
# for i in string_2:
#     if i != " ":
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] = d[i] + 1
#     else:
#         pass
#
# new_list = []
# for h,r in d.items():
#    new_list.append(r)
#
# print(new_list)
# # print(d)
# # for j in d.values():
# #
# #     print(j)
# #
#
#
# for i in range(len(new_list)):
#     for j in range(len(new_list)-1):
#         if new_list[j] > new_list[j+1]:
#             new_list[j],new_list[j+1] = new_list[j+1],new_list[j]
#
#
# print(new_list)
# print(new_list[-1])
# c = 0
# for i in new_list:
#     c = c+i
# print(c)
#
# string_result = str(c)
# for i in range(len(string_result) - 1):
#     print(int(string_result[i])+int(string_result[i+1]))
# class office:
#     def __init__(self,name,age):
#         self.name =name
#         self.age = age
#     def emp(self):
#         print("name ",self.name)
#         print("age",self.age)
#
#
#
# class office2:
#     def __init__(self,name,age,phone ):
#         self.name =name
#         self.age = age
#         self.phone =phone
#     # def emp(self,phone):
#     #     print("name ",self.name)
#     #     print("age",self.age)
#     #     print("phone ", phone)
#
#
#     def emp(self,data):
#         print("name ",self.name)
#         print("age",self.age)
#         print("phone ", self.phone)
#         print("data",data)


# obj =office("pavan",34,666666)
# obj.emp("jvevgf")



#
# class first:
#     def __init__(self,name):
#         self.name = name
#     def emp_name(self):
#         print("my name is  ",self.name)
#
#
#
#
# obj = first("pavan")
# obj.emp_name()

# class Hr:
#     def work(self):
#         print("Should do Hr related work ")
#
# class Testing(Hr):
#     def work(self):
#         print("Should do testing related work ")
#
# class Developer(Hr):
#     def work(self):
#         print("Should do Developer related work ")
#
#
# class Manager(Hr):
#     def work(self):
#         print("Should do Manager  related work ")
#
#
# # def Comapny(Worker):
# #     Worker.work()
#
#
# # Manager =Manager()
# # Developer =Developer()
#
# Manager = Manager()
#
# Manager.work()



#
# class Employee:
#     def emp(self):
#         d = {}
#         while True:
#
#             data = input("do u want to give us data :--")
#             if data == "yes" :
#                 name = input("name of emp")
#                 age  = int(input("age of emp "))
#                 d.update({name:age})
#
#             else:
#                 print(len(d))
#                 print(d)
#                 break






# Employee=Employee()
# Employee.emp()


#
#
# class Employee:
#     def emp(self, **employee_data):
#         return employee_data
#
#
# # Example usage:
# employee = Employee()
#
# # Example employee data
# employee_data_1 = {"pavan", 22}
# employee_data_2 = {"pavan2", 222}
# emp3 ={"pavan3":333}
# #
# # # Calling the emp method with both employee data lists
# count = employee.emp(emp1 =employee_data_1, emp2 =employee_data_2,emp3 ={"pavan3":323})
# print("Number of employees:", count)  # Output: Number of employees: 2
# #
# #
#


# def my_function_with_args(arg1, *args):
#     print("First argument:", arg1)
#     for arg in args:
#         print("Next argument through *args:", arg)
#
# my_function_with_args("Hello", "world", "how", "are", "you")

#
# ip = "192.168.250.22"
# ip_split = ip.split(".")
# print(len(ip_split))
# if len(ip_split) ==  4 :
#     print("it is valid")
#     for i in range(len(ip_split)):
#         if int(ip_split[i]) > 0 and int(ip_split[i]) < 256  :
#
#     print("it is valid ")
#
#
#
# else:
#     print("it is not valid ")

#
# ip = "0.168.250.22"
# ip_split = ip.split(".")
# print(len(ip_split))
# flag = True
# if len(ip_split) ==  4:
#
#     for i in range(len(ip_split)):
#
#         if 0 <= int(ip_split[i]) < 256:
#             flag  =True
#
#         else:
#             flag = False
#             # print("Octet", i + 1, "is not valid")
#             break
# else:
#     print("false")
# if flag == True:
#     print("its is valid")
# else:
#     print("it is not valid")

# import re
#
# def validate_ipv4(ip):
#     # ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
#     ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
#     if re.match(ipv4_pattern, ip):
#         return True
#     else:
#         return False
 # Test cases
# print(validate_ipv4("127.0.0.1"))  # Output: True
# print(validate_ipv4("255.0.0.1"))     # Output: False
# #

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16]
#
# #
# #output = [4,10,
# for i in range(0 ,len(list1),3):
#     # if i %3 ==0:
#     #     print(i)
#         if list1[i] % 2 == 0:
#             print("index number is {}".format(i),list1[i])
#         else:
#             print("index number is {}".format(i),"but the result number is not even {}".format(list1[i]))


# class first:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         return "age and name  is {} {}".format(self.age,self.name)
#
# class second(first) :
#     def __init__(self,name,age,emp_id):
#         super().__init__(name,age)
#         self.emp_id = emp_id
#
#     def display(self):
#
#         return "emp name is  {} and age is  {} and his id number is  {}".format(self.name,self.age,self.emp_id)


# obj1 = second("pavan",25,3333)
# print(obj1.display())
#
#
# listss = [1,2,3,3,33,3,3,333]
# def sub(ele):
#     result = ele * ele
#     return result
#
# c = map(sub,listss)
# r = list(map(lambda x : x * x,listss))
#
# print(list(c))
# print(r)


# list2 =[1,2,3,4,5,56,6]
# comp = [i for i in list2 if i >10 ]
# print(comp)
#
# dicts = {x : x * x for x in list2}
# print(dicts)


# for i in range(len(list2)):
#     for j in range(i ,len(list2)):
#         # print(list2[i],list2[j])
#         if list2[i] > list2[j]:
#             list2[i], list2[j] = list2[j],list2[i]

# print(list2)
# def fib (n):
#     a =0
#     b =1
#     for i in range(2,n):
#         a, b = a+b ,a
#
#     return b
#
# obj = fib(10)

# print(obj)


# digi = 123
# reverse = 0
# while digi > 0 :
#     div = digi % 10
#     reverse = reverse * 10 + div
#     digi = digi // 10
#
# # print(reverse)
#

# srti = "hemnath mac wont come"
# dicts ={}.fromkeys(srti,0)
# for i in srti:
#     if i not  in dicts:
#         dicts[i] = 1
#     else:
#         dicts[i] = dicts[i]+1

# print(dicts)

# sub_str = srti.split(" ")
# dict2 = {}
# for index,i  in enumerate(sub_str):
#     if index==0:
#         index = index + 1
#         dict2[index] = i
#     elif index in dict2.keys():
#         index +=1
#         dict2[index]=i
# print(dict2)

#
# dict2 = {'Student1':{'Name':{"Hemant":{"company":'Terralogic'}}, 'Gender':'Male'},
#          'Student2':{'Name':{"Pavan":{"company":'Terralogic1'}}, 'Gender':'Male'},
#          'Student3':{'Name':{"Kamal":{"company":'Terralogic32'}}, 'Gender':'Male'}}
# names_str=""
# for i in range(len(dict2)):
#     r ="Student"+str(i+1)
#     v = dict2[r]["Name"]
#     # print(v)
#
# #     names_str = names_str +" "+ v
# # print(names_str)
#
# for k ,v in dict2.items():
#     for j,r in v.items():
#         if j == "Name":
#             for p,g in r.items():
#                 for l,m in g.items():
#                     print(l)
#                     if m =="Terralogic":
#                         g[l] = "google"
# print(dict2)
#
#
# lis = [1,2,3,4,5,6,7,8,9,10]
# new_lis = []
# for i in lis:
#     if i % 2 == 0:
#         new_lis.insert(0,i)
#
#     else:
#         new_lis.append(i)

# print(new_lis)
#
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# out = []
# for num in lis:
#     if num % 2 != 0:  # If number is odd, append to the left
#         out.insert(0, num)
#     else:  # If number is even, append to the right
#         out.append(num)
#
# print(out)
#
# for i in lis:
#     for j in lis:
#         if i % 2 != 0 and i not in new_lis:
#             new_lis.append(i)
#     if i not in new_lis and i%2==0:
#         new_lis.append(i)
#
#
#     else:
#         new_lis.insert(-1,i)
# print(new_lis)


# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # out = []
# # for index, num in enumerate(lis):
# #     if num % 2 != 0:  # If number is odd, append to the left
# #         out.append(num)
# #     else:  # If number is even, append to the right
# #         out.insert(index - len(out), num)
# #
# # print(out)
#
# for i in range(len(lis)):
#     for j in range(i, len(lis)):
#         if lis[i] % 2 ==0:
#             lis[j], lis[i] = lis[i], lis[j]
#         # elif lis[i] % 2 == 0 and lis[j] = 0:
#
# for i in range(len(lis)):
#     for j in range(i,len(lis)):
#         if lis[i] % 2 ==0 and lis[j] % 2 ==0:
#             lis[j], lis[i] = lis[i], lis[j]
# print(lis)
#
#
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# test = []
# for i in range(len(lis)):
#     if i<len(lis):
#         if lis[i]%2==0:
#             test.append(lis.pop(i))
#
# print(lis+test)
# # print(lis)
#


# Decorator function
# def my_decorator(func):
#     def gold():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return gold
#
# @my_decorator# Function to be decorated
# def say_hello():
#     print("Hello!")

# Decorate the function
# my_decorator(say_hello)
#
# # # Call the decorated function
# say_hello()

# result_dict = {}
# my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
#
# # Convert dictionary to list of tuples (key, value)
# dict_items = list(my_dict.items())
#
# print(dict_items)
#
# for i in range(len(dict_items)):
#     for j in range(i+1, len(dict_items)):
#         if dict_items[i][1] > dict_items[j][1]:
#             dict_items[i],dict_items[j] = dict_items[j],dict_items[i]
#
# print(dict_items)
#
# for items in dict_items:
#     print(items[0])
#     result_dict[items[0]] =items[1]
#
# print(result_dict)


# import re
#
#
# def is_valid_email(email):
#     # Regular expression pattern for validating email addresses
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#
#     # Check if the provided email matches the pattern
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
#
#
# # Example usage:
# email1 = "example@example.com"
# email2 = "invalid_email@example"
#
# print(is_valid_email(email1))  # Output: True
# print(is_valid_email(email2))  # Output: False

#
# for k in range(2, 100):
#     f = 0
#     for i in range(2, k - 1):
#         if (k % i) == 0:
#             f = 1
#
#     if f == 0:
#         print("{} is prime number".format(k))
#     else:
#         print("{} is  not prime number".format(k))
#
#
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator# Function to be decorated
# def say_hello():
#     print("Hello!")
#
# # Decorate the function
#
# say_hello()



# list1 = [9,2,3,5,6]
# a = [3,2,4,5,865,90,78,32,9]
# g =0
# c= 0
# for i in range(len(a) -1):
#     if a[i] > g:
#         g = a[i]
# print(g)
# for j in range(len(a) - 1):
#     if a[j] > c and a[j] != g :
#         c = a[j]
# print(c)



# with open("pavan.txt","r") as file:
#     # f = file.write("this is first line \n")
#     # f2 = file.write("this is second line \n")
#     readd = file.read()
# print(readd)


# list1 =[1,2,9,4,5]
# left = 0
# right = len(list1) -1
# while left < right :
#     list1[left] , list1 [right] = list1[right] , list1[left]
#     left +=1
#     right -= 1
#
#

# a = 897
# reverse = 0
# while a > 0:
#     digi = a % 10
#     reverse = reverse *10 +digi
#     a = a // 10
# print(reverse)


# def even_numbers():
#     n = 0
#     while True:
#         yield n
#         n += 2
#
# # Create a generator object
# gen = even_numbers()
#
# # Iterate over the generator and print the first 5 even numbers
# for _ in range(5):
#     print(next(gen))  # Output: 0, 2, 4, 6, 8
