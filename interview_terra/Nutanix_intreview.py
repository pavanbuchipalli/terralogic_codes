lis =[1,2,3]
dictt = {}
# for i in lis:
#     dictt[i] =0
#
# print(dictt)

# for i in range(len(lis)):
    # dictt[i] = lis[i]**2

# print(dictt)

# test_dict = {}
# for index,values in enumerate(lis):
#     print(values,index)
#     test_dict[index] = values
# print(test_dict)

string_main ="Nutanians"
string1 =string_main.lower()
dupli ={}.fromkeys(string1,0)
for  char in string1:
    if char in  dupli:
        dupli[char] += 1
print(dupli)
# for key,value in dupli.items():
valuse_list= list(dupli.values())
for i in range(len(valuse_list)):
    for j in range(i,len(valuse_list)-1):
        if valuse_list[j] < valuse_list[j+1]:
            valuse_list[j],valuse_list[j+1]= valuse_list[j+1],valuse_list[j]


# for maxx in valuse_list:
#     if dupli[]
print(valuse_list)
#
maximu =max(valuse_list)
# print(maximu)
for k,v in dupli.items():
    if v ==maximu:
        print(k)

# print(valuse_list)
#
#

from collections import Counter

list2 = [1,2,2,3,3,4,4]
count1 =Counter(list2)
print(count1)



















# v = [{x:x**2} for x in range(1,10)]
# print(v)
# d = {}
# for i in range(1,10):
#     d[i]=i**2
# print(d)

#
# d ={1:2,10:100}
# print(d.keys())


#
# string_main ="Nutanians"
# test = ""
# for i in string_main:
#     if i not in test:
#         print(f"{i} : {string_main.count(i)}")
