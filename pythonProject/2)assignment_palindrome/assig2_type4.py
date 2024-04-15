def main4(stringg):
    # string = " pavan"
    reverse = ""
    new_string = stringg[::-1]
    for i in new_string:
        reverse = reverse + i

    if reverse == stringg:
        return " Given string '{}' is a palindrome".format(stringg)
    else:
        return " Given string '{}' is not  palindrome".format(stringg)


print(main4(input("Choose a String :- ")))
