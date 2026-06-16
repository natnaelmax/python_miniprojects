import random
import time
Operator=["+","-","*"]
minimum=3
maximum=12
Total_Problems=4

def generate_problem():
    left=random.randint(minimum,maximum)
    right=random.randint(minimum,maximum)
    operator=random.choice(Operator)

    expr=  str(left) + " " + operator + " " + str(right)
    answer=eval(expr)
    return expr,answer
wrong=0
input("Are u ready to start!")
print("-------------------")
start_time=time.time()
for i in range(Total_Problems):
    expr,answer=generate_problem()
    while True:
       guess=input("Problem No"+ str(i+1)+" : " + expr + '=')
       if guess==str(answer):
           break
       wrong+=1
end_time=time.time()
total_time=round(end_time-start_time,1)
print("----------------")
print("U HAVE FINISHED IN",total_time,"seconds")     


