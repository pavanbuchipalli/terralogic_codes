def replace(stringg):

    replaced_by = "z"
    exsisting_char =input("Provide a character :-")
    new_str =""
    if exsisting_char in stringg :

        for i in stringg :
            if i == exsisting_char:
                i= replaced_by

            new_str = new_str + i
        return "The string after replacing  new character is   '{}' ".format(new_str)
    else:

        return "The Character '{}' you provided is not in the string  '{}' ".format(exsisting_char,stringg)




print(replace(input("Provide a string : - ")))