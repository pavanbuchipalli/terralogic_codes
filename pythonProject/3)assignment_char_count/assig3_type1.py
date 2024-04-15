def string1(chars):
    count_dict = {}

    length = len(chars)

    print("Total length of the string is ", len(chars))

    for i in chars:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] = count_dict[i] + 1

    return count_dict


print(string1(input("Choose a sting ")))
