a=10
def some():
    a=15
    globals()['a']=25 # we can change the value global variable using the function globals[]
    print("inside: ", a)
some()
print("outside: ", a)    