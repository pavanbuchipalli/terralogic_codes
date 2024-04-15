def char4(string4):
    no_duplicates = set(string4)
    print("Total length of the string is ", len(string4))
    for i in no_duplicates:
        count = 0
        for char in string4:
            if char == i:
                count += 1

        print("count of character {} in string is {}".format(i, count))


char4(input("Choose a string :- "))
