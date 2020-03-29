#INVENTORY CLASS
#Inventory - a list that stores Items

from Item import *

class Inventory:
    
    def __init__(self,inventory=[]):
        self.inventory = inventory
    
    def get_inventory(self):
        return self.inventory
    
    def show_inventory(self):
        for item in self.inventory:
            print("|\t" + item.get_name())
    
    def add_item(self,item):
        self.inventory.append(item)
    
    def drop_item(self,item):
        for x in self.inventory:
            if x.get_item_id() == item.get_item_id():
                self.inventory.remove(x)
                break
    
    def is_empty(self):
        if self.inventory == []:
            return True
    