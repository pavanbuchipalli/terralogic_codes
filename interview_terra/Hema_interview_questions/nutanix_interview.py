# # list1 = [9,2,3,5,6]
# # for i in range(len(list1)):
# #     for j in range(len(list1)):
# #         if list1[i] > list1[j]:
# #             list1[i],list1[j] = list1[j],list1[i]
# #
# # print(list1)
# # second_large = list1[1]
# # print(second_large)
# #
# # first =list1[0]
# # for i in range(len(list1)):
# #     if list1[i] > list[i+1]:
#
#
# # class employee():
# #     def __init__(self,name,id):
# #         self.name = name
# #         self.id = id
# #     def details(self):
# #         print("name of employee is  {} and his/her is is {}".format(self.name,self.id))
# #
# #
# # class extra_details(employee):
# #     def __init__(self, name, id, age, sex):
# #
# #         super().__init__(name, id)
# #         self.age = age
# #         self.sex = sex
# #
# #     def details(self):
# #         print("name of employee is  {} and his/her is is {} age is {} and sex is {} ".format(self.name, self.id,self.age,self.sex))
# #
# # ouremp =["pavan","kiran","mohan","rajeeve","somu"]
# # our_emp_id= [55,6,44,66,22]
# # our_emp_age=[23,24,25,26,27]
# # our_emp_sex = ["male","male","male","male","male"]
# # # print(len(ouremp))
# # for i in range(len(ouremp)):
# #     obj = extra_details(ouremp[i],our_emp_id[i],our_emp_age[i],our_emp_sex[i])
# #
# #
# #     obj.details()
# #
# #
# #
#
# #
# # list1 = [9,2,3,5,6]
# # a = [3,2,4,5,865,90,78,32,9]
# # g =0
# # c= 0
# # for i in range(len(a) -1):
# #     if a[i] > g:
# #         g = a[i]
# # print(g)
# # for j in range(len(a) - 1):
# #     if a[j] > c and a[j] != g :
# #         c = a[j]
# # print(c)
#
#
#
#
#
#
#
#
#
#
#
#
#

# keys =["a","b","c","d","e"]
# values = [1,2,3]
# dict1 ={}
# # for i in range(len(l1)):
# #     dict1[l1[i]]  = l2[i]
# #
# # print(dict1)
#
#
def dicts(keys,values):
    d = {}
    for i in range(len(keys)):
        if i > len(values) -1:

            d[keys[i]] = None
        else:
            d[keys[i]]= values[i]

        # if i == len(keys)-1:
        #     print("inside",i)
        #     d[keys[i]] = None
    return (d)
    # return ("it is method")
keys = ["a", "b", "c","d"]
values = [1, 2, 3]

c =dicts(keys,values)
print(c)
# # print(keys,values)
# # keys = ["a", "b", "c"]
# # values = [1, 2, 3]
# #
# # for k, v in c.items():
# #     print(v)
# # if c.get("f") == None:
#
#
