def manin(stringg):
    reverse = ""
    for i in range(len(stringg) - 1, -1, -1):
        reverse = reverse + stringg[i]

    return "original string is '{}' and reverse string is  '{}' ".format(stringg, reverse)


ss = manin(input("choose a string : -"))
print(ss)
