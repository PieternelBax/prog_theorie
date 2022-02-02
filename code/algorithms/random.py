"""
random.py
Course: programmeertheorie
Team: The three programmers

This file contains the random algorithm and is called from the main file (rushhour.py).

"""

import random

def random_solver(grid_object):
    
    # initialize list to store moves made
    moves_made = []

    while not grid_object.won():
        
        # choose random vehicle to move
        vehicle = random.choice(grid_object._vehicle_ids)

        # choose random move to make
        move = random.choice(grid_object._moves)

        # check if move is possible to make
        if grid_object.move(move, vehicle):
            moves_made.append(f"{vehicle} moved {move}")

#----------------------------------------Uncomment to get output for one------------------#
#----------------------------------------Comment when finding results of 200--------------#
    #print("\n")
    #print("Solved puzzle:")
    # visualize solved puzzle
    #grid_object.visualize_grid()

    # total amount of moves made
    #print(f"Total moves made: {len(moves_made)}") 
    #print(len(moves_made))
    return str(len(moves_made))

