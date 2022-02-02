import queue
import copy


def breadth_first_search(grid_object):
    # initialize dict to store visited grids
    visited = {}
    # store moves made
    moves_made = []
    # initialize a queue
    q = queue.Queue()

    # add start grid to queue
    q.put(grid_object)

    while not q.empty():
        #get the first grid
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
                print(child.visualize_grid())
                q.put(child)

                if child.won():
                    path = find_path(child, visited, grid_object)
                    print(len(path))
                    child.visualize_grid()
                    print()
                    return
        # print queue
        if q.qsize() % 1000 == 0:
            print(q.qsize())

    # return moves made
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

    # search for empty space
    for row in range(grid._size):
        for col in range(grid._size):
            if grid._grid[row][col] == "_":
                # print all vehicles around an empty spot
                if col + 1 < grid._size and grid._grid[row][col + 1] != "_" and grid._vehicles[grid._grid[row][col + 1]]._orientation == "H":
                    # print(grid._grid[row][col + 1])
                    possible_moves.append(["left", grid._grid[row][col + 1]])

                if col - 1 >= 0 and grid._grid[row][col - 1] != "_" and grid._vehicles[grid._grid[row][col - 1]]._orientation == "H":
                    # print(grid._grid[row][col - 1])
                    possible_moves.append(["right", grid._grid[row][col - 1]])      

                if row + 1 < grid._size and grid._grid[row + 1][col] != "_" and grid._vehicles[grid._grid[row + 1][col]]._orientation == "V":
                #     print(grid._grid[row + 1][col]) 
                    possible_moves.append(["up", grid._grid[row + 1][col]])

                if row - 1 >= 0 and grid._grid[row - 1][col] != "_" and grid._vehicles[grid._grid[row - 1][col]]._orientation == "V":
                    # print(grid._grid[row - 1][col])
                    possible_moves.append(["down", grid._grid[row - 1][col]])

    return possible_moves