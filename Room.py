#ROOM CLASS
#Room - a location block where the Player can explore

from Item import *

class Room:
    
    def __init__(self,room_id,room_name,description,room_inventory,room_north,room_east,room_south,room_west,room_up,room_down,
                        locked_room_north,locked_room_east,locked_room_south,locked_room_west,visited_description,enemy_present = None,visited=False,):
        self.room_id = room_id
        self.room_name = room_name
        self.description = description
        self.room_inventory = room_inventory
        self.room_north = room_north
        self.room_east = room_east
        self.room_south = room_south
        self.room_west = room_west
        self.room_up = room_up
        self.room_down = room_down
        self.locked_room_north = locked_room_north
        self.locked_room_east = locked_room_east
        self.locked_room_south = locked_room_south
        self.locked_room_west = locked_room_west
        self.visited_description = visited_description
        self.enemy_present = enemy_present
        self.visited = visited
    
    def get_room_id(self):
        return self.room_id
    
    def get_room_name(self):
        return self.room_name.upper()
    
    def get_description(self):
        return self.description
    
    def get_room_inventory(self):
        return self.room_inventory
    
    def get_room_north(self):
        return self.room_north
    
    def get_room_east(self):
        return self.room_east
    
    def get_room_south(self):
        return self.room_south
    
    def get_room_west(self):
        return self.room_west
    
    def get_room_up(self):
        return self.room_up
    
    def get_room_down(self):
        return self.room_down
    
    def get_locked_room_north(self):
        return self.locked_room_north
    
    def get_locked_room_east(self):
        return self.locked_room_east
    
    def get_locked_room_south(self):
        return self.locked_room_south
    
    def get_locked_room_west(self):
        return self.locked_room_west

    def get_visited(self):
        return self.visited
        
    def update_description(self,new_description):
        self.description = new_description
    
    def unlock_north_room(self):
        self.locked_room_north = False
    
    def unlock_east_room(self):
        self.locked_room_east = False
    
    def unlock_south_room(self):
        self.locked_room_south = False
    
    def unlock_west_room(self):
        self.locked_room_west = False
    
    def get_enemy_present(self):
        return self.enemy_present
    
    def enemy_defeated(self):
        self.enemy_present = None

    def has_been_visited(self):
        self.visited = True
        self.update_description()

    def update_description(self):
        self.description = self.visited_description

# Map Class
# Map - an array of Rooms

class Map:
    
    def __init__(self,room_array):
        self.room_array = room_array
    
    def get_room_array(self):
        return self.room_array