def string3(char3):
    print("Total lenght of the string is ", len(char3))

    char_count = {i: char3.count(i) for i in set(char3)}

    return char_count


print(string3(input("choose a string : - ")))
