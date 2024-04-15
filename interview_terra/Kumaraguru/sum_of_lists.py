# list1= [1,2,3,4,5]
# list = [6,7,8,9,10]
# l1= sum(list1)
# l2= sum(list)
# print(l1,l2)
# print(l1+l2)
# v =0
# print(len(list1),len(list))
# for i in range(len(list1)):
#     v = v +list1[i]+list[i]
# print(v)
#
#
#
#
# v =6
# a  = [ 1,2,3,4,5,6,7]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==v:
#             print(a[i],a[j])



l = [1,2,3,4,5]
target = 6
l2 = []
for i in l:
    if (target - i) in l:
        l2.append([i, target - i])
    else:
        pass
print(l2)
l3 = []
for i in l:
    if ((target - i) in l) and ([target - i, i] not in l2) and ((target - i) != i):
        l3.append([i, target - i])
    else:
        pass
print(l3)