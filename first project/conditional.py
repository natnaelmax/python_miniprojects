
a=0
if a >=0 and a%2 ==0:
    print("A is positive")
elif a<0:
    print("A is negative")    
else:
    print("A is zero")    

usero="nathan"
access_level=4
if usero=="james"or access_level>=5:
    print("Access granted")
else:
    print("Access Denied")

user =int(input("Enter your age:"))
print(user)
if user > 18:
    print("you are old enough to learn to drive.")
else:    
    print(f"You need{18-user} more years to learn to drive")

   
user =int(input("Enter your age: "))

if user > 18:
    print("You are old enough to learn to drive.")
else:    
    print(f"You need {18-user} more years to learn to drive")

my_age=19
your_age=int(input("Enter ur age: "))

if your_age>my_age:
    difference=your_age - my_age
    if difference==1:
        print(f"You are {difference} year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age==my_age:
    print("We are the same age")  
else:
    difference = my_age - your_age
    if difference==1:
        print(f"I am {difference} year older than you.")
    else:    
        print(f"I am {difference} years older than you.")


first_number=int(input("Enter Number one: "))
second_number=int(input("Enter nuber two:"))

if first_number > second_number :
    print(f"{first_number} is greater than {second_number}")

elif first_number < second_number:
    print(f"{first_number} is less than {second_number}")
else:
    print(f"{first_number} is equal to {second number}")    