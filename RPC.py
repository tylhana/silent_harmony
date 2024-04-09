import random

print("Welcome to Rock, Paper, Scissors!")

game = 0
player = 0

player = int(input("Rock (1), Paper(2), Scissors(3)"))
game = random.randrange(1, 4)


if player == 1:
    if game == 1:
        print("Draw! You both chose rock.")
    elif game == 2:
        print("Lose! You chose rock and the computer chose paper.")
    else:
        print("Win! You chose rock and the computer chose scissors.")
elif player == 2:
    if game == 1:
        print("Win! You chose paper and the computer chose rock.")
    elif game == 2:
        print("Draw! You both chose paper.")
    else:
        print("Lose! You chose paper and the computer chose scissors.")
elif player == 3:
    if game == 1:
        print("Lose! You chose scissors and the computer chose rock.")
    elif game == 2:
        print("Win! You chose scissors and the computer chose paper.")
    else:
        print("Draw! You both chose scissors.")
else:
    print("ERROR. Invalid input.")