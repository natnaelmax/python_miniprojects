print("Welcome to Natnaels quiz game:! ")
playing=input("Do You want to play? ").upper()
if playing != "YES":
    quit()
print("okay! let's begin :)")

score=0
answer=input("what does JVM stands for? ").upper()

if answer == "JAVA VIRTUAL MACHINE":
    print("correct!")
    score+=1
else:
    print("incorrect!")
answer =input("which is the simplest programming language to learn? ").upper()

if answer=="PYTHON":
    print("correct")
    score+=1

else:
    print("incorrect")

answer=input("in python to simplify repetitive variable what do u use?").lower()

if answer == "while":
    print("correct!")
    score+=1
else:
    print("Incorrect")

print(f"You have {score} questions correct")
print(f"You got {score/3 * 100}%.")
