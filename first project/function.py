


from operator import mul


def generate_fullname():
    first_name="Natnael"
    space= " "
    last_name="John"
    full_name=first_name+space+last_name
    return full_name
print(generate_fullname())

def add():
    num1=4
    num2=3
    ad=num1+num2
    return ad
print(add())
# single parameter
def greeting (name):
    message = name+ ",welcome to python"
    return(message)
print(greeting("Natnael"))

def area_of_circle(r):
    pi=3.14
    area=pi*r*r
    return(area)
print(area_of_circle(3))
def multiply(num1,num2):
    multi=num1*num2
    return(multi)
print("multiplication of 2 number is ",multiply(4,5))

def is_even(n):
    if n%2==0:
        return True
    return False
print(is_even(11))
print(is_even(10))
def add_twelve(num):
    add=num+12
    return(add)
print("the sum of these number is ",add_twelve(10))
# two parameters
def generate_full_name(first_name,last_name):
    full_name=first_name+" "+last_name
    return(full_name)
print(generate_full_name("Natnael","Habtamu"))

def weight_of_object(mass,gravity):
    weight=str(mass*gravity)+ "N"
    return(weight)
print("Weight of the object in newton ",weight_of_object(70,9.8))
# Function with default parameter
def greeting(name="Natnael"):
    message= name + "Welcome to Python"
    return(message)
print(greeting())
print(greeting("JOHN "))

# hiding ur password
from getpass import getpass
user=input("Enter ur nmae: ")
password=getpass("Enter ur password: ")
print(password)