str1="p1=0p2=1p3=2p4=3"
#d={"p1":0,"p2":1,"p3":2,"p4":3}
import re
#pattern = r'((\w{1})(\d{1})=(\d{1}))'
pattern = r'(\w+\=\d)(\w+\=\d)(\w+\=\d)(\w+\=\d)'

v = re.search(pattern,str1)
#
# print(v)
print(v.group())
d={}
for i in range(1,5):
    s1=v.group(i)
    data=s1.split("=")
    d[data[0]]=int(data[1])
print(d)