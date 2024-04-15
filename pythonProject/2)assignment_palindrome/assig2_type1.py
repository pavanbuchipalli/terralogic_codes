def main(main_string):
    reverse = main_string[::-1]
    if main_string == reverse:
        return "Given sting  '{}'  is palindrome".format(main_string)
    else:
        return "Given string  '{}' is not palindrome".format(main_string)


print(main(input("Choose a string :- ")))

