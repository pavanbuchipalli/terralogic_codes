import re
def Test5(string5):

    l = []
    print("Total length of the string is ", len(string5))
    for i in set(string5):

        count = len(re.findall(i,string5))
        if i not in l :
            l.append([i,count])

    return l

print(Test5(input("choose a string : -")))