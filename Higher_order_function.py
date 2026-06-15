def square(x):
   return x**2
def cube(x):
   return x**3
def absolute(x):
   if x>=0:
      return x
   else:
      return -(x)
def higher_order_function(type):
   if type=="square":
      return square
   elif type=="cube":
      return cube
   else:
      return absolute
result=higher_order_function("square")
print(result(3))
result=higher_order_function("cube")
print(result(3))
result=higher_order_function("absolute")
print(result(-6))
# closure
def add_five():
   five=5
   def add(num):
      return five+num
   return add
closure=add_five()
print(closure(10))
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
map
numbers = [1, 2, 3, 4, 5] 
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))   

squares=map(lambda num:num**2,numbers)
print(list(squares))
names=["natnael","jacob","levi","lidet"]
def upper(name):
   return name.upper()
upper_case=map(upper,names)
print(list(upper_case))
# using lambda
uppers=map(lambda name:name.upper(),names)
print(list(uppers))
number_str=["1","2","3","4"]
number_int=map(int,number_str)
print(list(number_int))
# filter
number=[1,2,3,4,5,6]
def is_even(num):
   if num%2==0:
      return True
   return False
even=filter(is_even,number)
print(list(even))
name=["natnael","jacob","lensa","levi"]
def short_names(names):
   if len(names)<=5:
      return True
   return False
shortnames=filter(short_names,name)
print(list(shortnames))

countries=["Ethiopia","Switherland","ireland","canada","morocco","Netherland"]
def contain(name):
   if "land" in name:
      return True
   return False
contains_land=filter(contain,countries)
print(list(contains_land))
country=["Ethiopia","Switherland","ireland","canada","morocco","Netherland"]
def six_characters(char):
   if len(char)==6:
      return True
   return False
sixletter=filter(six_characters,country)
print(list(sixletter))