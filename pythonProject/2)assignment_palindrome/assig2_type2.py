def mani2(mainstring):
    # mainstring = "malayalam"
    reverse = ""
    for i in mainstring:
        reverse = i + reverse

    if reverse == mainstring:
        return "Given sting '{}'  is Palindrome".format(mainstring)
    else:
        return "Given String '{}'  is not palindrome".format(mainstring)


print(mani2(input("Choose a string :- ")))
