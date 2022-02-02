"""
a_star.py
Course: programmeertheorie
Team: The three programmers

This file contains the A* algorithm and is called from the main file (rushhour.py).
The algoritm uses a priority queue and calculates the cost towards the final goal.
Finally it will return the length of the fastest path towards the end goal.
"""
from code.algorithms.breadth_1 import possible_moves, make_tuple, find_path
import queue
import copy
import math


def a_star(grid_object):
    """
    This algorithm builds a priority queue of possible states of the game. Priority is given based on the depth 
    and the admissable heuristic. Only unique states are in the queue. The algorithm stops when a winning state is 
    found or when the queue is empty.
    """

    # initialize starting grid
    start_grid = copy.deepcopy(grid_object)

    # initialize starting grid for queue. First 0 is the F cost, second the ID number, third G cost
    to_visit = (0, 0, 0, start_grid)

    # dictionary to save visited states
    visited = {}

    # set to save the length of the best found path
    best_length = set()

    # initialize the priority queue
    q = queue.PriorityQueue()

    # add starting position to queue
    q.put(to_visit)
    
    # counter for ID number needed for when the F cost is the same
    id_count = 0

    while not q.empty():

        # get the current node from queue
        _, _, current_cost, current_grid = q.get()
        
        # list with new states
        child_list = []
        
        # check for possible moves and return these to loop over
        for move in possible_moves(current_grid):

            # make copy of grid
            child = copy.deepcopy(current_grid)

            # get direction and vehicle ID to move vehicle
            direction = move[0]
            vehicle_id = move[1]

            # move car on grid
            child.move(direction,vehicle_id)
            
            created_tuple = make_tuple(child._grid)

            if created_tuple not in visited:
                # add child to the visited dictionary
                visited[created_tuple] = current_grid
            
                # check if winning state
                if child.won():
                    # find path and calculate the length and stops program once found
                    path = find_path(child, visited, start_grid)
                    path_length = len(path)
                    best_length.add(path_length)
                    print(path_length)
                    return
                    
                # add new states to list
                child_list.append(child)

            # calculate cost and add to the queue
            for child_in_list in child_list:
                id_count += 1
                g_cost = current_cost + 1
                h_cost =  calculate_h_cost(child_in_list)
                f_cost = g_cost + h_cost
                q.put((f_cost, id_count, g_cost, child_in_list))
                
    # return the best length found
    return print(min(best_length))    


def calculate_h_cost(child_in_list):
    """Returns the heuristic cost of a state."""
    # calculate the distance from car X to the goal coordinates
    size = child_in_list._size
    middle_row = child_in_list._grid[math.ceil(size / 2) - 1]
    index = middle_row.index('X')
    distance_from_exit = child_in_list._size - 2 - index
    
    # calculate the amount of obstructing cars in front of car X
    free_spaces = middle_row[index:].count('_')
    obstructing_cars = (size - 1 - index - 1 - free_spaces)

    # add up the factors for the H costs
    h_cost = distance_from_exit + obstructing_cars

    return h_cost
