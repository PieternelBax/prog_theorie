import queue
import copy

def breadth_first_search(grid_object):
    # store moves made
    moves_made = []
    # initialize a queue
    q = queue.Queue()
    # add a start node to queue
    q.put(grid_object)
    while not q.empty():
        #get the first node
        node = q.get()
        # check is the node is the end node
        # get all possible moves for the node
        moves = node._moves
        vehicles=node._vehicle_ids
        # for each move
        for move in moves:
            # check if move is possible to make
            for vehicle in vehicles:
                if node.won():
                    # print(f"Valid move made -> Vehicle {vehicle} moved {move}")
                    # visualize solved puzzle
                    node.visualize_grid()
                    # total amount of moves made
                    print(f"Total moves made: {len(moves_made)}")
                    # return moves made
                    return moves_made
                if node.move(move,vehicle) == True and "{vehicle} moved {move}" not in moves_made :
                    # print(f"Valid move made -> Vehicle {vehicle} moved {move}")
                    # visualize grid
                    #grid_object.visualize_grid()
                    #print()
                    # add move to moves made
                    moves_made.append(f"{vehicle} moved {move}")
                    # add node to queue
                    q.put(node)
    # return moves made
    return moves_made
