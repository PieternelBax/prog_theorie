import pandas as pd
import argparse
from code.classes.grid import Grid
import matplotlib.pyplot as plt

# parser for command line
if __name__ == '__main__':

    # Import CSV file and read to Pandas Dataframe
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="data/Rushhour6x6_1.csv")
    file = parser.parse_args()
    df = pd.read_csv(file.csvfile)
    
    new_file = str(file)
    split_name = new_file.split("'")[1]

    # create grid object
    grid_object = Grid(file)

    # get grid size
    grid_size = grid_object.grid_size(split_name)

    # get grid
    grid = grid_object.create_grid(int(grid_size))