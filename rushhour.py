import pandas as pd
import argparse
from code.classes.grid import Grid

# parser for command line
if __name__ == '__main__':

    # Import CSV file and read to Pandas Dataframe
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="data/Rushhour6x6_1.csv")
    file = parser.parse_args()
    df = pd.read_csv(file.csvfile)
    
    new_file = str(file)
    split_name = new_file.split("'")[1]
    # print(split_name[1])

    grid_return = Grid.grid_size(file, split_name)
    Grid.create_grid(file, int(grid_return))

    print(grid_return)