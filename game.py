#!/usr/bin/python3
import time
from map import rooms
from player import *
from items import *
from gameparser import *
timeforfood = True
friendswithsisters = False
enemywithsisters = False
taxesproblem = False
knowchess = False
knowred = False
talkedtored = False
first_office = True



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


def execute_take_hammer(item_id):
    
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



def execute_restart():
    if len(inventory) != 0:
        for item in inventory:
            inventory.remove(item)
            
    global current_room
    current_room = rooms["Cell"]

    global timeforfood
    global friendswithsisters
    global enemywithsisters
    global taxesproblem
    global knowchess
    global knowred
    global talkedtored
            
    timeforfood = True
    friendswithsisters = False
    enemywithsisters = False
    taxesproblem = False
    knowchess = False
    knowred = False
    talkedtored = False

    main()


    

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


    elif command[0] == "restart":
        execute_restart()



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

    print("")
    



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

    global knowred

    knowred = True

    
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
    


def inmatesfurtherquestions():

    print("")
    print("Type 1 : Where can I find him?")
    print("Type 2 : Ask about how much it costs")
    print("")

    

    while True:
        user_input = input("Enter option:").lower()

        if user_input == "1":

            print("___________________________________________________________________")
            print("")
            print("Inmate:")
            print("Try out in the yard during outdoor time.")
            print("")
            print("You:")
            print("Stand up and leave the table")

            break
            
        elif user_input == "2":

            print("___________________________________________________________________")
            print("")
            print("Inmate:")
            print("""
They talk about the current economy of the prison,
and how even the guards and the warden are getting ripped off by tax.
""")
            print("Stand up and leave the table")

            break

        else:
            print("You cannot do that.")




