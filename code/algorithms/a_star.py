from code.algorithms.breadth_1 import possible_moves, make_tuple, find_path
import queue
import copy
import math

def a_star(grid_object):
    
    start_grid = copy.deepcopy(grid_object)

    to_visit = (0, 0, 0, start_grid) #TODO: find out all information needed
    visited = {}
    best_lenght = set()
    q = queue.PriorityQueue()

    # Arrange to_visit based on the F_cost number / create priority queue
    q.put(to_visit)
    id_count = 0

    while not q.empty():
        # current node in to_visit with lowest f_cost and pop from list
        _, _, current_cost, current_grid = q.get()
        
        child_list = []
        
        # for each neighbour of the current grid:
        for move in possible_moves(current_grid):

            # copy next grid
            child = copy.deepcopy(current_grid)
            direction = move[0]
            vehicle_id = move[1]

            # move car on grid
            child.move(direction,vehicle_id)
            # child.visualize_grid()
            # print('before won')
            created_tuple = make_tuple(child._grid)

            if created_tuple not in visited:
                # add child to visited dict
                visited[created_tuple] = current_grid
            
                # if current_node is the target node do not finish here finish queue first
                if child.won():
                    path = find_path(child, visited, start_grid)
                    path_lenght = len(path)
                    print(path_lenght)
                    best_lenght.add(path_lenght)
                    # child.visualize_grid()
                    
                child_list.append(child)

            for child_in_list in child_list:
                id_count += 1
                g_cost = current_cost + 1
                h_cost =  calculate_h_cost(child_in_list)
                f_cost = g_cost + h_cost
                q.put((f_cost, id_count, g_cost, child_in_list))
    return print(min(best_lenght))    

def calculate_h_cost(child_in_list):
    # huidige plaats van car x minus final plek index
    size = child_in_list._size
    middle_row = child_in_list._grid[math.ceil(size / 2) - 1]
    index = middle_row.index('X')
    distance_from_exit = child_in_list._size - 2 - index
    
    # check car die in de weg staan
    free_spaces = middle_row[index:].count('_')
    obstructing_cars = (size - 1 - index - 1 - free_spaces)

    # massa aan rechter kant berekenen
    # row_density = []
    # for row in child_in_list._grid:
    #     free_space_count = row[index + 2:].count('_')
    #     occupied_board = (size - 1 - index - 1 - free_space_count)
    #     row_density.append(occupied_board)
    # board_density = sum(row_density)

    # distance + cars in de weg = H cost
    h_cost = distance_from_exit + obstructing_cars #+ board_density
    return h_cost