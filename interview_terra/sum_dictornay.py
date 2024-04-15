from collections import Counter
d1 = {"a":100,"b":200,"c":300,"e":800}
d2 = {"a":120,"b":300,"c":400,"d":200}
d3= {}
#type1
# x = Counter(d1)
# z = Counter(d2)
# x.update(z)
# print(dict(x))
# type2
# for i,k in zip(d1,d2):
#     if i == k:
#         d3[i]=d1[i]+d2[k]
#     else:
#         d3[i]=d1[i]
#         d3[k]=d2[k]
#
# print(d3)

# d1={"a":100,"c":200,"b":200}
# d2={"b":400,"a":200,"d":300}
# d3={}
# for i in d1:
#     for j in d2:
#         if i == j:
#             d3[i]=d1[i]+d2[j]
#         elif i != j and i not in d2 and j not in d1:
#             d3[i]=d1[i]
#             d3[j]=d2[j]
# print(d3)
#

print(d1.update(d2))
print(d1)