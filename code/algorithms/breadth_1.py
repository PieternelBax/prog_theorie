# from matplotlib.pyplot import grid
from code.algorithms.breadth_first import possible_moves
from code.classes.grid import Grid
import queue
import copy

def breadth_first_search(grid_object):

    visited = {}
    # store moves made
    moves_made = []
    # initialize a queue
    q = queue.Queue()

    # make copy
    # grid_copy = copy.deepcopy(grid_object)

    # add a start node to queue
    q.put(grid_object)
    while not q.empty():
        #get the first node
        node = q.get()

        for move in possible_moves(node):
            # copy next grid
            #print(node, move)
            child = copy.deepcopy(node)
            direction = move[0]
            vehicle_id = move[1]

            child.move(direction,vehicle_id)

            created_tuple = make_tuple(child._grid)

            if created_tuple not in visited:
                # make child._grid a tuple so it can be added to the visited set
                visited[created_tuple] = node
                print(child.visualize_grid())
                q.put(child)
                if child.won():
                    path = find_path(child, visited, grid_object)
                    print(len(path))
                    child.visualize_grid()
                    print()
                    return
        if q.qsize() % 1000 == 0:
            print(q.qsize())
    print('hi')           


    # return moves made
    return moves_made


def make_tuple(grid):
    new_tuple = []

    for row in grid:
        new_tuple.append(tuple(row))

    return tuple(new_tuple)

def find_path(child, visited, start_grid):
    path = [child]

    while child != start_grid:
        parent = visited[make_tuple(child._grid)]
        path.append(parent)
        child = parent


    return path
        
