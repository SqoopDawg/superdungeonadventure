#ITEM CLASS
#Item - something the player can put in their inventory

class Item:
    
    def __init__(self,name,description,item_id):
        self.name = name
        self.description = description
        self.item_id = item_id
        
    def get_name(self):
        return self.name
        
    def get_description(self):
        return self.description
        
    def get_item_id(self):
        return self.item_id

#POTIONS
class Potion(Item):
    
    def __init__(self,name,description,item_id,amount_restored):
        Item.__init__(self,name,description,item_id)
        self.amount_restored = amount_restored
    
    def get_amount_restored(self):
        return self.amount_restored

class Health_Potion(Potion):
    
    def __init__(self):
        Potion.__init__(self,'HEALTH POTION','A potion for restoring life force',1,50)

class Mana_Potion(Potion):
    
    def __init__(self):
        Potion.__init__(self,'MANA POTION','A potion for restoring magic energy',2,50)

#WEAPONS
class Weapon(Item):
    
    def __init__(self,name,description,item_id,damage):
        Item.__init__(self,name,description,item_id)
        self.damage = damage
    
    def get_damage(self):
        return self.damage

class Sword(Weapon):
    
    def __init__(self):
        Weapon.__init__(self,'Sword','A short sword used to protect yourself',3,10)

class Axe(Weapon):
    
    def __init__(self):
        Weapon.__init__(self,'Axe','A simple woodcutters axe',4,15)

#KEYS
class Key(Item):
    
    def __init__(self,name,description,item_id,room_id,door_id):
        Item.__init__(self,name,description,item_id)
        self.room_id = room_id
        self.door_id = door_id
    
    def get_room_id(self):
        return self.room_id
    
    def get_door_id(self):
        return self.door_id

class Boss_Key(Key):
    
    def __init__(self):
        Key.__init__(self,'Boss Key','The key to open the lair where the boss is...',5,2,8)

class Western_Hall_Key(Key):
    
    def __init__(self):
        Key.__init__(self,'Western Corridor Key','The key to open the west corridor...',6,2,6)