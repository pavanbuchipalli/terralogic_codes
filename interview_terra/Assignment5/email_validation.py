import re
def validemail():
    while True:
        email= input("Enter your email:----")
        permission= input("Select yes or no")
        if permission == "yes" :
            pattern = r"^[a-zA-Z0-9]+[a-zA-Z0-9]{7,20}\@[a-z]*\.[a-z]*"
            check =re.search(pattern,email)
            if check:
                print(check.group())
                files = open("validemail","a")
                files.write(check.group()+"\n")
            else:
                print("its is not valid email")

        else:
            files = open("validemail", "r")
            print(files.read())
            break
obj = validemail()

# pavanb1997@gmail.compavanbbb@gmail.comthippeswamy95655@gmail.compavanb1997@gmmm.compavanb1997@gmail.commpavanb1997@gmail.commpavanb188@gmail.compavanb188@gmail.com