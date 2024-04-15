def replacee(original):
    char_replace = input("Provide a character to replace : - ")
    replaced = "z"
    if char_replace in original:
        for i in original:
            if i == char_replace:

                new_string = original.replace(i, replaced)


        return "The string after replacing  new character is" ,new_string

    else:
        return "The Character '{}' you provided is not in the string  '{}' ".format(char_replace, original)


print(replacee(input("provide a string : - ")))
