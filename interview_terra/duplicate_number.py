a = [1,8,9,0,6,7,8,9,4,3,7,9,0,2,98,9,90,97,55]

c = []
for i in a:
    if i not in c:
        c.append(i)
print(c)