import pandas as pd
import csv
import argparse
from code.classes.grid import Grid
from code.classes.vehicle import Vehicle
import matplotlib.pyplot as plt

def create_vehicle(file):
    with open(file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        # skip header
        # next(csv_reader)

        # create vehicle for each row in file
        for row in csv_reader:
            # create vehicle
            vehicle = Vehicle(row["car"], row["row"], row["col"], row["orientation"], row["length"])

            print(vehicle)


# parser for command line
if __name__ == '__main__':

    # Import CSV file and read to Pandas Dataframe
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="data/Rushhour6x6_1.csv")
    file = parser.parse_args()
    df = pd.read_csv(file.csvfile)
    
    new_file = str(file)
    
    split_name = new_file.split("'")[1]
    #print(split_name)

    # create grid object
    grid_object = Grid(file)

    # get grid size
    grid_size = grid_object.grid_size(split_name)

    # get grid
    grid = grid_object.create_grid(int(grid_size))


    # print(grid_size)
    # print(grid)

    # 
    create_vehicle(file.csvfile)