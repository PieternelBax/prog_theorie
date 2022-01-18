# setting up the grid for Rush Hour
from venv import create
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

class Grid():
    # load the file (in this case: source_file)
    def __init__(self, file):
        self.board = self.grid_size(file)
        # the move to the exit
        # self.end_move = end_move

    def grid_size(self, file):
        #  Returns a 2D grid array with the starting positions of the car objects.
        if "12x12" in file:
            # size = 12
            # # or is size = 144
            # self.end_move = [12, 7]
            return "12"
        elif "6x6" in file:
            # size = 6
            # # or is size = 36
            # # add end_move 
            # self.end_move = [6, 3]
            return "6"
        elif "9x9" in file:
            # size = 9 
            # # or is size = 81
            # self.end_move = [9, 5]
            return "9"
        else:
            return "Try new size of board"

    def create_grid(self, size):
        # grid = []

        # size = size + 1

        # for row in range(1, size):
        #     for col in range(1, size):
        #         grid.append([row, col])

        nx, ny = (size, size)
        x = np.linspace(1, size, nx)
        y = np.linspace(1, size, ny)
        X, Y = np.meshgrid(x , y)
        
        # x_2, y_2 = np.meshgrid(x, y, indexing = 'ij')
        min_max = np.min(x), np.max(x), np.min(y), np.max(y) 
        res = np.add.outer(range(size), range(size))%2 

        plt.imshow(res)
        plt.xticks([])
        plt.yticks([])
        plt.show()


        
        return grid
           
