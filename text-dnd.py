import random

# now lets start with a story line, with characters and plot twists, with name insertion and cool tools.
'''
Developer's note:
1. set up core interactive functions.
    1a. player statistic(level, health, name etc.)
    1b. moving function
2. Environment seting
    2a. NPC location based on x y cords.
3. set up main storyline.
    3a. activation and welcome
    3b. chapter 1 in island 1
    3c. chapter 2 in island 2 etc.
4. linking player action with storyline.
5. code for rare cases.
6. more
'''


#function assignment

def encounter(npc):
    if npc == "angle":
        if player_level >= 10:
            print(f"You have encountered {npc}")
            print(f"An angle have blessed you with health and luck.")
            get_player_status()
            if player_health <= 9:
                player_health = player_health + 1
            else: None
        elif player_level >= 20:
            print(f"You have encountered {npc}")
            print(f"An angle have blessed you with health and luck.")

def get_player_status():
    print(f"player {player_name} status as: ")
    print(f"health: {player_health}")
    print(f"level: {player_level}")
    return None

def move(input):
    if input == "w":
        y_cord = y_cord + 1
    elif input == "a":
        x_cord = x_cord - 1
    elif input == "s":
        y_cord = y_cord - 1
    elif input == "d":
        x_cord = x_cord + 1
    return None

def get_position():
    print(f"current position: x{x_cord}, y{y_cord}")
    return None

def assign_new_rank():
    if player_level < 10:
        return "Novice"
    elif player_level >= 10 and player_level < 20:
        return "Primary"
    elif player_level >= 20 and player_level < 30:
        return "Secondary"
    elif player_level >= 30 and player_level < 40:
        return 

#activate storyline

def set_player_name():
    player_name = input("Welcome to the world of ESG, I am the lord here." \
    " how my I call you my brave worrier? \n")
    if input(f"Awesome, welcome to this world my friend. From your record, you are {player_name} right?(y/n)") == "y":
        print(f"Welcome to the world {player_name}, as you are new here, I would like to entroduce you to the 'ranking' system.")
    else:
        player_name = input("sorry I didn't catch that, how my I call you?")
    return player_name

def activate_chapter_1():
    get_player_status()
    print(f"{player_name}, from now on you are a ")

#variable assignment

player_health = 10

x_cord = 0
y_cord = 0

player_name = ""
player_level = 0
player_rank = assign_new_rank()

key = ""

#key command line assignment

while key != "quit":
    key = input("command line")
    player_name = set_player_name()
    if key == "player_status":
        get_player_status()
    elif key == "w" or key == "a" or key == "s" or key == "d":
        move(key)
    elif key == "quit":
        break   