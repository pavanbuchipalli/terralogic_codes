def reversal(main_string3):
    reverse = "".join(reversed(main_string3))

    return "Given sting is '{}'".format(main_string3), "revesed string is '{}' ".format(reverse)


obj3 = reversal(input("choose a string : -"))
print(obj3)
