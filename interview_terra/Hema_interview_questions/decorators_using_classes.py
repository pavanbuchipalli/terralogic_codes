# # class main():
# #
# #     def __int__(self,a,b):
# #         self.a = a
# #         self.b = b
# #     def addition(self):
# #         return self.a * self.b
# #
# #     def multiplication(self):
# #         return
#
#
#
# class MyClass:
#     def my_decorator(method):
#         def wrapper(self, *args, **kwargs):
#             # Perform some actions before the method call (if needed)
#             print("Decorator: Before method execution")
#
#             # Call the original method
#             result = method(self, *args, **kwargs)
#
#             # Perform some actions after the method call (if needed)
#             print("Decorator: After method execution")
#
#             return result
#
#         return wrapper
#
#     @my_decorator
#     def my_method(self, arg1, arg2):
#         # Method logic goes here
#         print(f"My method called with {arg1} and {arg2}")
#
# # Usage:
# obj = MyClass()
# obj.my_method(10, 20)




# def check_name(method):
#     def inner(name_ref):
#         if name_ref.name == "pavan":
#             print("names are similar")
#         else:
#             method(name_ref)
#     return inner
# class printing():
#     def __init__(self,name):
#         self.name = name
#     @check_name
#     def print_name(self):
#         print("entered username is :",self.name)
#
# p = printing("pavan")
# p.print_name()



class decorator:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        str1 = self.func()
        return str1.upper()

@decorator
def greet():
    return 'good morning'
print(greet())


class div:
    def __init__(self,func):
        self.func = func
    def __call__(self, a,b):
        if b == 0:
            a,b= b,a
            return (a,b)

            # return self.func(a, b)
        else:
            return self.func(a,b)


@div
def division(a,b):
    return a/b
print(division(10,5))