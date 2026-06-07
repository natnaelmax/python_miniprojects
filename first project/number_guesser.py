import random
top_number=input("type a number:")
if top_number.isdigit():
    top_number=int(top_number)
    if top_number<=0:
        print("Enter number greater than 0 next time.")
        quit()
else:
    print("enter a number next time")
    quit()
random_number=random.randint(0,top_number)

guesses=0
while True: 
    guesses+=1
    user_guess=input("Guess a number: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Enter a number next time.")
        continue
    if user_guess==random_number:
        print("You guessed right")
        break
    elif user_guess>random_number:
            print("You guessed above the number")
    else:
            print("You guessed below the number")    


print(f"You have got in {guesses} guesses")
