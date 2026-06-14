person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person))
print(person.get("first_name"))
person["personality"]="Ambivert"
print(person)
person['skills'].append("HTML")
print(person)
person['first_name']="Natnael"
person['last_name']="Habtamu"
print(person)
person.pop("first_name")
person.popitem()
print(person)

print(person.items)
a=person.keys()
print(a)
b=person.values()
print(b)