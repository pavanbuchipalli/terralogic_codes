for i in range (33,65):
    print(chr(i))
string = "pavan.bje,be/bvj'nhdb.l,nv.,sv.dvvds"
for i in string:
    for j in range(33,65):
        if i == chr(j):
            print(i,j)

#             s=string.replace(i,"")
# print(s)


#
string = "pavan.bje,be@bvj$nhdb*l^nv(sv)dvvds"
v = ""
for i in string:
    if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        v += i
print(v)
# r = []
# g = string
# for i in string:
#     for j in range(33,65):
#         if i == chr(j):
#             # print(i,j)
#             # r.append[string.index(i)]
#             r.append(string.index(i))
# print(r)
# for i in r:
#     c = string.replace(string[i],"")
#     g = c
#     print(g)

#
