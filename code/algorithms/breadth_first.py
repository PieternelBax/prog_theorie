from os import stat
import queue
import copy
from turtle import st

"""Breadth First algorithm."""

def possible_moves(grid):
    # initiate list to store possible moves
    possible_moves = []

    # search for empty space
    for row in range(grid._size):
        for col in range(grid._size):
            if grid._grid[row][col] == "_":
                try:
                    # print all vehicles around an empty spot
                    if grid._grid[row][col + 1] != "_" and grid._vehicles[grid._grid[row][col + 1]]._orientation == "H" and col + 1 < grid._size:
                        # print(grid._grid[row][col + 1])
                        possible_moves.append(["left", grid._grid[row][col + 1]])

                    if grid._grid[row][col - 1] != "_" and grid._vehicles[grid._grid[row][col - 1]]._orientation == "H" and col - 1 >= 0:
                        # print(grid._grid[row][col - 1])
                        possible_moves.append(["right", grid._grid[row][col - 1]])      

                    if grid._grid[row + 1][col] != "_" and grid._vehicles[grid._grid[row + 1][col]]._orientation == "V" and row + 1 < grid._size:
                    #     print(grid._grid[row + 1][col]) 
                        possible_moves.append(["up", grid._grid[row + 1][col]])

                    if grid._grid[row - 1][col] != "_" and grid._vehicles[grid._grid[row - 1][col]]._orientation == "V" and row - 1 >= 0:
                        # print(grid._grid[row - 1][col])
                        possible_moves.append(["down", grid._grid[row - 1][col]])
                except IndexError:
                    pass

    return possible_moves

def breadth_first_solver(grid):
    
    # Create a Queue
    # Add stating state to queue
    state_queue = [grid]

    # Create a set to add visited states.
    visited = set()

    # Take the first item in queue and add it to visited list
    current_state = state_queue.pop()
    visited.add(current_state)

    # Create a list of the possible states from the current state. Add those which are not within the visited list to the rear of the queue.
    
    move_list = possible_moves(grid)
    for move in move_list:
        print(move)
        # create child
        # make a move
        # check if game is won

        # 

    
    # Repeat untill queue is empty


