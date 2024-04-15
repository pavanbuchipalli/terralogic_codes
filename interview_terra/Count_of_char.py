#type1#
a = "pavana"
# for i in a:
#     if a.count(i)==1:
#         continue
#     else:
#         print(i,a.count(i))
#         break
#type2
# d = {}.fromkeys(a,0)
# for i in a:
#     if i in a:
#         d[i] += 1
#     else:
#         d[i]= 1
# print(d)
# for i,j in d.items():
#     if j == 2:
#         print(i)
#type3
# for i in range(0,len(a)):
#     count = 1
#     for j in range(i+1,len(a)):
#         if a[i]==a[j] and a[i]!=" ":
#             count = count+1
#     a = a[:j]+a[j+1:]
#     if count >1 and a[i]!=0:
#         print(count,a[i])
 # type 4
# c ={}
# count = 1
# for i in a:
#      if a.count(i) > 1:
#          count += 1
#          if i not in c:
#             c[i]=count
# print(c)