lan =("a","b","c",'d')
print(len(lan))
print(lan[0:3])
print(lan[1:3])
print(lan[-1:])

coding=("python","html","c++","c")
programming=("code","maintain","feasible")
coding =list(coding)
coding[1]="Java"
coding =tuple(coding)
print("new tuple:",coding)

print("Java" in coding)

al= coding + programming
print("JOINING TUPLE:",al)
del lan
