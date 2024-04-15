a = [1,3,5,7,11,15]
ma = 0
for i in a:
    if i > ma:
        ma = i
# print(ma)
for i in range(1,ma+1,2):
    if i not in a:
        print(i)