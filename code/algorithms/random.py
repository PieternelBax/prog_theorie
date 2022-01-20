import random

# row 3 [0, 1, 2, 3, 4, 5]
#  = 
# index [0          -2,-1]

# keep moving cars until vehicle id X is on index -1 -> while loop?
# randomize directions -> list with directions needed
# randomize vehicles -> list with vehicle id's needed
# store move 

def random_solver(grid_object):
    # check if red car is at the end point
    while not grid_object.won():
        # choose random vehicle to move
        vehicle = random.choice(grid_object._vehicle_ids)
        # print(vehicle)

        # choose random move to make
        move = random.choice(grid_object._moves)
        # print(move)

        # check if move is possible to make
        if grid_object.move(move, vehicle) is True:
            print(f"Car {vehicle} moved {move}")
            print(f"Valid move made -> Vehicle {vehicle} moved {move}")

            
            print(grid_object.visualize_grid())
    
# --------------
# random_solver attempt

# move functie werkt niet helemaal goed, random solver geeft index error en 
# verplaatst vehicles voorbij de grid boundaries

# Start grid
# _ _ B A A C
# _ _ B _ _ C
# _ _ B X X C
# _ _ _ G D D
# F E E G _ _
# F _ _ G H H

# Car B moved up
# Valid move made -> Vehicle B moved up
# Grid after move made
# _ _ B A A C
# _ _ B _ _ C
# _ _ _ X X C
# _ _ _ G D D
# F E E G _ _
# F _ B G H H

# Car B moved up
# Valid move made -> Vehicle B moved up
# _ _ B A A C
# _ _ B _ _ C
# _ _ B X X C
# _ _ _ G D D
# F E E G _ _
# F _ _ G H H
    

