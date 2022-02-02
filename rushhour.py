from code.classes.grid import Grid
import code.algorithms.random as random_alg
# import code.algorithms.breadth_first as breadth_first
import code.algorithms.breadth_1 as breadth_1
import code.algorithms.a_star as a_star
import code.visualisation.visualisation as visual
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
    total_iterations = 200
    data = []

    for _ in range(total_iterations):
        # create grid object
        grid_object = Grid(size)
        # load cars on grid
        grid_object.load_vehicles(args.csvfile)

        # show visual of starting grid
        # grid_object.visualize_grid()
        # run random algorithm
        data.append([random_alg.random_solver(grid_object)])
        #random_alg.random_solver(grid_object)
        # run breadth first
        # breadth_1.breadth_first_search(grid_object)
        # a_star.a_star(grid_object)
    # visualising random
    visual.outputCsv(workload=args.csvfile, data=data)
    visual.scatterPlot(workload=args.csvfile, data=data)
    # run breadth first algorithm
    # breadth_first.breadth_first_solver(grid_object)

        # run breadth first
        #breadth_1.breadth_first_search(grid_object)
        
        # a_star.a_star(grid_object)


if __name__ == '__main__':

    main()
