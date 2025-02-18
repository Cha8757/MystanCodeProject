"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    move()
    turn_left()
    for i in range(5):
        move()
    for i in range(3):
        turn_left()

    move()
    for i in range(3):
        turn_left()
    for i in range(5):
        move()
    turn_left()
    move()
    turn_left()
    for i in range(10):
        move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    for i in range(10):
        move()
    turn_left()
    move()
    turn_left()
    for i in range(4):
        move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    for i in range(4):
        move()
    for i in range(2):
        turn_left()
    for i in range(3):
        move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    for i in range(3):
        move()
    for i in range(2):
        turn_left()
    for i in range(13):
        move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    for i in range(13):
        move()
    turn_left()
    move()
    turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(2):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(2):
        turn_left()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
