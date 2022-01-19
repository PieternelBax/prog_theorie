from code.classes.grid import Grid
# import code.loader as loader
import matplotlib.pyplot as plt
import pandas as pd
import pprint
import argparse
import re

def main():
    # import CSV file and read to Pandas Dataframe
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="data/Rushhour6x6_1.csv")
    file = parser.parse_args()
    # df = pd.read_csv(file.csvfile)

    # get grid size from file name
    size = int(re.findall(r'[0-9]+', f"{file.csvfile}")[0])

    # create grid object
    grid_object = Grid(size)

    grid_object.load_vehicle_dict(file.csvfile)
    grid_object.load_vehicle(file.csvfile)
    # print(grid_object._vehicles)


# parser for command line
if __name__ == '__main__':

    main()
