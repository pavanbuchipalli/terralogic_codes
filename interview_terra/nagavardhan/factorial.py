# def recur(n):
#     if n == 0:
#         return 1
#     elif n != 0:
#         return n * recur(n - 1)
#
#
# obj = recur(1)
# print(obj)


NUMBER  = int(input("provide a number -:"))

factorial_ = 1
while NUMBER >0:
    factorial_ = factorial_ * NUMBER
    NUMBER = NUMBER -1
print(factorial_)