s = "abcdabmnmnqrsabcdefg"
g = ""
new = ""
for i in range(len(s)-1):
    if s[i] not in g:
        g = g+s[i]
        if i == len(s)-1:
            if g > new:
                new= g
    else:
        if g > new:
            new= g
            g = s[i]
        else:
            g = s[i]
print(new)
print(g)



str = "abcdabmnmnqrsabcdefg"
le = len(str)
op = ""
new = ""
for i in range(len(str) - 1):
    if str[i] not in op :
        op = op + str[i]
        if i == len(str) - 1:
            if op > new:
               new = op
    else:
        if op > new:
           new = op
           op = str[i]
        else:
            op = str[i]


print(new)
print(op)

