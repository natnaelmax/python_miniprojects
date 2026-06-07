from cryptography.fernet import Fernet
master_password=input("what is ur master password: ")


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("User: ",user ,"Password: ",passw)



def add():
    name=input("Name: ")
    password=input("password: ")
    with open('password.txt','a') as f:
        f.write(name + "|" + password +"\n")



while True:
    mode=input("Would u like to add a new password or view existing one(add,view), press q to quit? ").lower()

    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
      
    else:
        print("invalid mode")
        continue


    print("heyy")