def introduceyourself():

    print("___________________________________________________________________")
    print("")
    print("You:")
    print("""
Hi, I'm Andy Dufresne.
Wife-killing accountant.

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

    

    while True:
        user_input = input("Enter option: ").lower()
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
            global knowred
            knowred = True
            inmatesfurtherquestions()                    
            
            
            break
        
        elif user_input == "2":

            print("___________________________________________________________________")
            print("")
            print("Inmate:")
            print("""
"The sisters?" The table goes quiet. 
"You be careful around those two."
""")

            print("You:")
            print("Stand up and leave the table")

            
            
            break
        else:
            print("")
            print("You cannot do that.")
            print("")
            print("")
            



def avoidloudtable():

    print("___________________________________________________________________")
    print("")
    print("""
Nothing more of note is spoken about,
other than the Warden's apparent love for chess.
""")
    global knowchess

    knowchess = True
    
    print("You:")
    print("Stand up and leave the table")
        
    
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

    

    while True:
        user_input = input("Enter option: ").lower()
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
    
    

      
    while True:
        user_input = input("Enter choice: ").lower()
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
            
            
    


    





def choosetable():
    
    print("")
    print("Type 1 to sit at the loud table")
    print("")
    print("Type 2 to sit at the quieter table")
    print("")

    

    while True:
        user_input = input("Where do you want to sit? ").lower()
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
            
        




def lunchtime():

    global timeforfood

    timeforfood = False
    
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
    


def getahammer():

    global talkedtored
    talkedtored = True
    
    print("")
    print("""

You:
I wonder if you might get me
a rock hammer.

Red:
A hammer? In a prison? You must be mad.

You:
A rock hammer is about
six or seven inches long. Looks like a miniature pickaxe
I'm a rock hound.
At least I was in my old life.

Red:
Or maybe you'd like to sink your toy
into somebody's skull

You:
No, I have no enemies here.

Red has now given you the hammer wrapped in a cloth.
""")
    inventory.append(item_hammer)
    inventory.append(item_cloth)

    time.sleep(11)
    



def talktored():
    global talkedtored
    talkedtored = True
    print("")
    print("You are now in the Yard.")
    print("You see Red. You approach him.")
    print("")
    print("""
You:
I understand you're a man
that knows how to get things.

Red:
I'm known to locate certain things
from time to time.
""")

    print("Type 1 to ask for a Hammer.")
    print("Type 2 to leave without anything.")

    
    while True:
        user_input = input("Enter option: ").lower()
        if user_input == "1":

            print("___________________________________________________________________")
            
            getahammer()
            break

        elif user_input == "2":

            print("___________________________________________________________________")
            print("Hint: It's better if you ask for a hammmer.It would come in handy!")

            time.sleep(1.3)

            getahammer()

            break
        else:

            print("")
            print("You cannot do that")
            print("")
        
            



def getshank():
    

    print("")
    print("""

You:
Sisters want a shank for some business

Red:
Here is your shank.
Just....be careful around the sisters.
""")
    inventory.append(item_shank)

    time.sleep(1)

    print("""
Red passes you the shank, you discreetly put it in the waistband of your trousers.

You turn to leave the Yard when you see the Sisters and around seven others grouped together.
The Sisters give you a nod and motion for you to join them.
""")
    time.sleep(3.2)

    print("“I hope you’re ready Fish.”")

    time.sleep(1.2)

    print("""

Suddenly the group charge at the guard covering the yard’s entrance,
the sister’s grab his weapon whilst the others beat him.

You stand motionless watching the violence unfold when one of the Sisters snaps at you:

""")

    time.sleep(2.3)

    print("What do you want to do? ")
    print("")
    print("1)Withdraw your shank and follow the Sister ")
    print("2)Run and hide")

    while True:
        user_input = input("Enter option: ")

        if user_input == "1":

            print("___________________________________________________________________")
            print("")
            print("""

You withdraw your shank and follow the Sister’s into the Prison,
adrenaline is coursing through your veins.

""")
            time.sleep(2)

            print("As a mob you take control of the canteen and hold two guards’ hostage.")

            time.sleep(2)

            print("""

The Sister’s ask you and two others to move to the Guards office
and get the keys for the cells but on the way the Guards surround you. 

""")
            time.sleep(3)

            print("""

You fight bravely but are no match for the guards in riot gear and fall to the ground. 

""")
            time.sleep(2)

            print("""

15 years are added to your sentence and you are moved to a higher security prison.

""")
            print("Do you want to Restart or Exit the game?")


            while True:
                user_input = input("Enter option: ").lower()

                if user_input == "restart":
                    execute_restart()
                elif user_input == "exit":
                    exit()
                else:
                    print("")
                    print("You cannot do that.")
                    
            
                
            
        elif user_input == "2":
            print("")
            print("""

Adrenaline coursing through your veins,
you run as fast as your cowardly legs can carry you towards the fence. 
""")
            time.sleep(3.5)
            print("As you turn to see if the Sisters are following you,")
            time.sleep(3)
            print("""
you trip and the shank in your waistband sinks deep into your side as you hit the ground.

You bleed out in the yard.

""")
            time.sleep(3)
            
            print("Oops.")

            print("Do you want to Restart or Exit the game?")

            print("Type 1 to Restart")
            print("Type 2 to Exit")


            while True:
                user_input = input("Enter option: ").lower()

                if user_input == "1":
                    for item in inventory:
                        inventory.remove(item)
            
                    global current_room
                    current_room = rooms["Cell"]

                    global timeforfood
                    global friendswithsisters
                    global enemywithsisters
                    global taxesproblem
                    global knowchess
                    global knowred
                    global talkedtored
            
                    timeforfood = True
                    friendswithsisters = False
                    enemywithsisters = False
                    taxesproblem = False
                    knowchess = False
                    knowred = False
                    talkedtored = False

                    main()

                elif user_input == "2":
                    exit()
                else:
                    print("")
                    print("You cannot do that.")
            
            
        else:
            print("")
            print("You cannot do this.")

          



def talktoredfromsisters():

    print("""
You:
I understand you're a man
that knows how to get things.

Red:
I'm known to locate certain things
from time to time.

""")
    print("Type 1 to ask for the shank")
    print("Type 2 to leave")

    

    while True:
        user_input = input("Enter option").lower()
        if user_input == "1":

            print("___________________________________________________________________")
            getshank()

            break

            pass
        elif user_input == "2":

            print("___________________________________________________________________")
            print("Hint: It's better if you ask for a hammmer.It would come in handy!")

            getshank()
            break
            
            pass
        else:
            print("")
            print("You can't do that")
            print("")



def visitredforshank():

    print("___________________________________________________________________")
    print("")
    print("""
Your in the Yard.
You approach Red.
""")
    talktoredfromsisters()
    
    

def getkilled():

    print("___________________________________________________________________")
    print("")
    print("""
You join the queue to enter the yard and begin searching for Red.
When the guard watching the entrance turns his back you feel two strong arms grip you
and drag you out of the queue into a side room.
You struggle but your arms are held firmly behind your back.
You turn your head and see it’s the sisters with someone else you recognise from the loud table.
They punch you in the stomach, hard.

""")

    time.sleep(20.4)

    print("""“Aren’t you going to scream?” The Sisters smirk at you.""")
    print("")

    time.sleep(3.4)
    print("You manage to get one arm free and swing at the sisters.")
    print("")

    time.sleep(3.4)

    print("“He’s got fight in him, we’ll soon change that.” ")
    print("")

    time.sleep(3.4)

    print("The sisters beat you within an inch of your life.")
    print("")

    time.sleep(3.4)

    print("""

You wake up in the infirmary and spend 4 months recovering.
You are transferred to a different prison for you own protection.

""")
        
    print("")
    print("Type 1 to Restart")
    print("Type 2 to exit")

    

    while True:
        user_input = input("Enter option: ").lower()
        if user_input == "1":
            for item in inventory:
                inventory.remove(item)
            
            global current_room
            current_room = rooms["Cell"]

            global timeforfood
            global friendswithsisters
            global enemywithsisters
            global taxesproblem
            global knowchess
            global knowred
            global talkedtored
            
            timeforfood = True
            friendswithsisters = False
            enemywithsisters = False
            taxesproblem = False
            knowchess = False
            knowred = False
            talkedtored = False

            main()

        elif user_input == "2":
            exit()

        else:
            print("You cannot do that")
            

def firstoffice():
    global first_office
    

    print("___________________________________________________________________")
    print("")
    print("You are now in the Guard's Office.")
    print("""
An old, worn sign showed “NO INMATES” on the open door,
you peak around the corner. 
Three guards are sat eating their lunch talking in the common room.
To your left you can see a door ajar with “Wardens Office” written on.
On the his wall you can make out a Poster of a Chess board.

""")
    print("What do you want to do?")
    print("")
    print("Type 1 to go back to cell, I don’t want to risk getting caught here.")
    print("Type 2 to try and overhear what the guards are talking about.")
    
    
    while True:
        user_input = input("Enter option: ").lower()
        if user_input == "1":

            print("___________________________________________________________________")
            global current_room
            current_room = rooms["Cell"]
            break
        
        elif user_input == "2":

            print("___________________________________________________________________")
            print("Guard 1: ")
            print("The Warden has it worst, I heard he has to sell his new car!")
            print("")
            time.sleep(0.9)
            print("Guard 2: ")
            print("It’s a joke, I swear the prisoners have it better than us.")
            print("")
            time.sleep(0.9)
            print("Guard 3: ")
            print("There’s only two things certain in this life, death – and taxes.")
            print("")

            firstoffice_A()
            
            break
            
        else:

            print("")
            print("You cannot do that")
            print("")
        
            
        
        
def firstoffice_A():
    print("What do you want to do?")
    print("Type 1 to 'Go Inside'")
    print("Type 2 to 'Keep Listening'")

    
    while True:
        user_input = input("Enter option: ").lower()
        if user_input == "1":
            print("")
            print("___________________________________________________________________")
            print("Choose what to say next...")
            print("")
            print("Type 1 to say 'I’m sorry to interrupt you Gentleman, I believe I can help you'")
            print("")
            print("Type 2 to say 'Word in the prison is that you are struggling with paying tax, I can help'")
            print("")
            print("___________________________________________________________________")

            while True:
                user_input = input("Enter option: ").lower()
                if user_input == "1":
                    print("""
Guard:
'What do you mean you can help us!'
""")
                    time.sleep(0.9)
                    print("You:")
                    print("I don’t mean to be rude.")
                    time.sleep(0.9)
                    print("I used to be an accountant and I understand the new laws on the taxation of prison officers.")
                    time.sleep(0.9)
                    print("I thought I could be of help.")

                    firstoffice_B()
                
                    break
                elif user_input == "2":
                    print("""
Guard:
'Who do you think you are coming in here, back to your cell.'""")
                    global current_room
                    current_room = rooms["Cell"]
                    break
                else:
                    print("You cannot do that.")
            
            
            break
        elif user_input == "2":
            print ("""
This is a bad decision. The Guards walks past and sees you eavesdropping.
Now you've been sent back to your cell.""")
            global current_room
            current_room = rooms["Cell"]
            break
        else:
            print("You cannot do this.")

    
def firstoffice_B():
    print("")
    print("___________________________________________________________________")
    print("""
The Prison Guards look at each other, not sure how to respond.
Before they get a chance you hear the creak of a chair and the warden’s office door opens fully. 
“Come in here inmate.” The Warden invites you into his office and asks you to take a seat.
""")
    print("What do you want to do?")
    print("")
    print("Type 1 to 'Talk about how you can help him and the other guards with taxes'.")
    print("")
    print("Type 2 to 'Talk about the Warden's love for chess'.")

    while True:
        user_input = input("Enter option").lower()
        if user_input == "1":
        
            print("___________________________________________________________________")
            print("")
            print("""The Warden is impressed with your knowledge and skills and is willing to take your help.""")
            print("")
            print("However, he is suspicious of your kindness and asks 'What's in it for you?'")
            print("")
            print("You:")
            print("“All I ask is for a poster, my cell is cold and unhomely, I would do anything to add some personality to those bare walls. “")
            print("")
            inventory.append(item_poster)
            print("You now have the poster from the Warden's office.")
            global first_office
            first_office = False

            break
        
        elif user_input =="2":
            print("___________________________________________________________________")
            print("The Warden is happy to meet an inmate that shares the same interests as him.")
            print("You begin to notice that he is no longer calling you 'inmate' and comment on his poster.")
            print("The Warden catches you eyeing the poster and offers you it because he sees how lonely the cells can be.")
            inventory.append(item_poster)
            print("You now have the poster from the Warden's office.")
            global first_office
            first_office = False

            break
        
        else:
            print("")
            print("You cannot do this.")


def cellbeginning():

    print("___________________________________________________________________")
    print("")
    print("""
The cell wall are as harsh and dull as the prison itself.
The bed was a plank of wood on legs,
there was nothing you could call a mattress.
A shelf hung alongside your so called bed,
on it laid nothing but your dead wife’s locket.
The cold metal tin they called a toilet clung to the north wall of the cell,
you notice above it the wall has dampened and become soft.
Maybe you could do some damage here.
""")
            
def checkinventory():

    if len(inventory) == 0:

        print("___________________________________________________________________")
        print("")
        print("""
The cell wall are as harsh and dull as the prison itself.
The bed was a plank of wood on legs,
there was nothing you could call a mattress.
A shelf hung alongside your so called bed,
on it laid nothing but your dead wife’s locket.
The cold metal tin they called a toilet clung to the north wall of the cell,
you notice above it the wall has dampened and become soft.
Maybe you could do some damage here.

""")
    elif len(inventory) == 1:

        print("___________________________________________________________________")
        print("")
        print("""
You enter your cell.
You notice the wall above the toilet is still dampened and soft.
Maybe you could some kind of tool to do some damage here and your poster to hide it
from the guards.

""")
    elif len(inventory) == 2:

        print("___________________________________________________________________")
        print("")
        print("""
You enter your cell.
You notice the wall above the toilet is still dampened and soft.
Maybe you could use the hammer to do some damage here,
but be careful the Guards might see it.

""")
    elif len(inventory) == 3:

        print("___________________________________________________________________")
        print("")
        print("""
You enter your cell.
You notice the wall above the toilet is still dampened and soft.
You can use the hammer to do some damage here,
and the poster to cover it up.

You now have everything you need.

Do you want to start your escape?

Type 'yes' to escape
Type 'no' if you want to make the prison your home, what's freedom anyway.

""")

        

        while True:
            user_input = input("Enter option: ").lower()
            
            if user_input == "yes":

                print("")
                print("You delicately begin digging away at the soft cell wall,")
                print("")
                time.sleep(5.5)
                print("the wall crumbles easily and you make quick progress at the start.")
                print("")
                time.sleep(5)
                print("You dig all night and by morning you have a small hole in the wall.")
                print("")
                time.sleep(5)
                print("You cover the hole with the poster and put the fallen rock into your trousers.")
                print("")
                time.sleep(5)
                print("That day you discard the rock in the yard, and head back to your cell,")
                print("")
                time.sleep(5)
                print(",waiting for lights out so you can continue your escape.")
                print("")
                time.sleep(5)
                print("You spend 6 sleepless months carefully digging away at the wall in your cell.")
                print("")
                time.sleep(5)
                print("Every day the wall gets harder, every day you make trips to the yard,")
                print("")
                time.sleep(5)
                print("every day you live with the fact at any point you could get caught.")
                print("")
                time.sleep(5)
                print("You keep doing the taxes for the Warden")
                print("")
                time.sleep(3.3)
                print("and soon the entire guard force to keep their favour,")
                print("")
                time.sleep(5)
                print("whilst fighting tirelessly with the Sisters and other prison gangs.")
                print("")
                time.sleep(5)
                print("After just over six months you reach the end of the wall.")
                print("")
                time.sleep(5)
                print("You wait for a loud, stormy night to make your escape.")
                print("")
                time.sleep(5)
                print("As soon as the lights are out you crawl through the hole,")
                print("")
                time.sleep(5)
                print("make your way to the end and reach the outside.")
                print("")
                time.sleep(5)
                print("The rain drenches you, you strip off your prison uniform and run.")
                print("")
                time.sleep(2)
                print("You are free.")
                print("")
                time.sleep(2)
                print("You are ready to find the true killer.")
                print("")
                time.sleep(2)
                print("You are ready to avenge your wife.")
                print("")

                time.sleep(1.7)

                print ("")
                print("Do you want to Restart or Exit The Game?")
                print("")

                while True:
                    
                    user_input = input("Restart or Exit?").lower()

                    if user_input == "restart":
                        execute_restart()

                    elif user_input == "exit":
                        exit()

                    else:
                        print("Cannot Do That")

                

                
                
                pass
            elif user_input == "no":

                print("")
                print("""
You decide revenge isn't worth it. You choose to remain
in prison because out there you are nothing, in here
you are something.
""")

                print("")
                print("Do you want to Restart or Exit The Game?")
                print("")

                while True:
                    
                    user_input = input("Restart or Exit?").lower()

                    if user_input == "restart":
                        execute_restart()

                    elif user_input == "exit":
                        exit()

                    else:
                        print("Cannot Do That")
                
                
                pass
            else:
                print("You cannot do that.")

    

def learnaboutred():

    print("")
    print("""
While waiting in the queue to enter the Yard,
you overhear other inmates talking abour red.
The man in charge of illegal movement of equipment
and many more.
""")
    time.sleep(2)

    talktored()

       


    
def main():

          
        
    # Main game loop
    while True:
        if current_room["name"] == "Cell":
            checkinventory()
        
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

        if current_room["name"] == "Yard":

            if enemywithsisters == True:
                getkilled()                
                
                pass
            elif friendswithsisters == True:
                visitredforshank()

                pass

            else:
            
                if knowred == True:
                    if talkedtored == False:
                        talktored()
                else:
                    if talkedtored == False:
                        learnaboutred()

        if current_room["name"] == "Guard's Office":
            if first_office == True:
                firstoffice()

                pass
                



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    intro()
    main()

