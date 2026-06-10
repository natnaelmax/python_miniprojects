from multiprocessing import Value


data = ["nathan ", 12, "bona", "discrete"]
for i in range(10):
    if i==5:
        break
    print(i)
evens=odds=0
for n in range(101):
    if n%2==0:
        evens+=n
     
    else:
        odds+=n
print(f"the sum of even number is {evens} And the sum of odd number is{odds}")

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])


person = {
    'first_name':'Nathan',
    'last_name':'habtam',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)
for key,value in person.items():
    print(key,value)    
for key in person:
    if key=="skills":
        for skill in person['skills']:
            print(skill)
lst=list(range(11))
print(lst)
st=set(range(11))
print(st)
even_list=list(range(0,10,2))
print(even_list)    