Number = int(input("give a number :- "))
Flag = 0
for i in range(2,Number):
    if Number%i==0:
        Flag =1


if Flag==0:
    print("{} is a prime_number ".format(Number))
else:
    print("{} is not a prime_number".format(Number))