from code.classes.grid import Grid
import code.algorithms.random as random_alg
import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="data/Rushhour6x6_1.csv")
    file = parser.parse_args()

    # get grid size from file name
    size = int(re.findall(r'[0-9]+', f"{file.csvfile}")[0])

    # create grid object/new game
    grid_object = Grid(size)

    # load cars on grid
    grid_object.load_vehicles(file.csvfile)

    # show visual of starting grid
    grid_object.visualize_grid()

    # run random algorithm
    random_alg.random_solver(grid_object)


if __name__ == '__main__':

    main()
