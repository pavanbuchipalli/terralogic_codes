def reversal4(main_string4):
    reverse = ""
    for i in range(len(main_string4)):
        operation = main_string4[len(main_string4) - i - 1]
        reverse = reverse + operation
    return "Given sting is '{}'".format(main_string4), "reversed string is '{}' ".format(reverse)


obj4 = reversal4(input("choose a string: - "))
print(obj4)
