# # # a = {([])}
# # # count = 0
# # # ans = "false"
# # # for i in a:
# # #     if i =="(" or i=="{" or i == "[":
# # #         count = +1
# # #     elif i==")" or i =="}" or i=="]" :
# # #         count -= 1
# # #     if count <0:
# # #         print(ans)
# # #
# #
# # # from tkinter import *
# # # root = Tk()
# # # # Code to add widget will go here……..
# # # # w = Label(root, width = "500", height = "500")
# # # # w.pack()
# # # # root.mainloop()
# # #
# # #
# # # # numpy
# # # import numpy as np
# # #
# # # # 1 print the integers
# # # # arr = array([1,2,3,4,5,6,7])
# # #
# # # # print(arr)
# # # # 2 indexing the integers
# # # # print(arr[1])
# # #
# # # # 3 slicing the  arrary
# # # # arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # # # print(arr[0,2])
# # #
# # # # 4 to fine thr version
# # # # print(np.__version__)
# # #
# # # # 5 to form 2 d array or 2x2 matrix
# # # # arr = np.array([[[1,2,3],[2,3,4]],[[1,2,3],[2,3,4]]])
# # # # print(arr)
# # #
# # # # 6 to find the dimention the array
# # # # a = np.array(42)
# # # # b = np.array([1, 2, 3, 4, 5])
# # # # c = np.array([[1, 2, 3], [4, 5, 6]])
# # # # d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# # # #
# # # # print(a.ndim)
# # # # print(b.ndim)
# # # # print(c.ndim)
# # # # print(d.ndim)
# # #
# # # # 7 to add the values
# # # # arr = np.array([1,2,3],[4,5,5])
# # # my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# # # n = len(my_list)
# # # k = n
# # # mi = 0
# # # while k != 0:
# # #     for j in range(n):
# # #         if my_list[j] < mi:
# # #             mi = my_list[j]
# # #     n = n - 1
# # #     my_list.append(mi)
# # #     my_list.remove(mi)
# # #     k = k - 1
# # # print(my_list)
# # # import _mysql_connector
# #
# #
# # # a = "pavan"
# # # b = "kumar"
# # # v = ""
# # # for i in range(len(a)):
# # #     v = v +a[i]+b[i]
# # # print(v)
# #
# # # import random
# # # r = []
# # #
# # # print("Random integers between 0 and 51: ")
# # # for i in range(1,51):
# # #     y = random.randrange(50)
# # #     if y % 2 !=0:
# # #         r.append(y)
# # # print(r)
# # # for i in range(1,51,2):
# # #     if i not in r :
# # #         print(i,end=" ")
# #
# # # f = []
# # # c = ""
# # # a = "i am pavan"
# # # #n av apmai
# # # for i in range(len(a)):
# # #     if a[i] == " ":
# # #        v =  i
# # #        c= a.replace(a[i],"")
# # #        f.append(i)
# # # print(f,c)
# # # r =c[::-1]
# # # print(r)
# # # s1=""
# # # start=0
# # # for i,j in zip(range(len(a)),r):
# # #     if a[start+i]==" ":
# # #         s1=s1+a[start+i]+j
# # #         start=start+1
# # #     else:
# # #         s1=s1+r
# # # print(s1)
# #
# # # st = "i am pavan"
# # # l = []
# # # for i in range(len(st)):
# # #
# # #     if st[i] == " ":
# # #       l.append(i)
# # #
# # # res = st[::-1].replace(" ","")
# # # print(res)
# # # # print(l)
# # # a= ""
# # # for j in range(len(res)):
# # #    a = a+res[j]
# # #    if len(a) in l:
# # #        a = a+" "
# # # print(a)
# #
# # r =""
# # # v = ""
# # # string_= "hello world i hello am i"
# # # s = string_.split(" ")
# # #
# # # for i in range(len(s)):
# # #     ss = s[i]
# # #     v = v+" "+(ss[::-1])
# # #
# # # print(v)
# #
# # #     s.replace(i,i[::-1])
# # # print(string_)
# # # v  =""
# # # c = "pavan hello i ma navap olleh sey"
# # # for i in c:
# # #     if i not in v or i == " " :
# # #         v = v +i
# # #     print(v)
# #
# #
# #
# #
# # # class School():
# # #     def __int__(self):
# # #         print("hello")
# # #
# # #     def names(self):
# # #         print("name is {}")
# # #
# # #     def ages(self):
# # #         print("age is {}".format(self.age))
# # #
# # #
# # # obj =School()
# # # obj.names()
# #
# #
# # # class Cat:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #
# # #     def info(self):
# # #         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
# # #
# # #     def make_sound(self):
# # #         print("Meow")
# # #
# # #
# # # class Dog(Cat):
# # #     def __init__(self, name, age):
# # #         print("in constructure")
# # #         self.name = name
# # #         self.age = age
# # #
# # #     def info(self,a,b):
# # #
# # #         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
# # #         print("dog class")
# # #
# # #
# # #     def info(self):
# # #
# # #         print("dummy")
# # #         print("dog class")
# # #     def make_sound(self):
# # #         print("Bark")
# # #
# # # obj = Dog("dshf",4)
# # # obj.info(10,12)
# #
# #
# #
# #
# # import re
# # import subprocess
# #
# # # ip = "192.22.23.225"
# # # ip = "24.12.86.216"
# # # ip ="60.233.161.149"
# # class ip_():
# #     def ping_valid(self):
# #         while True:
# #             self.ip = input("provide a valid input :----")
# #             self.check = input("Do you want to check this ip address -- ({}) -- and ping it  select yes/no".format(self.ip))
# #             self.ip_validation()
# #
# #     def ip_validation(self):
# #
# #         if self.check == "yes":
# #             pattern = r"^(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
# #
# #             self.match = re.match(pattern, self.ip)
# #             self.matching()
# #         else:
# #             file3 = open("ip_check", "r")
# #             print("list of valid and invalid ips", "\n", file3.read())
# #     def matching(self):
# #         if self.match:
# #             ip_to_ping = self.match.group()  # Extract the matched IP address
# #             try:
# #                 output = subprocess.check_output(['ping', ip_to_ping])
# #                 ping_result = output.decode('utf-8')
# #                 print(ping_result)
# #                 files = open("ip_check", "a")
# #                 files.write("valid_ip:   " + ip_to_ping + "\n")
# #
# #             except subprocess.CalledProcessError as e:
# #                 print(e.output.decode('utf-8'))
# #                 files = open("ip_check", "a")
# #                 files.write("invalid_ip    :" + ip_to_ping + "\n")
# #
# #
# #         else:
# #             print("Invalid IP address format")


