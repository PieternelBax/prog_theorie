from os import stat
import queue
import copy
from turtle import st

"""Breadth First algorithm."""

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
    # TODO: Create a function find possible moves from current state.
    
    # Repeat untill queue is empty
