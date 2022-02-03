"""
breadth_1.py
Course: programmeertheorie
Team: The three programmers

This file contains the Breadth first search algorithm and is called from the main file (rushhour.py).
"""
import queue
import copy

def breadth_first_search(grid_object):
    # initialize dict to store visited grids
    visited = {}
    
    # initialize list to store moves made
    moves_made = []
    
    # initialize a queue
    q = queue.Queue()

    # add start grid to queue
    q.put(grid_object)

    while not q.empty():
        # get the first grid
        node = q.get()

        for move in possible_moves(node):
            # copy next grid
            child = copy.deepcopy(node)

            direction = move[0]
            vehicle_id = move[1]

            # move vehicle on grid
            child.move(direction,vehicle_id)

            created_tuple = make_tuple(child._grid)

            if created_tuple not in visited:
                # add child to visited dict
                visited[created_tuple] = node

                # add child to queue
                q.put(child)

                # check if winning state
                if child.won():
                    path = find_path(child, visited, grid_object)
                    print(len(path))
                    return
                    
    return moves_made


def make_tuple(grid):
    """Turns grid list into a tuple."""
    new_tuple = []

    for row in grid:
        new_tuple.append(tuple(row))

    return tuple(new_tuple)


def find_path(child, visited, start_grid):
    """Returns the path that leads to the solution."""
    path = [child]

    while child != start_grid:
        parent = visited[make_tuple(child._grid)]
        path.append(parent)
        child = parent

    return path
        

def possible_moves(grid):
    """Returns nested list of all possible moves."""
    # initiate list to store possible moves
    possible_moves = []

    for row in range(grid._size):
        for col in range(grid._size):
            # search for empty spot and add all possible moves to list
            if grid._grid[row][col] == "_":
                if col + 1 < grid._size and grid._grid[row][col + 1] != "_" and grid._vehicles[grid._grid[row][col + 1]]._orientation == "H":
                    possible_moves.append(["left", grid._grid[row][col + 1]])

                if col - 1 >= 0 and grid._grid[row][col - 1] != "_" and grid._vehicles[grid._grid[row][col - 1]]._orientation == "H":
                    possible_moves.append(["right", grid._grid[row][col - 1]])      

                if row + 1 < grid._size and grid._grid[row + 1][col] != "_" and grid._vehicles[grid._grid[row + 1][col]]._orientation == "V":
                    possible_moves.append(["up", grid._grid[row + 1][col]])

                if row - 1 >= 0 and grid._grid[row - 1][col] != "_" and grid._vehicles[grid._grid[row - 1][col]]._orientation == "V":
                    possible_moves.append(["down", grid._grid[row - 1][col]])

    return possible_moves