fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0]="love"
orange_and_mango = fruits[1:3] # it does not include the first index
k=fruits[0:3]
print(k)

does_exist = 'love' in fruits
print(does_exist)
fruits.append("Natnael")
fruits.append("Habtamu")
print(fruits)
fruits.insert(4,"My name is ")
print(fruits)
fruits.remove('lemon')
print(fruits)
fruits.pop(2)
print(fruits)
del fruits[0:3]
print(fruits)
list1 = [1,2,3,4,5]
list2 = [0]
list3 =[-5,-4,-3,-2,-1]
integer = list3 + list2 + list1
print(integer)
numu1= [1,2,3,4]
numu2= [-4,-3,-2,-1]
numu3 =[0]

numu2.extend(numu3)
numu2.extend(numu1)
print(numu2)

fruits1=["banana","Mango","Apple"]
vegetable=["Tomato","Potato","Cabbage"]
fruits1.extend(vegetable)
print("Fruit and Vegetable:",fruits1)
print(fruits1.count("banana"))
print(fruits1.index("Tomato"))
fruits1.reverse()
print(fruits1)

aba=[1,2,3,4]
aba.reverse()
print(aba)
lst=["item1","item2"]
lst.reverse()
print(lst)
fruits1 =["banana","apple","dog","c++"]
fruits1.sort()
print(fruits1)
fruits1.sort(reverse=True)
print(fruits1)
print(sorted(fruits1))

print(sorted("natnael"))

