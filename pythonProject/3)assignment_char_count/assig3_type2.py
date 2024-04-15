def countt(chars):

    count = {}.fromkeys(chars, 0)

    print("Total lenght of the string is ",len(chars))
    for char in chars :
        if char in count:
            count[char]  += 1
    return (count)

print(countt(input("provide  a string : - ")))