import random

target = random.randint(1, 100)

while True:
    userChoice = (input("guess the target or Quit(Q) : "))
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("success : Correct Guess!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number was too big. Take a smaller guess..")


print("____GAME OVER____")