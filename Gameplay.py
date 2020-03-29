#GAMEPLAY FUNCTIONS

import sys
import time

def print_text_normal(text):
    print('================================')
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.05)
    print("")

def print_text_slow(text):
    print('================================')
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.1)
    print("")

def print_text_fast(text):
    print('================================')
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.01)
    print("")