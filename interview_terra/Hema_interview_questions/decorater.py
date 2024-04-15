# def car(model):
#     shade = "black"
#
#     def detalis():
#         print(model,shade)
#     detalis()
# car("my new car colour is")
#


# def printer():
#     print("this should be second line")
#
# def display(func):
#     def inner():
#         print("execute",func.__name__,"function")
#         func()
#         print("executed last line ")
#     return inner
#
# decoratord = display(printer)
# decoratord()
#
#



# iterators

values =[1,2,3]
numbers =iter(values)

item1 =next(numbers)
print(item1)

item2 =next(numbers)
print(item2)

item3 =next(numbers)
print(item3)

item4 =next(numbers)
print(item4)



# generators

