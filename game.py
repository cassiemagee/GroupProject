#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
timeforfood = True
friendswithsisters = False
enemywithsisters = False
taxesproblem = False



def list_of_items(items):
    
    #create a list
    items_name = []
    
    #add all the items in the list
    for i in items:
        items_name.append(i["name"])
        
    return items_name
             
    pass




def print_room_items(room):
    
    #First check if there are items in the room. To prevent None print or error
    if len(list_of_items(room["items"])) != 0:
        #print all available items in the room
        print("There is " , list_of_items(room["items"]) , " here.")
    
    
    pass




def print_inventory_items(items):
    
    #Check if the player has inventory items.
    if len(items) != 0:
        #Print all available inventory items.
        print("You have " , list_of_items(items) , ".")
    
    
    
    pass




def print_room(room):

    # Display room name
    print("___________________________________________________________________")
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display available items in room
    print_room_items(room)



       

def exit_leads_to(exits, direction):
    
    return rooms[exits[direction]]["name"]




def print_exit(direction, leads_to):
    
    print("GO " + direction.upper() + " to " + leads_to + ".")




def print_menu(exits, room_items, inv_items):
    
    print("")
    print("You can:")
    
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    
    #Print what the player can take from the room. First "id" and then the "name"
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take ", item["name"])
    
    #Print what the player can drop from the player's inventory
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop ", item["name"])
    

    print("")
    print("What do you want to do?")




def is_valid_exit(exits, chosen_exit):
    
    return chosen_exit in exits




def execute_go(direction):
    
    #we want to modify the global version of current_room. (Functions are private)
    global current_room
    
    #Check if the input is a valid exit from the current_room
    if is_valid_exit(current_room["exits"], direction):
        #move to the new room
        current_room = move(current_room["exits"], direction)
    else:
        #if something else is written,in other words..not valid exit
        print("")
        print("You cannot go there." )
        print("")
   
    pass



def execute_take(item_id):
    
    #create a boolean to check if item is available/exists
    item_exists = False
    
    #Compare the input with the items in the room. if it exists take the item
    for item in current_room["items"]:
        if item_id == item["id"]:
            item_exists = True
            current_room["items"].remove(item)
            inventory.append(item)
            print(item["name"] + " added to inventory.")
    #If the input item doesn't exist then: 
    if not item_exists:
        print("You cannot take that.")
        
        
    pass
    


def execute_drop(item_id):
    
    #create a boolean to check if item is available/exists
    item_exists = False
    
    #Compare the input with the items in the inventory. if it exists drop the item
    for item in inventory:
        if item_id == item["id"]:
            item_exists = True
            inventory.remove(item)
            current_room["items"].append(item)
            print(item["name"] + " removed from inventory.")
    #If the input item doesn't exist then:
    if not item_exists:
        print("You cannot drop that.")
    
    pass

    

def execute_command(command):
    

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")



def menu(exits, room_items, inv_items):
    
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input




def move(exits, direction):
    
    # Next room to go to
    return rooms[exits[direction]]




# This is the entry point of our program

def intro():

    print("")
    print("INTRO:")
    print("")

    print("""
The first night's the toughest.
No doubt about it.
They march you in naked as the day you were born,
skin burning and half-blind from that delousing shit.
And when they put you in that cell and those bars slam home,
that's when you know it's for real.
Old life blown away
in the blink of an eye """ )



def teamupwithsisters():

    global friendswithsisters

    friendswithsisters = True

    print("___________________________________________________________________")
    print("")
    print("The Sisters:")
    print("")
    print("Perfect! Welcome to our Team")
    print("Just a heads up....a Riot is about to happen")
    print("When we start, join the the Riot or we won't be happy")
    print("If you need a weapon go to Red....he's found at the Yard")
    print("See you later")
    print("")
    print("You:")
    print("")
    print("Stand up and leave from the table")

    pass


def avoidsisters():

    global enemywithsisters

    global timeforfood

    timeforfood = False
    enemywithsisters = True

    
    print("___________________________________________________________________")
    print("""

The Sisters:

"Hard to get.

I like that."


You:

Stand up and leave from the table

""")


    pass
    


def introduceyourself():

    print("___________________________________________________________________")
    print("")
    print("You:")
    print("""
Hi, I'm Andy Dufresne.
Wife-killing banker.

Inmate:

Why'd you do it?

You:

I didn't, since you ask.

Inmate:

You're going to fit right in.
Everybody in here's innocent
 """)

    print("")
    print("Type 1 to ask about how to get things into the prison ")
    print("Type 2 to ask about the sisters")
    print("")

    user_input = input("Enter option: ")

    while True:
        if user_input == "1":

            print("___________________________________________________________________")
            print("")
            print("""
"Red is the guy who can get it for you.
Cigarettes, a bag of reefer,
if that's your thing...
...bottle of brandy to celebrate
your kid's high school graduation.
Damn near anything within reason."

""")
            
            
            break
        elif user_input == "2":

            
            
            break
        else:
            print("")
            print("You cannot do that.")
            print("")
            print("")
            choosetable()

    
    

    


def table2():

    print("___________________________________________________________________")
    print("")
    print("""
You sit at Table 2.
You overhear two inmates talking about buying cigars  across from you.
""")
    print("")
    print("Type 1 to introduce yourself")
    print("Type 2 to keep to yourself.")
    print("")

    user_input = input("Enter option: ")

    while True:
        if user_input == "1":

            introduceyourself()
            
            break
        elif user_input == "2":

            avoidloudtable()
            
            break
        else:
            print("")
            print("You cannot do that.")
            print("")
            print("")
            choosetable()
    



def table1():
    
    print("___________________________________________________________________")
    print("")
    print("")
    print("You sit down at table 1. Immediately two men in the late twenties start talking to you")
    print("")
    print("The Sisters:")
    print("""
"Why hello there"
suddenly every eye turns to you as you look up from your plate.

"You can call us the sisters, what is it you do fish?"
Two young men who seemed to be in charge are giving you their full attention.

You:

"My name is Andy, I used to be an account." 
Most of the table seemed to have  lost interest already,
but the Sisters carry on.

The Sisters:

''Anybody come at you yet?
Anybody get to you yet?
Hey, we all need friends in here.
I could be a friend to you."

""")

    print("Type 1 to Keep to yourself?")
    print("")
    print("Type 2 to team up with the sisters")
    print("")
    
    user_input = input("Enter choice: ")

      
    while True:
        if user_input == "1":

            avoidsisters()
            
            break
        elif user_input == "2":

            teamupwithsisters()
            
            break
        else:
            print("")
            print("You cannot do that.")
            print("")
            print("")
            choosetable()
            
    
pass

    





def choosetable():

    print("")
    print("Type 1 to sit at the loud table")
    print("")
    print("Type 2 to sit at the quieter table")
    print("")

    user_input = input("Where do you want to sit? ")

    while True:
        if user_input == "1":
            table1()
            break
        elif user_input == "2":
            table2()
            break
        else:
            print("")
            print("You cannot go there.")
            print("")
            print("")
            choosetable()
        




def lunchtime():
    
    print("___________________________________________________________________")
    print("")
    print("Cafeteria:")
    print("")
    print("""
You make your way inside the canteen,
grab a tray of food and take a look around.
You see there is a seat free on two tables.
One table is loud and full of young men arguing aggressively,
the other is more quiet and seems to be home
to the older generations of the prison.
""")

    choosetable()
    
    

def main():

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        if current_room["name"] == "Cafeteria":
            if timeforfood == True:
                lunchtime()



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    intro()
    main()

