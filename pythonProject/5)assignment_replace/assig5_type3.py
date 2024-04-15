import re


def replace3(string):

    new_char = "z"
    replace_str = input("Provide a character to replace : - ")

    if replace_str in string :

        return " The string after replacing  new character is",  re.sub(replace_str, new_char, string)

    else:
        return "The Character '{}' you provided is not in the string  '{}' ".format(replace_str,string)






ss = replace3(input("provide a string : - "))
print(ss)