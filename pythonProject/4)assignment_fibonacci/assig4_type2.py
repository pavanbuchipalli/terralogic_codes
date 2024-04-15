def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib (number - 2)


number = int(input("provide a number :- "))
print("The fibonacci value of {} is ".format(number),fib(number))