# import pandas as pd
# import plotly.graph_objects as go
#
# # Read data from an Excel file
# df = pd.read_excel(r"C:\Users\PavanB-3247\Downloads\pavan_data.xlsx")
#
# # Define labels and values based on the columns in your Excel file
# labels = df['Area'].tolist()
# values = df['Existing Team Members Proficient with this area'].tolist()
#
# # Define a list of different shades of green
# green_shades = [
#     'rgb(0, 64, 0)',    # Dark Green
#     'rgb(0, 100, 0)',   # One level below dark green
#     'rgb(0, 32, 0)',    # Two levels below dark green
#     'rgb(0, 128, 0)',   # Two levels above light green
#     'rgb(0, 255, 0)',   # One level above light green
#     'rgb(173, 255, 47)',  # Light green
#     'rgb(173, 255, 47)',  # Light green
# ]
#
# color_mappings = {
#     shade: color for shade, color in zip(df['Average Team Expertise (1-5)'].unique(), green_shades)
# }
#
# # Map the 'colors' column to RGB colors
# colors = df['Average Team Expertise (1-5)'].map(color_mappings)
#
# # Create a treemap figure
# fig = go.Figure(go.Treemap(
#     labels=labels,
#     parents=[''] * len(labels),
#     values=values,
#     texttemplate="%{label}<br>(%{value})",
#     textfont={"size": 15},
#     textposition="middle center",
#     hoverinfo="text",
#     marker=dict(
#         colors=colors  # Assign colors based on the 'colors' column
#     )
# ))
#
# fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
#
# # Display the treemap
# fig.show()

#
# # s =[2,3,4,5,6,7,8,9]
# # import random
# # c = random.randint(1,10) not in s
# # # if c not in s:
# # #     s.append(c)
# # # else:
# # #     r =random.randint(1, 10) not in  s
# #
# # print(c)
#
# import queue
# q = queue.Queue()
# number = [2,10,12,13,13,14]
# for i in number:
#     q.put(i)
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# class Animal:
#     def __init__(self, species, sound):
#         self.species = species
#         self.sound = sound
#
#     def make_sound(self):
#         return f"The {self.species} makes a sound: {self.sound}"
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__("Dog", "Woof")
#         self.name = name
#
#     def greet(self):
#         return f"{self.name} wags its tail and says: {self.sound}"
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__("Cat", "Meow")
#         self.name = name
#
#     def purr(self):
#         return f"{self.name} purrs: {self.sound}"
#
# # Creating instances of the classes
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
#
# # Using methods from the classes
# print(dog.greet())
# print(cat.purr())
import  copy


a = [1,2,3,4]
c=  copy.deepcopy(a)
print(c)