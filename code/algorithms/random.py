import random

from pyparsing import col

from code.classes.grid import Grid

# victory end point
# coordinate x = row nr of vehicle X
# coordinate y = last row index of vehicle x (-1 or -2)

# row 3 [0, 1, 2, 3, 4, 5]
# index [0          -2,-1]

# keep moving cars until vehicle id X is on index -1 -> while loop?
# randomize directions -> list with directions needed
# randomize vehicles -> list with vehicle id's needed
# check if move made
# store move 

def random_solver(move, vehicle_id, grid_size, grid_object):
    # while game not won:
        # choose random vehicle to move
        # vehicle = random.choice(list of vehicle id's)

        # choose random move to make
        # move = random.choice(list of moves)
    
    # show current grid
    current_grid = ""

    for row in range(grid_size):
        for col in range(grid_size):
            current_grid += grid_object._grid[row][col]
