# type 1
# a = [1,10,11,12,14,1,17]
# n = max(a)
# for i in range(1,n):
#     if i not in a:
#         print(i)

# type2
# def findMissingNumbers(n):
#     numbers = set(n)
#     length = len(n)
#     output = []
#     for i in range(1, n[-1]):
#         if i not in numbers:
#             output.append(i)
#     return output
#
#
# listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
# print(findMissingNumbers(listOfNumbers))

# trpe 3
a =[1,-10,11,12,14,17]
mi = 0
ma = 0
for i in a:
    if i < mi :
        mi = i
    elif i > ma :
        ma = i

print(mi,ma)
for i in  range(1,ma+1):
    if i not in a:
        print(i)




