from asyncore import loop
import heapq
from http.client import FOUND

from zmq import fd_sockopts

def a_star():
    to_visit = 
    visited =

    loop
        current = node in to_visit with lowest f_cost
        remove current_node from to_visit
        add currect_node to visited

        if current_node is the target node
            return path has been found
        
        for each neighbour of the current_node:
            if neighbour is not traversable or neighbour is in visited:
                skip to next neighbour
            
            if new path to neighbour is shorter or neighbour is not in to_visit:
                set f_cost of neighbour
                set parent of neighbour to current_node
                if neighbour is not in to_visit:
                    add neighbour to to_visit 


def calculate_g_cost():
    pass

def calculate_h_cost():
    pass

def calculate_f_cost():
    pass