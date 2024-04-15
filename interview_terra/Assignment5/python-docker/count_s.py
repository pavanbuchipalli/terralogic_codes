
a="pavan"
d = {}.fromkeys(a,0)
for i in a:
     if i in a:
         d[i] += 1
     else:
         d[i]= 1
print(d)
