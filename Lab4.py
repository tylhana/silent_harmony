import random

print("Welcome to Itomori!")
print("You have stolen a boat to escape this island, and regain the mainland.")
print("The locals want their boat back, and are chasing you down! Survive your journey, and out run the locals.")
print()

# Game Variables

done = False
player = 0
thirst = 0
boat = 0
locals =  -20
oil = 5
drink = 5

while (done == False):
    # Game Instruction
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and and fill up the tank.")
    print("E. Status Check.")
    print("Q. Quit.")
    print()

    command = str(input("Your choice?"))
    command = command.lower()
    print()

# Input Handling

    if ((command == "q") or (command == "quit")):
        print("You chose to close the game.")
        done = True

    elif (command == "e"):
        print("Kilometers travel: ", player)
        print("Drinks in canteen: ", drink)
        print("Oil bidons available: ", oil)
        print("The locals are", locals, "km behind you.")
        print()

    elif (command == "d"):
        if (oil > 1):
            oil -= 1
            boat = 0
            print("You have fill up the tank. Ready to go full blast.")
            locals += random.randrange(7,15)
        else:
            print("ERROR. Not enough ressources.")
        print()

    elif (command == "c"):
        add_km += random.randrange(10, 21)
        player += add_km
        locals += random.randrange(7, 15)
        boat += random.randrange(1, 4)
        thirst += 1
        print("You have traveled", add_km, "km.")
        print(player, " km in total.")
        print()

    elif (command == "b"):
        add_km = random.randint(5, 12)
        player += add_km
        locals += random.randrange(7, 15)
        boat += 1
        thirst += 1
        print("You have traveled", add_km, " km.") 
        print(player," km in total.")
        print()

    elif (command == "a"):
        if (drink > 0):
            drink -= 1
            thirst = 0
            print("You take a sip from your canteen. Your thirst is quenched.")
        else:
            print("ERROR: Not enough ressources.")
        print()
    else:
        print("ERROR: Invalid input! Please input a functional key.")

# Game Win Check
    if((player >= 200) and (done == False)):
        print("Congratulations! You have reached the mainland and outran the locals.")
        done == True

# Condition Handling
    if ((thirst >= 4) and (thirst <= 6) and (done == False)):
        print("You're thirsty.")
    elif ((thirst > 6) and (done == False)):
        print("GAME OVER \n You died of thirst!")
        done = True

    if ((boat >=5) and (boat <= 8) and (done == False)):
        print("Oil's level is low, the tank would appreciate to be fill up.")
    elif ((boat > 8) and ( done == False)):
        print("GAME OVER \n Your boat can't move anymore!")
        done = True

    if (((player - locals) <= 15) and ((player - locals) > 0) and (done == False)):
        print("The locals are getting close.")
    elif ((player <= locals) and (done == False)):
        print("GAME OVER \n Locals have caught you!")
        done = True

# Random events