import heapq
import copy
from code.algorithms.breadth_first import possible_moves

from numpy import true_divide

def a_star(grid_object):
    
    start_grid = copy.deepcopy(grid_object)

    to_visit = [(0, start_grid)] #TODO: find out all information needed
    visited = {}


    # Arrange to_visit based on the F_cost number / create priority queue
    heapq.heapify(to_visit)

    while len(to_visit) > 0:
        # current node in to_visit with lowest f_cost and pop from list
        current_heap = heapq.heappop(to_visit)
        current_grid = current_heap[1]

        # add currect_node to visited
        created_tuple = make_tuple(current_grid._grid)
        visited.add(created_tuple)
        
        child_list = []

        # for each neighbour of the current_node:
        for move in possible_moves(current_grid):
            # copy next grid
            print(current_grid, move)
            child = copy.deepcopy(current_grid)
            direction = move[0]
            vehicle_id = move[1]

            child.move(direction,vehicle_id)

            visited[created_tuple] = current_grid
            # if current_node is the target node do not finsih here finsifh queue first
            if child.won():
                path = find_path(child, visited, grid_object)
                print(len(path))
                child.visualize_grid()
                print()
                return
            
            child_list.append(child)
        
        calculate_g_cost(child_list)

        for child_in_list in child_list:
            calculate_h_cost(child_in_list)
            heapq.heappush(to_visit, (calculate_f_cost(), 0, child_in_list))
        
        # 


def calculate_g_cost(child_list):
    length_child_list = len(child_list)
    return length_child_list

def calculate_h_cost():
    check_distance_from_finish()

def calculate_f_cost():
    return calculate_g_cost() + calculate_h_cost()

def make_tuple(grid):
    new_tuple = []

    for row in grid:
        print(row, 'test')
        new_tuple.append(tuple(row))

    return tuple(new_tuple)

def check_distance_from_finish():
    # huidige plaats van car x minus final plek index
    # check car die in de weg staan
    # distance + cars in de weg = H cost
    pass