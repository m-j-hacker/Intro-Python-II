from room import Room
from player import Player
from colorama import init, Fore, Back, Style
init()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

def get_room(cmd, current_room):
    # This function uses if statements
    if cmd == 'n':
        return current_room.n_to
    elif cmd == 's':
        return current_room.s_to
    elif cmd == 'w':
        return current_room.w_to
    elif cmd == 'e':
        return current_room.e_to
    else:
        return "Error: improper input (must be n, s, e, or w)"

def fetch_room(cmd, current_room):
    # This function uses concatenated strings
    moving = cmd + "_to"
    return getattr(current_room, moving)

acceptable_values = ('n','s','e','w','q')
# Make a new player object that is currently in the 'outside' room.
warrior = Player("Hacker", room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(Fore.CYAN + "\n" + warrior.room.name)
    print(Fore.WHITE + "\n" + warrior.room.description)
    prompt = input("\n\nWhich way do we go?\n" + Fore.GREEN + "(n e s w to move, q to quit) \n" + Fore.RED + "HP=100 MP=100" + Fore.RESET + " $> ")
    if prompt not in acceptable_values:
        print("Please type a valid command (n, e, s, w, or q)")
    elif prompt == 'q':
        print("Thank you for playing Lambda Quest!")
        break
    else:
        new_room = get_room(prompt, warrior.room)
        if new_room != None:
            warrior.change_room(new_room)
        else:
            print("\nYou can't go that way!!\n")
        # for key, value in room:
        #     if key.find(str(prompt + "_to")) and value != type(None):
        #         print("STARTED FROM THE BOTTOM NOW WE HEEEERE")
            
        # directions = current_room.__dict__.keys() 
        # for key in directions:
        #     if key.find("_to") > 0:
        #         global direction_to_go
        #         direction_to_go = str(prompt + "_to")
        # warrior.change_room(room[])