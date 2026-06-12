# lst=[i for i  in "language"]
# print(lst)
# squares=[i*i for i in range(11)]
# print(squares)
# multipl=[i*8 for i in range(11) if i%2==0 ]
# print(multipl)
# number=[-6,-5,-4,-3,0,1,2,3,4]
# positive_evennumbers=[i for i in number if i%2==0 and i>0]
# negative_evennumbers=[i for i in number if i%2==0 and i<0]
# print(positive_evennumbers)
# print(negative_evennumbers)
# # Lambda function
# print((lambda num1,num2:num1+num2)(45,43))
# square=lambda x:x**2
# print(square(9))
# multi=lambda x,y,z:x**2 + y -z*3
# print(multi(4,3,2))





numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers=[i for i in numbers if i<0]
print(negative_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = [x for sublist in list_of_lists for x in sublist]
print(result)

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)


y_intercept = lambda x1, y1, x2, y2: y1 - ((y2 - y1) / (x2 - x1)) * x1

# Full equation string
linear_eq = lambda x1, y1, x2, y2: (
    f"y = {(y2-y1)/(x2-x1)}x + {y1 - ((y2-y1)/(x2-x1)) * x1}"
)
x1, y1, x2, y2 = 1, 3, 4, 9

print(slope(x1, y1, x2, y2))        
print(y_intercept(x1, y1, x2, y2))  
print(linear_eq(x1, y1, x2, y2))    