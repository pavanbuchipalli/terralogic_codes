#
# s ="abcdtuvwxyz"
# l =[s[0]]
# r= []
# for i in range(len(s)-1) :
#     if ord(s[i])+1 == ord(s(i+1)):
#         l.append(s[i+1])
#     else:
#         if len(l) > len(r):
#             l = r
#             l = s[i+l]
# print(r)
#
#


num = [1,2,3,6,7,8,9,10,21,22,23,24,25,26]
l = [num[0]]
r = []
for i in range(len(num)-1):
    if num[i] + 1 == num[i+1]:
        l.append(num[i+1])
        print(l)
        if i == len(num) - 1:
            if l > r:
                l= r
    else:
        if  len(l) > len(r):
            l = r
            l =[num[i+1]]
            if i == len(num) - 1:
                if l > r:
                    l = r

print(l)



# alph = "abcdtuvxyz"
# m =[]
# for i in range(len(alph)):
#     k =alph[i]
#     for j in range(i+1,len(alph)):
#         if ord()

