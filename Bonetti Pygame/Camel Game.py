import random

print("Welcoe to camel! \nYou have stolen a camel to make your way across the great Mobi Desert. \nThe natives want thier camel back and are chasing you down! \nSurvive your  desert trek and outrun the natives. \n")

mile = 0
thirst = 0
camel = 0
natives = -20
initial_drinks = 3
check = 0

done = False

while done == False:
    print("A. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop for the night. \nE. Status check. \nQ. Quit.")
    choice = input("Your choice? ")
    if choice.upper()== "Q":
        done = True
    elif choice.upper() == "E":
        print("Miles traveled = {} \ndrinks in canteen = {} \nthe natives are {} miles back\n".format(mile, initial_drinks, natives))
    elif choice.upper() == "D":
        camel = 0
        print("The Camel is happy")
        natives += random.randrange(7,15)
    elif choice.upper() == "C":
        mile += random.randrange(10, 20)
        print("You traveled {} miles".format(mile))
        thirst += 1
        camel += random.randrange(1, 3)
        natives += random.randrange(7,15)
    elif choice.upper() == "B":
        mile += random.randrange(5, 12)
        print("You traveled {} miles".format(mile))
        thirst += 1
        camel += 1
        natives += random.randrange(7,15)
    elif choice.upper() == "A":
        if initial_drinks != 0:
            initial_drinks -= 1
            thirst = 0
        else:
            print("You don't have any more water")


    if thirst >= 4:
        print("You are thirsty")
    elif thirst > 6:
        print("You died of Thirst!")
        check = 1
        done = True
    if camel >= 5:
        print("Your camel is tired")
    elif camel > 8:
        print("Your camel is dead")
    if natives > mile:
        print("end the game, the natives caught up")
        check = 1
        done = True
    elif natives > mile - 15:
        print("the natives are getting close")
    if mile >= 200:
        check = -1
        done = True
    if random.randrange(1, 20) == 10:
        print("You found an Oasis!")
        thirst = 0
        camel = 0
        initial_drinks = 3

if check = -1:
    print("\nYou Won!")
elif check = 1:
    print("\nYou lost")
