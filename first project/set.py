lang ={"dog","cat","hyena","lion"}
print(len(lang))
lang.add("banana")
print(lang)
lang.update(["king","Queen","Start up"])
print(lang)

fam={}
print(type(fam))
famu={1,2,3,4}
print(5 in famu)
famu.remove(4)
print(famu)
famu.pop()
print(famu)
b=famu.pop()
print(b)
lang =list(lang)
print(lang)
lang = set(lang)
print(lang)

a={1,2,3}
b={4,5,6}
print(a.union(b))
a.update(b)
print(a)

whole_numbers ={1,2,3,4,5,6,7,8}
even_numbers= {2,4,6,8}
print(whole_numbers.intersection(even_numbers))
print(whole_numbers.issuperset(even_numbers))
print(whole_numbers.difference(even_numbers))
print(even_numbers.difference(whole_numbers))

print(whole_numbers.symmetric_difference(even_numbers))
print(whole_numbers.isdisjoint(even_numbers))


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.update(B)
print(A)
B.update(A)
print(B)

age=list(age)
print(age)
print(len(age))

age=set(age)
print(age)
print(len(age))