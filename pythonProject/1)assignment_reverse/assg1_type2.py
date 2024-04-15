def revesal2(main_string2):
    reverses = ""

    for i in main_string2:
        reverses = i + reverses

    return "Given sting is '{}'".format(main_string2), "revesed string is '{}'".format(reverses)


obj2 = revesal2(input("choose a string : -  "))
print(obj2)
