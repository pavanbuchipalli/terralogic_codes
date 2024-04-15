def fib2(number):

    first = 0
    second  = 1

    for i in range(2,number+1):
        first,second =second,first+second
    print("The fibonacci value of {} is".format(number),second)



fib2(int(input("choose a number : - ")))
