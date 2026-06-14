def person(name,**kmap):
    print("name ",name)
    for i,j in kmap.items():
        print(i, " : ", j)       

person(name ="nati",age=19,loc="adama",code="python") 
