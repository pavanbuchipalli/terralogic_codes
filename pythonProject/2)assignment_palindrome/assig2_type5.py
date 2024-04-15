def manin(stringg):
    reverse = ""
    for i in range(len(stringg) - 1, -1, -1):
        reverse = reverse + stringg[i]

    if reverse == stringg:
        return "Given  string  '{}' is Palindrome ".format(stringg)

    else:
        return "Given String  '{}' is not palindrome ".format(stringg)


ss = manin(input("choose a string : -"))
print(ss)
