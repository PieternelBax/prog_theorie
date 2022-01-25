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
            print(f"Valid move made -> Vehicle {vehicle} moved {move}")

            grid_object.visualize_grid()

            moves_made.append(f"{vehicle} moved {move}")

    # total amount of moves made
    print(len(moves_made)) 
