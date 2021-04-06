def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()
    return new_function

@decorator
def initial_function():
    print("Initial Functionality")

initial_function()


# class AnotherWay:
#
#     def __init__(self, var):
#         ## calling the set_a() method to set the value 'a' by checking certain conditions
#         self.set_a(var)
#
#     ## getter method to get the properties using an object
#     def get_a(self):
#         return self.__a
#
#     ## setter method to change the value 'a' using an object
#     def set_a(self, var):
#         if var > 0 and var % 2 == 0:
#             self.__a = var
#
#         else:
#             self.__a = 2
#
#     a = property(get_a, set_a)
#
#
# ## creating an object for the 'AnotherWay' class
# obj = AnotherWay(28)
#
# print(obj.get_a())
