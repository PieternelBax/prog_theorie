from code.classes.grid import Grid
# import code.algorithms.random as random_alg
# import code.algorithms.breadth_first as breadth_first
import code.algorithms.breadth_1 as breadth_1
import pandas as pd
import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', default="data/Rushhour6x6_1.csv", help="Add game csv path here")
    args = parser.parse_args()

    # get grid size from file name
    size = int(re.findall(r'[0-9]+', f"{args.csvfile}")[0])
    
    # run code x times
    total_iterations = 1

    for _ in range(total_iterations):
        # create grid object
        grid_object = Grid(size)
        # load cars on grid
        grid_object.load_vehicles(args.csvfile)
        # show visual of starting grid
        grid_object.visualize_grid()
        # run random algorithm
        # random_alg.random_solver(grid_object)
        # run breadth first
        breadth_1.breadth_first_search(grid_object)

    # run breadth first algorithm
    # breadth_first.breadth_first_solver(grid_object)



if __name__ == '__main__':

    main()
