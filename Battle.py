#BATTLE FUNCTIONS
#Battle - when the player fights one or more enemies

from Gameplay import *
from Character import *
from Inventory import *
from Item import *
from Room import *
import random

def get_command(player,enemy):
    print_text_fast("What do you want to do?!\n\tFight\n\tUse Item")
    user_input = str(input(">> "))
    user_input = user_input.upper()
    if user_input == 'FIGHT':
        print_text_fast("Choose your move")
        for move in player.get_moveset():
            print("|\t" + move)
        attack_choice = str(input(">> ")).upper()
        attack(player,enemy,attack_choice)
    elif user_input == 'USE ITEM':
        if not player.get_player_inventory().is_empty():
            print_text_fast("Which potion do you want to use?")
            for item in player.get_player_inventory().get_inventory():
                if item.get_item_id() >= 1 and item.get_item_id() <= 2:
                    print("|\t" + item.get_name())
            potion_choice = str(input(">> ")).upper()
            use_potion(player,potion_choice)
        else:
            print_text_fast("Your inventory is empty!")
            print_text_fast("What do you want to do?!\n\tFight\n\tUse Item")
            user_input = str(input(">> "))
            user_input = user_input.upper()
    else:
        print_text_fast("invalid input!")
        print_text_fast("What do you want to do?!\n\tFight\n\tUse Item")
        user_input = str(input(">> "))
        user_input = user_input.upper()

def attack(attacker,target,attack_name):
    if attacker.get_equipped_weapon() != None:
        total_damage = attacker.get_equipped_weapon().get_damage() + attacker.get_moveset()[attack_name]
        target.set_health(target.get_health() - total_damage)
    else:
        total_damage = attacker.get_moveset()[attack_name]
        target.set_health(target.get_health() - total_damage)

def use_potion(player,potion_name):
    print(potion_name)
    if potion_name == 'HEALTH POTION':
        player.use_health_potion()
        print_text_fast("You recovered HP! You now have " + str(player.get_health()) + " HP!")
    elif potion_name == 'MANA POTION':
        player.use_mana_potion()

def randomize_attack(attacker,target):
    attacker_moveset = []
    for move in attacker.get_moveset():
        attacker_moveset.append(move)
    attack(attacker,target,attacker_moveset[random.randint(0,len(attacker_moveset) - 1)])

def initiate_battle(player,enemy):
    print_text_fast("A " + str(enemy.get_name()) + " attacked!")
    while not player.is_dead() and not enemy.is_dead():
        get_command(player,enemy)
        if enemy.get_health() <= 0:
            enemy.is_dead()
            print_text_fast("You've defeated the " + str(enemy.get_name()) + "!")
            break
        else:
            print_text_fast("The " + str(enemy.get_name()) + " has " + str(enemy.get_health()) + " HP")
        randomize_attack(enemy,player)
        if player.get_health() <= 0:
            player.is_dead()
            print_text_slow("You perished...")
            break
        else:
            print_text_fast("You have taken damage! You have " + str(player.get_health()) + " HP!")
