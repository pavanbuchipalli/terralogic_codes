# # def star(func):
# #     def wrapper():
# #         print("**************")
# #         func()
# #         print("**************")
# #
# #     return wrapper
# #
# #
# # def dash(func):
# #     def wrapper():
# #         print("---------------")
# #         func()
# #         print("---------------")
# #
# #     return wrapper
# #
# #
# # @star
# # @dash
# # def note():
# #     print("welcome")
# #
# #
# # note()
# def addtion(a):
#
#     def multiplication(b=6):
#         print(a*b)
#     return multiplication
# obj=addtion(5)
# obj()
# #
# # def custom_decorator(arg1, arg2):
# #     def decorator_function(original_function):
# #         def wrapper_function(*args, **kwargs):
# #             # Custom logic using the arguments
# #             print(f"Decorator arguments: {arg1}, {arg2}")
# #             result = original_function(*args, **kwargs)
# #             # You can add more functionality here if needed
# #             return result
# #
# #         return wrapper_function
# #
# #     return decorator_function
# #
# # # Usage of the decorator with arguments
# # @custom_decorator(6, 5)
# # def my_function(arg):
# #     print(f"My function is called with argument: {arg}")
# #
# # # Call the decorated function
# # my_function(5)








def decor1(func):
    def wrapper():
        x = func()
        print("the multiplication in decorator 2 is {} * {} =".format(x, x), x * x)
        return x * x

    return wrapper


def decor(func):
    def wrapper():
        x = func()
        print("the addition at decorator 1 is 2 + {} =".format(x), 2 + x)
        return 2 + x

    return wrapper


@decor1
@decor
def num():
    return 10

num()
