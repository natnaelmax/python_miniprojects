# def square(x):
#    return x**2
# def cube(x):
#    return x**3
# def absolute(x):
#    if x>=0:
#       return x
#    else:
#       return -(x)
# def higher_order_function(type):
#    if type=="square":
#       return square
#    elif type=="cube":
#       return cube
#    else:
#       return absolute
# result=higher_order_function("square")
# print(result(3))
# result=higher_order_function("cube")
# print(result(3))
# result=higher_order_function("absolute")
# print(result(-6))
# # closure
# def add_five():
#    five=5
#    def add(num):
#       return five+num
#    return add
# closure=add_five()
# print(closure(10))
# decorator
def greeting():
   return "welcome to python"
def decorator_uppercase(function):
   def wrapper():
      func=function()
      make_uppercase=func.upper()
      return make_uppercase
   return wrapper
res=decorator_uppercase(greeting)
print(res())

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON