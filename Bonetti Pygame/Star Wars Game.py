import random
import pygame

pygame.init()

print("Welcome to Star Wars! \nYou have stolen a spaceship to make your way across the Outer Rim. \nThe Imperials want thier spaceship back and are chasing you down! \nSurvive your space trek and outrun the Imperials. \n")

mile = 0
thirst = 0
camel = 0
natives = -20
initial_drinks = 3
check = 0

done = False

while done == False:
    print("A. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop for refeuling. \nE. Status check. \nQ. Quit.")
    choice = input("Your choice? ")
    if choice.upper()== "Q":
        done = True
    elif choice.upper() == "E":
        print("Cliks traveled = {} \ndrinks in canteen = {} \nthe Imperials are {} clicks back\n".format(mile, initial_drinks, natives))
    elif choice.upper() == "D":
        camel = 0
        print("Your tank is full!")
        natives += random.randrange(7,15)
    elif choice.upper() == "C":
        mile += random.randrange(10, 20)
        print("You traveled {} clicks".format(mile))
        thirst += 1
        camel += random.randrange(1, 3)
        natives += random.randrange(7,15)
    elif choice.upper() == "B":
        mile += random.randrange(5, 12)
        print("You traveled {} clicks".format(mile))
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
        print("You're running out of fuel is tired")
    elif camel > 8:
        print("You ran out of fuel!")
    if natives > mile:
        print("End of the game, the Imperials caught up")
        check = 1
        done = True
    elif natives > mile - 15:
        print("the Imperials are getting close")
    if mile >= 200:
        check = -1
        done = True
    if random.randrange(1, 20) == 10:
        print("You found a Planet!")
        thirst = 0
        camel = 0
        initial_drinks = 3

if check == -1:
    print("\nYou Won!")
elif check == 1:
    print("\nYou lost")
