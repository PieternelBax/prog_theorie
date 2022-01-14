# setting up the grid for Rush Hour
class grid():
    # load the file (in this case: source_file)
    def __init__(self, file):
        self.board = self.grid_size(file)
        # the move to the exit
        self.end_move
    def grid_size(self, file):
        #  Returns a 2D grid array with the starting positions of the car objects.
        if "12x12" in file:
            size = 12
            # or is size = 144
        elif "6x6" in file:
            size = 6
            # or is size = 36
            # add end_move 
        elif "9x9" in file:
            size = 9 
            # or is size = 81
        else:
            print("Try new size of board")
        