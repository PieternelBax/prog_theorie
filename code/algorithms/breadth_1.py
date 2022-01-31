# from matplotlib.pyplot import grid
from code.algorithms.breadth_first import possible_moves
from code.classes.grid import Grid
import queue
import copy

def breadth_first_search(grid_object):

    visited = []
    # store moves made
    moves_made = []
    # initialize a queue
    q = queue.Queue()

    # make copy
    grid_copy = copy.deepcopy(grid_object)

    # add a start node to queue
    q.put(grid_object)
    while not q.empty():
        #get the first node
        node = q.get()
        # check is the node is the end node
        if node.won():
            # visualize solved puzzle
            grid_object.visualize_grid()
            # total amount of moves made
            print(f"Total moves made: {len(moves_made)}")
            # return moves made
            return moves_made

        for move in possible_moves(node):
            # copy next grid
            child = copy.deepcopy(node)
            direction = move[0]
            vehicle_id = move[1]

            if child.move(direction,vehicle_id) == True and child._grid not in visited:
                visited.append(child._grid)
                q.put(child._grid)

            # print(child)
            # q.put(child)
            print(child._grid)

            print(visited)


    # return moves made
    return moves_made
