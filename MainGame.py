# -*- coding: utf-8 -*-
# Test environment

from Item import *
from Inventory import *
from Character import *
from Room import *
from Gameplay import *
from Battle import *
import sys
import time


def main_game():

    print_text_slow("What name do you go by?")
    user_name = str(input(">> "))
    start_health = 100
    player_input = ''
    if user_name.upper() == 'COOP' or user_name.upper() == 'COOPER':
        print_text_slow("Time to die " + user_name + "...")
        start_health = 1
    else:
        print_text_slow("Welcome " + user_name + ". Good luck...")
    player = Player(user_name, start_health)
    while player_input.upper() != 'QUIT' and player.get_health() > 0:
        if player.find_enemies() != None:
            initiate_battle(player,player.find_enemies())
            player.enemy_died()
        else:
            print_text_fast(player.current_room.get_room_name() + " - " + player.current_room.get_description())
            player.visited_room()
            player_input = player.get_user_action()
            player.perform_user_action(player_input)

main_game()
