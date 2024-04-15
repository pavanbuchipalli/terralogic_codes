def replace(original):

    convert =list(original)
    place = []
    replacee = input("Provide a character to replace : - ")
    if replacee in original :
        for i in range(len(convert)-1):
            if convert[i] == replacee :
                place.append(i)


        for j in range(len(convert)):
            if j in place :
                convert[j] = "z"

        return " The string after replacing  new character is", "".join(str(convert))

    else:
        return "The Character '{}' you provided is not in the string  '{}' ".format(replacee,original)





ss = replace(input("provide a string : - "))
print(ss)