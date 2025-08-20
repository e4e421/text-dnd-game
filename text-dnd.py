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
#variable assignment

player_health = 10

x_cord = 0
y_cord = 0

player_name = ""
player_level = 0

key = ""

island_1_name = "Ground"
island_1_intro = "where everything started"

island_2_name = "Olive"
island_2_intro = "where we create wonders through vine and oil"

island_3_name = "Mistake"
island_3_intro = "where you have to indulge on my occational mistakes"

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
    print("----------------------------------")
    print(f"player {player_name} status as: ")
    print(f"health: {player_health}")
    print(f"level: {player_level}")
    print("----------------------------------")
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
    
player_rank = assign_new_rank()

#activate storyline

def set_player_name():
    player_name = input("Welcome to the world of ESG, I am the lord here." \
    " how my I call you my brave worrier? \n")
    if input(f"Awesome, welcome to this world my friend. From my record, you are {player_name} right?(y/n)") == "y":
        print(f"Welcome to the world {player_name}, lets get started!/n")
        main_story_line()
    else:
        player_name = input("sorry I didn't catch that, how may I call you?")
    return player_name

def main_story_line():
    activate_chapter_1()
    if activate_chapter_1() == "done":
        activate_chapter_2()
        if activate_chapter_2() == "done":
            activate_chapter_3()
    else: None

def activate_chapter_1():
    get_player_status()
    print(f"Welcome to {island_1_name}, {island_1_intro}./n")
    print(f"{player_name}, from now on you are a ")
    return "done"

def activate_chapter_2():
    get_player_status()
    print(f"Welcome to {island_2_name}, {island_2_intro}./n")
    return "done"

def activate_chapter_3():
    get_player_status()
    print(f"Welcome to {island_3_name}, {island_3_intro}./n")
    return "done"

#key command line assignment

while key != "quit":
    key = input(": ")
    player_name = set_player_name()
    if key == "player_status":
        get_player_status()
    elif key == "w" or key == "a" or key == "s" or key == "d":
        move(key)
    elif key == "quit":
        break   