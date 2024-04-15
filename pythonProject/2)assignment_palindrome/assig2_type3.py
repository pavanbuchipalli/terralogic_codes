def main3(main_string):
    length = len(main_string) // 2
    m = -1
    flag = True
    for i in range(length):
        if main_string[i] != main_string[m]:
            flag = False
        m = m - 1
    if flag:
        print(" Given string '{}' is a palindrome".format(main_string))
    else:
        print("Given String '{}' is not palindrome".format(main_string))


main3(input("Choose a string : - "))
