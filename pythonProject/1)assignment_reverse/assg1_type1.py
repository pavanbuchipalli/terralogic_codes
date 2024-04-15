# type 1
def reveal(main_string):
    if len(main_string) <= 1:

        return main_string

    else:
        reversestring = main_string[::-1]

        return "Given sting is '{}'".format(main_string), "revesed string is '{}'".format(reversestring)


string = input("choose a string : -")
obj = reveal(string)
print(obj)
