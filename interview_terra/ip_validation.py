import re
a =["122.121.32.0","522.121.32.0","122.121.322.0"]
for i in a:

    c = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",i).group()
    # print(c)
    ipr = c.split(".")
    for i in ipr:
        if int(i) < 0 and int(i) > 255:
            print("no")
        else:
            print(ipr)