from code.algorithms.breadth_1 import possible_moves, make_tuple
import heapq
import copy
import math

def a_star(grid_object):
    
    start_grid = copy.deepcopy(grid_object)

    to_visit = [(0, 0, start_grid)] #TODO: find out all information needed
    visited = {}


    # Arrange to_visit based on the F_cost number / create priority queue
    heapq.heapify(to_visit)

    while len(to_visit) > 0:
        # current node in to_visit with lowest f_cost and pop from list
        current_heap = heapq.heappop(to_visit)
        current_grid = current_heap[2]
 
        child_list = []
        
        # for each neighbour of the current grid:
        for move in possible_moves(current_grid):

            # copy next grid
            child = copy.deepcopy(current_grid)
            direction = move[0]
            vehicle_id = move[1]

            # move car on grid
            child.move(direction,vehicle_id)

            # add currect grid to visited
            created_tuple = make_tuple(current_grid._grid)
            visited[created_tuple] = current_grid

            # if current_node is the target node do not finsih here finsifh queue first
            if child.won():
                # path = find_path(child, visited, grid_object)
                # print(len(path))
                # child.visualize_grid()
                print('found')
                return
            
            child_list.append(child)
            
        count = 0

        for child_in_list in child_list:
            f_cost = calculate_f_cost(child_in_list, child_list)
            count += 1
            heapq.heappush(to_visit, (f_cost, count, child_in_list))
        
        # 

def calculate_h_cost(child_in_list):
    # huidige plaats van car x minus final plek index
    size = child_in_list._size
    middle_row = child_in_list._grid[math.ceil(size / 2) - 1]
    index = middle_row.index('X')
    distance_from_exit = child_in_list._size - 2 - index
    
    # check car die in de weg staan
    free_spaces = middle_row[index:].count('_')
    obstructing_cars = size - 1 - index - 1 - free_spaces

    # distance + cars in de weg = H cost
    h_cost = distance_from_exit + obstructing_cars
    return h_cost


def calculate_f_cost(child_in_list, child_list):
    f_cost = calculate_g_cost(child_list) + calculate_h_cost(child_in_list)
    return f_cost


def calculate_g_cost(child_list):
    g_cost = len(child_list)
    return g_cost


def make_tuple(grid):
    new_tuple = []

    for row in grid:
        new_tuple.append(tuple(row))

    return tuple(new_tuple)
