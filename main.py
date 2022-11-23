print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''') 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
def story_start():
    print("You stand on a shore to your left is port which you can see the fabled island in the distance.")
    print("to your right, is the the town of St. Murray's Bay")
    choice = input("Where do you head first? (\"left\" or \"right\")")
    if choice.lower() == "left":
        port_scene()
    elif choice.lower() == "right":
        tavern()

def port_scene():
    print("You head to the port, ships of all sizes lined off.") 
    print("you see three men:\n1. A wealthy man whose crew is currently loading a large ship\n2. A fisherman having a smoke by his medium sized boat\n3. A hooded figure leaning by building at the other side of the port.\n")
    choice = input("whom will you talk to? (1, 2 or 3): ")
    if(choice == "1"):
        wealthy_merchant()
    elif(choice == "2"):
        fisherman()
    elif(choice =="3"):
        shady_man()

def fisherman():
    print("The fisherman looks at you, haggard from what can only assumedly be a long days work.\nHe doesn't look like he'll be willing to help you out much.")
    print("Before you can decide whether to ask or leave he speaks. \n\"I know you're trying to reach that island over in the distance.\" \n\"You certainly ain't the first person here to do that, but y'all look the same so it's easy to guess after a while.\" ")
    print("\"So i'll make you a deal, I'll ferry you to that island and if you do actually happen to find treasure, I want a single piece of it as proof.\"\n")
    choice = input("Do we have a deal?(Y or N)")
    if (choice.lower() == 'y'):
        print("You and the fisherman reach an accord and you board his vessel to head out to sea.\n")
        sea_hazard()
    if (choice.lower() == 'n'):
        print("You decline and leave, him being so aware of your plans doesn't sit right with you.\n")
        port_options("fish")

def shady_man():
    print("Face obscured, not a single unique feature among what little details exist upon the vaguely human shaped cloth that is leaning upon the wall.\nYet you feel their gaze as your approach.")
    print("You muster up the courage and ask if they know a way to get the island. They...IT looks at you silent for a moment but then it speaks.\n\"We can get you to the island...but you might want to go to the bar and get a drink first...\"\n")
    print("The figure then leaves without giving you a chance to ask anything more.\n")
    print("I guess we can follow his advice and go for a drink (1) or we can go check the other people at the port (2) ")
    choice = input("What will you do?(1 or 2)")
    if(choice == "1"):
        tavern()
    elif(choice == "2"):
        port_options("shady")

def wealthy_merchant():
    print("You speak to the man who identifies himself as a merchant who regrettably informs you that the ship is heading in the opposite direction. \nYou can go with him if you like, but you will be heading away from the treausre.\n")
    choice = input("will you go?(\"Y\" or \"N\")")
    if choice.lower() == 'y':
        new_adventure_end()
    elif choice.lower() == 'n':
        print("You bid him safe travel and leave him to finish his preparations.\n")
        port_options("wealth")

def port_options(lock):
    if lock == "shady":
        print("Only two men left:\n1. A wealthy man whose crew is currently loading a large ship\n2. A fisherman having a smoke by his medium sized boat.\n")
        choice = input("whom will you talk to? (1 or 2): ")
        if(choice == "1"):
            wealthy_merchant()
        elif(choice == "2"):
            fisherman()
    elif lock == "fish":
        print("Only two men left:\n1. A wealthy man whose crew is currently loading a large ship\n2. A hooded figure leaning by building at the other side of the port.\n3. Head to town.\n")
        choice = input("whom will you talk to? (1, 2 or 3): ")    
        if(choice == "1"):
            wealthy_merchant()
        elif(choice == "2"):
            shady_man()
        elif(choice == "3"):
            tavern()
    elif lock == "wealth":
        print("Only two men left:\n1. A fisherman having a smoke by his medium sized boat\n2. A hooded figure leaning by building at the other side of the port.\n3. Head to town.\n")
        choice = input("whom will you talk to? (1, 2 or 3): ")
        if(choice == "1"):
            fisherman()
        elif(choice == "2"):
            shady_man()
        elif(choice == "3"):
            tavern()

def tavern():
    print("You walk into town and find a lively tavern.\nYou walk in and find yourself a seat by the bar\n")
    choice = input("Will you have a drink? (\"Y\" or \"N\"): ")
    if choice.lower() == "y":
        take_a_drink(1)
    else:
        print("you don't feel like it's the right time for a drink and head out\n")
        story_start()

def take_a_drink(limit):
    if limit < 5:
        print("you take a drink. The fire of liquor warms your throat and lights up your belly\n")
        choice = input ("will you drink another? (\"Y\" or \"N\") ")
        if choice.lower() == "y":
            limit+=1
            take_a_drink(limit)
        else:
            print("You think you've had enough and head out\n")
            story_start()
    else:
        print("Your world blurs and fades to black\n")
        island_shore(1)

def sea_hazard():
    print("The seas have become rough and the waves batter the ship as you sail.\nYou can see the island it looks so close as if you could just swim towards it.\n")
    choice = input("Will you try to swim for the island (\"Y\" or \"N\") ")
    if choice.lower() =='y':
        print("The seas show you no mercy as you desperately dive into the water to swim for the island that feels like it's a hands reach away.\n")
        health_failure_end()
    else:
        print("You decide to hold fast to the ship and hope the fisherman is skilled enough to make it through the rough tide.\n")
        island_shore()

def island_shore(barrel=0):
    if barrel:
        print("You wake up in a barrel on a shore.\nYour head is pounding and you see lights across the water.\nOnce your eyes focus you realise you're looking at the lights of St. Murray's Bay.\n Somehow by luck or otherwise you appear to be on Treasure Island.\n")
    else:
        print("You land on the shore of treasure island.\n")
    print("You see a foot path by the nearby bushes\n")
    choice = input("Will you follow the tracks(1) or look around(2)")
    if choice == "1":
        cave_encounter()
    else:
        print("There's nothing of note that comes from this action.\nWith nothing else to do you march on the path.\n")
        cave_encounter()

def cave_encounter():
    print("Following the path you come across a cave like entrance.\n walking in you hear a few faint clicks from the floor beneath you, but nothing seems to be happening...\n maybe there a traps or some kind of switch that's not working anymore?\nYou  hear a loud groan ahead and see a side path coming up.")
    choice = input("Will you keep heading straight(1) or take the side path(2)")
    if choice =="1":
        print("You hear a whistle through the air and several sharp punches knock you to the floor\n")
        death_trap_end()       
    elif choice =="2":
        print("You take the side corridor only to realize it's a dead-end\nYou hear a whistling noise quickly pass you by in the hallway before a faint metallic bang is heard closer to the caves entrance.\nYou continue back down the original corridor.\n")
        final_test()
    else:
        print("Your lack of action causes you to get hit by a delayed dart trap\n")
        death_trap_end()

def final_test():
    print("You make it to a room where there lies one large jewel.\nAs big as fist and as clear as a river's waters.\nIt appears to glow faintly on its pedestal.\nThere is a path behind it")
    choice = input("Will you take the jewel(1) or will you ignore it and continue on(2)? ")
    if choice =="1":
        print("the floor shatters beneath you and you fall into darkness")
        death_trap_end()
    if choice == "2":
        good_end()

def good_end():
    print("You have found the Teasure!\nCongratulations!")

def new_adventure_end():
    print("You decide to head on a different adventure...\nGAME OVER")

def death_trap_end():
    print("The hidden traps have claimed you as another victim...\nGAME OVER")

def health_failure_end():
    print("Your body can't handle the challenge and gives out...\nGAME OVER")

story_start()