room_list = []
current_room = 0
done = False

room = (["You just enter a dusty entry hall.\nPassages lead to the north and east.", 3, 2, None, None])
room_list.append(room)

room = (["You are in a large hall. It seems like not a lot people come here.\nThere are rooms to the north and west.", 2, None, None, 0])
room_list.append(room)

room = (["You are in an interior swimming pool. The smell of the water make you regret not having your swimsuit on. Maybe next time.\nThere are rooms off to the north and south.", 7, None, 1, None])
room_list.append(room)

room = (["You are in the dining room, doesn't seem like it's time for dinner.\nPassages lead to the north, south and west.", 6, None, 0, 4])
room_list.append(room)

room = (["You are in the kitchen, it looks like someone is hungry...\nThere is a room off to the east.", None, 3, None, None])
room_list.append(room)

room = (["You are in a bedroom. Maybe you could use some sleep.\nThere is a room off to the east.", None, 6, None, None])
room_list.append(room)

room = (["You just enter the gaming room. Anyone there to play pool wiht you?\nPassages lead to all directions. North, east, south and west.", 8, 7, 3, 5])
room_list.append(room)

room = (["You are in a torch-lit hallway, maybe be careful with all that.\nThere are rooms to the south and west.", None, None, 2, 6])
room_list.append(room)

room = (["Welcome to the garden, do not pick any flower.\nThere is a room to the south.", None, None, 6, None])
room_list.append(room)

while (done == False):
    print(room_list[current_room][0])
    print()
    command = str(input("What will you do?"))

    if ((command.lower() == "n") or (command.lower() == "north")):
        next_room = room_list[current_room][1]
        if (next_room == None):
            print("You can not go that way!")
        else: 
            current_room = next_room

    elif ((command.lower() == "e") or (command.lower() == "east")):
        next_room = room_list[current_room][2]
        if (next_room == None):
            print("You can not go that way!")
        else:
            current_room = next_room

    elif ((command.lower() == "s") or (command.lower() == "south")):
        next_room = room_list[current_room][3]
        if (next_room == None):
            print("You can not go that way!")
        else:
            current_room = next_room

    elif ((command.lower() == "w") or (command.lower() == "west")):
        next_room = room_list[current_room][4]
        if (next_room == None):
            print("You can not go that way!")
        else:
            current_room = next_room
            
    elif ((command.lower() == "q") or (command.lower() == "quit")):
        print("You have choose to close the game.")
        done = True
    else:
        print("Invalid output. Please try again...")
    