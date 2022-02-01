import heapq
import copy

def a_star(grid_object):
    
    start_grid = copy.deepcopy(grid_object)

    to_visit = [(0, start_grid._grid)]
    visited = []

    # Arrange to_visit based on the F_cost number
    heapq.heapify(to_visit)

    while len(to_visit) > 0:
        # current = node in to_visit with lowest f_cost and pop from list
        current = heapq.heappop(to_visit)

        # add currect_node to visited
        visited.append(current)
        
        # if current_node is the target node
        if current.won():
            return
        
        # for each neighbour of the current_node:
            # if neighbour is not traversable or neighbour is in visited:
                # skip to next neighbour
            
            # if new path to neighbour is shorter or neighbour is not in to_visit:
                # set f_cost of neighbour
                # set parent of neighbour to current_node
                # if neighbour is not in to_visit:
                    # add neighbour to to_visit 


def calculate_g_cost():
    pass

def calculate_h_cost():
    pass

def calculate_f_cost():
    pass