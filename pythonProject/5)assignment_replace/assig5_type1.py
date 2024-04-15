def replacee(string1):
    char = input("choose a char : - ")
    if char in string1:
        new_string =string1.replace(char,"Z")
        return "The string after replacing  new character is   '{}' ".format(new_string)
    else:
        return "The Character {} you provided is not in the string".format(char)


print(replacee(input("Provide a String : -")))


