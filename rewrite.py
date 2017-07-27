import random

class Monster():
    def __init__(self, name, health, attack, defense, level):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level


#   This is where you define the monsters
Green_Blob = Monster("Green Blob", 100, 5, 2, "1")
Red_Blob = Monster("Red Blob", 100, 5, 2, "2")
Blue_Blob = Monster("Blue Blob", 100, 5, 2, "3")
Yellow_Blob = Monster("Yellow Blob", 100, 5, 2, "4")
Black_Blob = Monster("Black Blob", 100, 5, 2, "5")

#   Monster loop this will define if there's a monster in the room or not

def make_monster():
    monster_in = random.randrange(3)
    if monster_in == (0 or 1):
        return 0
    monster = random.randrange(5)
    if monster == 0:
        monster = Green_Blob
    elif monster == 1:
        monster = Red_Blob
    elif monster == 2:
        monster = Blue_Blob
    elif monster == 3:
        monster = Yellow_Blob
    elif monster == 4:
        monster = Black_Blob
    return monster

#   Currently in working progress the battle system
def attack_emeny():
    monster = make_monster()
    while mychar.health > 0:
        print("what move you like to make?")
        answer = input()
        if answer == "attack":
            if monster.health <= 0:
                break
            monster.health = monster.health - (5 + mychar.attack - monster.defense)
            mychar.health = mychar.health - (monster.attack - mychar.defense)
            print("Monster health:",monster.health);print("Character health:",mychar.health)
        elif answer == "flee":
            print("you ran.. fgt")
            break

class Room(object):
    def __init__(self, name, description, monster_y_n):
        self.name = name
        self.description = description
        self.monster_y_n = monster_y_n
        if self.monster_y_n == "y":
            monster = make_monster()
            self.monster = monster

#   Room coordinates are as follows (north, east, south, west)
room1 = Room("Bedroom", "You are you in your own bedroom.\nTo the south, there is a garden past the back door.", "n")
room2 = Room("Garden",
             "You are in a garden with many flowers and a narrow stone path. \nTo the north, you see the backdoor of your house that enters your bedroom.\nA pathway leads west.",
             "y")
room3 = Room("Pathway",
             "You are in a narrow stone path with hedges on both sides of you.\nTo the east, there is a garden.", "y")
#   Room coordinates (had to create all the rooms to assign them to coordinates)
room1.coordinates = [0, 0, room2, 0]
room2.coordinates = [room1, 0, 0, room3]
room3.coordinates = [0, room2, 0, 0]

class Character(object):
    def __init__(self, name, health, attack, defense, location = room1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.location = location
        self.inv = []

    def look(self):
        place = self.location
        print(place.description)
        if place.monster_y_n == "y":
            if place.monster != 0:
                room_monster = place.monster
                print("There is a", room_monster.name, "in the room\n")
                attack_emeny()

#   This is where the main loop starts
whoami = input("input name:\n")
print("choose a class:")
print("warrior: HP: high - Atk: mid  - Def: mid")
print("mage:    HP: low  - Atk: high - Def: mid")
print("theif:   HP: mid  - Atk: mid  - Def: low")
condition = True
while condition:
    pickclass = input()
    if pickclass == "warrior":
        mychar = Character(whoami, 150, 5, 5)
        condition = False
    elif pickclass == "mage":
        mychar = Character(whoami, 100, 10, 5)
        condition = False
    elif pickclass == "theif":
        mychar = Character(whoami, 120, 5, 3)
        condition = False
    elif pickclass != "warrior" or pickclass != "mage" or pickclass != "theif":
        print("Please input again")

print("hello", mychar.name)
print("Welcome to a very simple python text based game")
print("Type commands for a list of commands.")
print("good luck!")
while True:
    command = input("")
    if command == "commands" or command == "command":
        print('"n","e","s", and "w" make your character go north, east, south, and west respectively')
        print('"end" to break')
        print('"look" to look around the room')
        print('"players" to see the player list')
        print("if there's a monster just type attack or flee")
    if command == "look":
        mychar.look()
    if command == ("n" or "north"):
        if mychar.location.coordinates[0] == 0:
            print("You cannot go that way.")
        else:
            mychar.location = mychar.location.coordinates[0]
            mychar.look()
    if command == ("e" or "east"):
        if mychar.location.coordinates[1] == 0:
            print("You cannot go that way.")
        else:
            mychar.location = mychar.location.coordinates[1]
            mychar.look()
    if command == ("s" or "south"):
        if mychar.location.coordinates[2] == 0:
            print("You cannot go that way.")
        else:
            mychar.location = mychar.location.coordinates[2]
            mychar.look()
    if command == ("w" or "west"):
        if mychar.location.coordinates[3] == 0:
            print("You cannot go that way.")
        else:
            mychar.location = mychar.location.coordinates[3]
            mychar.look()
    if command == "end":
        print("Thanks for playing!")
        break
