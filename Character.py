#CHARACTER CLASS
#Character - an interactive entity

from Inventory import *
from Item import *
from Room import *
from Gameplay import *

class Character:
    
    def __init__(self,name,health,equipped_weapon,moveset,alive):
        self.name = name
        self.health = health
        self.equipped_weapon = equipped_weapon
        self.moveset = moveset
        self.alive = True
    
    def get_name(self):
        return self.name
        
    def get_health(self):
        return self.health
    
    def get_equipped_weapon(self):
        return self.equipped_weapon
        
    def get_moveset(self):
        return self.moveset
        
    def get_status(self):
        return self.alive
    
    def set_health(self,updated_health):
       self.health = updated_health 
    
    def is_dead(self):
        self.alive = False

#PLAYER CLASS
#Player - the entity that the user controls

class Player(Character):
    
    def __init__(self,name):
        Character.__init__(self,name,1000,Sword(),{'SLASH':10,'FIRE':25},True)
        self.mana = 100
        self.inventory = Inventory([Health_Potion()])
        self.world_map = Map(
                                [Room(1,'Entrance','You approach the entrance to the beasts lair.\n'
                                                   'The dragon has been terrorizing the village for far too long.\n'
                                                   'You are the only one who can defeat it.',Inventory([]),2,None,None,None,None,None,False,False,False,False,'The entrance to the lair'),
                                Room(2,'Main Hall','You enter the main hall of the lair.\n'
                                                    'The torches barely give off any light but just enough to show a giant door to the north.\n'
                                                   'The dragon is in there. If the village is to be safe, you must get in there.',Inventory([Health_Potion()]),8,3,1,6,None,None,True,False,False,True,'The door to the dragon stands before you...'),
                                Room(3,'Eastern Corridor','You enter the eastern hall.\n'
                                                          'To your right is a flight of stairs that go down...somewhere.\n'
                                                          'To your left is a strange door. It gives off an unusual aura.',Inventory([Mana_Potion()]),10,None,4,2,None,None,True,False,False,False,'A mysterious door stands to your left. A flight of stairs sits to your right.'),
                                Room(4,'Dungeon','You go down the flight of stairs and enter the dungeons.\n'
                                                 'Cells line both walls. All looked rusted shut.\n'
                                                 'But you see a cell on your left that is still open...',Inventory([Health_Potion()]),3,5,None,None,None,None,False,False,False,False,'Cells line both walls. Only one is open to your left.',Goblin()),
                                Room(5,'Cell','You enter the only open cell.\n'
                                              'The remains of a poor soul is huddled in the corner.\n'
                                              'It looks like he\'s holding a key...',Inventory([Western_Hall_Key(),Mana_Potion()]),None,None,None,4,None,None,False,False,False,False,'A poor souls remains huddle in the corner.'),
                                Room(6,'Western Corridor','You enter the western hallway.\n'
                                                          'To your right is a flight of stairs going up.\n'
                                                          'But you hear voices coming farther down the hall in front of you.',Inventory([Health_Potion()]),7,2,None,9,None,None,False,False,False,False,'To your right are a flight of stairs. But strange voices can be heard furthur down the hall...'),
                                Room(7,'Armory','You enter the lairs armory.\n'
                                                'The goblin army that the dragon was building got their weaponary here.\n'
                                                'You can\'t let these weapons fall into the wrong hand.\n'
                                                'On the table, you see a key...',Inventory([Boss_Key(),Mana_Potion()]),None,None,6,None,None,None,False,False,False,False,'The craftmanship of the weapons is brutish.',Brute()),
                                Room(8,'Dragons Lair','The dragon\'s lair is big yet empty.',Inventory([]),None,None,2,None,None,None,False,False,False,False,'The dragon is dead...',Dragon()),
                                Room(9,'Riddle Room','Riddle me this!',Inventory([]),None,6,None,None,None,None,False,False,False,False,'RIDDLE!'),
                                Room(10,'Wizards Lab','You look around the wizard\'s lab.\n'
                                                      'Test tubes. Flasks. Strange colorful liquid. You have no idea what the wizard was making.\n'
                                                      'But on the wall, you see a strange yet powerful looking sword...',Inventory([]),None,None,3,None,None,None,False,False,False,False,'The wizard\'s lab is impressive.')]
                                )
        self.current_room = self.world_map.get_room_array()[0]
    
    #GET FUNCTIONS
    
    def get_mana(self):
        return self.mana
    
    def get_player_inventory(self):
        return self.inventory
    
    def get_current_room(self):
        return self.current_room.get_room_id()
    
    def get_world_map(self):
        return self.world_map

    def get_player_status(self):
        print_text_normal(str(self.get_name()) + "\'s Status")
        print("|\tHP:\t" + str(self.get_health()))
        print("|\tMP:\t" + str(self.get_mana()))
    
    def move_room_north(self):
        if not self.current_room.get_locked_room_north():
            for num in range(len(self.world_map.get_room_array())):
                if self.world_map.get_room_array()[num - 1] .get_room_id() == self.current_room.get_room_north():
                    self.current_room = self.world_map.get_room_array()[num - 1]
                    break
        else:
            print_text_fast("The room you are trying to go to is locked")
    
    def move_room_east(self):
        if not self.current_room.get_locked_room_east():
            for num in range(len(self.world_map.get_room_array())):
                if self.world_map.get_room_array()[num - 1] .get_room_id() == self.current_room.get_room_east():
                    self.current_room = self.world_map.get_room_array()[num - 1]
                    break
        else:
            print_text_fast("The room you are trying to go to is locked")
    
    def move_room_south(self):
        if not self.current_room.get_locked_room_south():
            for num in range(len(self.world_map.get_room_array())):
                if self.world_map.get_room_array()[num - 1] .get_room_id() == self.current_room.get_room_south():
                    self.current_room = self.world_map.get_room_array()[num - 1]
                    break
        else:
            print_text_fast("The room you are trying to go to is locked")
    
    def move_room_west(self):
        if not self.current_room.get_locked_room_west():
            for num in range(len(self.world_map.get_room_array())):
                if self.world_map.get_room_array()[num - 1] .get_room_id() == self.current_room.get_room_west():
                    self.current_room = self.world_map.get_room_array()[num - 1]
                    break
        else:
            print_text_fast("The room you are trying to go to is locked")
    
    def move_room_up(self):
        for num in range(len(self.world_map.get_room_array())):
            if self.world_map.get_room_array()[num - 1] .get_room_id() == self.current_room.get_room_up():
                self.current_room = self.world_map.get_room_array()[num - 1]
                break
    
    def move_room_down(self):
        for num in range(len(self.world_map.get_room_array())):
            if self.world_map.get_room_array()[num - 1] .get_room_id() == self.current_room.get_room_down():
                self.current_room = self.world_map.get_room_array()[num - 1]
                break
    
    def update_current_room(self,new_room):
        self.current_room = new_room
    
    def use_health_potion(self):
        for item in self.inventory.get_inventory():
            if item.get_item_id() == 1:
                if (self.health + item.get_amount_restored()) > 100:
                    self.health = 100
                else:
                    self.health += item.get_amount_restored()
                self.inventory.drop_item(item)
                print_text_normal("You used a health potion. You are at " + str(self.get_health()) + "HP.")
    
    def use_mana_potion(self):
        for item in self.inventory.get_inventory():
            if item.get_item_id() == 2:
                if (self.mana + item.get_amount_restored()) > 100:
                    self.mana= 100
                else:
                    self.mana += item.get_amount_restored()
                self.inventory.drop_item(item)
    
    def unlock_north_door(self):
        if self.current_room.get_locked_room_north():
            for item in self.inventory.get_inventory():
                if item.get_item_id() >= 5:
                    if item.get_door_id() == self.current_room.get_room_north():
                        self.current_room.unlock_north_room()
                        print_text_fast("The door to the north room has been unlocked!")
                        self.inventory.drop_item(item)
                    else:
                        print_text_fast("You don't have the key that unlocks that room")
        else:
            print_text_fast("The room you are trying to open is already unlocked...")
    
    def unlock_east_door(self):
        if self.current_room.get_locked_room_east():
            for item in self.inventory.get_inventory():
                if item.get_item_id() >= 5:
                    if item.get_door_id() == self.current_room.get_room_east():
                        self.current_room.unlock_east_room()
                        print_text_fast("The door to the east room has been unlocked!")
                        self.inventory.drop_item(item)
                    else:
                        print_text_fast("You don't have the key that unlocks that room")
        else:
            print_text_fast("The room you are trying to open is already unlocked...")
    
    def unlock_south_door(self):
        if self.current_room.get_locked_room_south():
            for item in self.inventory.get_inventory():
                if item.get_item_id() >= 5:
                    if item.get_door_id() == self.current_room.get_room_south():
                        self.current_room.unlock_south_room()
                        print_text_fast("The door to the south room has been unlocked!")
                        self.inventory.drop_item(item)
                    else:
                        print_text_fast("You don't have the key that unlocks that room")
        else:
            print_text_fast("The room you are trying to open is already unlocked...")
    
    def unlock_west_door(self):
        if self.current_room.get_locked_room_west():
            for item in self.inventory.get_inventory():
                if item.get_item_id() >= 5:
                    if item.get_door_id() == self.current_room.get_room_west():
                        self.current_room.unlock_west_room()
                        print_text_fast("The door to the west room has been unlocked!")
                        self.inventory.drop_item(item)
                    else:
                        print_text_fast("You don't have the key that unlocks that room")
        else:
            print_text_fast("The room you are trying to open is already unlocked...")
    
    def take_key(self):
        if not self.current_room.get_room_inventory().is_empty():
            for item in self.current_room.get_room_inventory().get_inventory():
                if item.get_item_id() >= 5 and item.get_item_id() <= 6:
                    self.inventory.add_item(item)
                    print_text_fast("You picked up the " + str(item.get_name()))
                    self.current_room.get_room_inventory().drop_item(item)
                else:
                    print_text_fast("There are no keys in this room")
        else:
            print_text_fast("The room is empty...")
    
    def take_potion(self):
        if not self.current_room.get_room_inventory().is_empty():
            for item in self.current_room.get_room_inventory().get_inventory():
                if item.get_item_id() >= 1 and item.get_item_id() <= 2:
                    self.inventory.add_item(item)
                    print_text_fast("You picked up a " + str(item.get_name()))
                    self.current_room.get_room_inventory().drop_item(item)
                else:
                    print_text_fast("There are no potions in this room")
        else:
            print_text_fast("The room is empty...")
    
    def look_around(self):
        if not self.current_room.get_room_inventory().is_empty():
            print_text_fast("Inside the room, you see the following:")
            self.current_room.get_room_inventory().show_inventory()
        else:
            print_text_fast("You look around, but there is nothing of interest here")

    def show_inventory(self):
        return self.inventory.show_inventory()
    
    def get_user_action(self):
        print_text_normal("What do you want to do?")
        user_input = str(input(">> "))
        user_input = user_input.upper()
        return user_input
    
    def perform_user_action(self,user_input):
        if user_input == 'GO NORTH':
            self.move_room_north()
        elif user_input == 'GO EAST':
            self.move_room_east()
        elif user_input == 'GO SOUTH':
            self.move_room_south()
        elif user_input == 'GO WEST':
            self.move_room_west()
        elif user_input == 'UNLOCK NORTH ROOM':
            self.unlock_north_door()
        elif user_input == 'UNLOCK EAST ROOM':
            self.unlock_east_door()
        elif user_input == 'UNLOCK SOUTH ROOM':
            self.unlock_south_door()
        elif user_input == 'UNLOCK WEST ROOM':
            self.unlock_west_door()
        elif user_input == 'TAKE KEY':
            self.take_key()
        elif user_input == 'TAKE POTION':
            self.take_potion()
        elif user_input == 'LOOK AROUND':
            self.look_around()
        elif user_input == 'SHOW INVENTORY':
            self.show_inventory()
        elif user_input == 'GET STATUS':
            self.get_player_status()
        elif user_input == 'USE HEALTH POTION':
            self.use_health_potion()
        elif user_input == 'HELP':
            print("To play Super Dungeon Adventure, here are the commands:\n"
                  "GO [Cardinal Direction] - moves player to a room in that direction if one exists\n"
                  "UNLOCK [Cardinal Direction] ROOM - Unlocks the door connected to a room in that direction\n"
                  "TAKE [Key/Potion] - adds a key or potion to inventory\n"
                  "LOOK AROUND - scans the room for any items\n"
                  "SHOW INVENTORY - lists items in inventory\n"
                  "GET STATUS - shows player stats such as HP and MP\n"
                  "USE HEALTH POTION - heals player\n"
                  "HELP - lists commands\n"
                  "QUIT - quits Super Dungeon Adventure")
        elif user_input == 'QUIT':
            return user_input
    
    def find_enemies(self):
        return self.current_room.get_enemy_present()
    
    def enemy_died(self):
        self.current_room.enemy_defeated()

    def visited_room(self):
        if not self.current_room.get_visited():
            self.current_room.has_been_visited()

# ENEMY CLASS
# Enemy - an entity that is hostile towards the Player

class Goblin(Character):
    
    def __init__(self):
        Character.__init__(self,'Goblin',100,Sword(),{'SLASH':10},True)

class Brute(Character):
    
    def __init__(self):
        Character.__init__(self,'Brute',120,Axe(),{'SLASH':10},True)

class Dragon(Character):
    
    def __init__(self):
        Character.__init__(self,'Dragon',150,None,{'FIRE':10,'FLAMETHROWER':20},True)
