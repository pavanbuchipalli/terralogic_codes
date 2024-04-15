list1 = [2,4,7,8,9,322,34,3,422,43,234,324,3242]
list2 = [9999,99,92,14,11,22,3,33,3333]
import itertools
c = list(itertools.chain(list1,list2))
print(c)
new_list= []
while c :
    min =c[0]
    for x in c:
        if x < min:
            min = x
    new_list.append(min)
    c.remove(min)

print(new_list)