# type1
import re

# string = "mnqrstabcdefmnoplq"
# sub_str  = "tabcde"
# rdd = re.search(sub_str,string).group()
# print(rdd)
#
# # type2
# try:
#     string.index(sub_str)
#     print("yes")
# except:
#     print("no")
#
#
# # type3
# if string.find(sub_str) != -1:
#
#     print("yes")
# else:
#     print("no")


# typr4
string = "mnqrstabcdefmnoplq"
sub_str = "tabcde"
# r = len(sub_str)
# print(r)
# for i in range(len(string)):
#     # print(string[i:r])
#     if string[i:r] == sub_str:
#         print(string[i:r])
#         print("yes")
#         break
#     else:
#         r += 1
# import random
# c = random.randint(1,100)
#
# print(c)
for i  in range(len(string)):
    if sub_str[:] in string:
        print("yes")
        break