import heapq
import copy

def a_star(grid_object):
    
    start_grid = copy.deepcopy(grid_object)

    to_visit = [(0, start_grid._grid)] #TODO: find out all information needed
    visited = set()

    # Arrange to_visit based on the F_cost number / create priority queue
    heapq.heapify(to_visit)

    while len(to_visit) > 0:
        # current node in to_visit with lowest f_cost and pop from list
        current_heap = heapq.heappop(to_visit)
        current = current_heap[1]

        # add currect_node to visited
        created_tuple = make_tuple(current)
        visited.add(created_tuple)
        
        # if current_node is the target node do not finsih here finsifh queue first
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

def make_tuple(grid):
    new_tuple = []

    for row in grid:
        new_tuple.append(tuple(row))

    return tuple(new_tuple)