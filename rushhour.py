"""
rushhour.py
Course: programmeertheorie
Team: The three programmers

This file is the main file from this file different functions are called in order to run the program.
To run program the following command line argument structure is needed:
"python3 filename.csv algorithm"
algorithms can be entered as one of the following: random or r | breadth-first or b | a-star or a
"""
from code.classes.grid import Grid
import code.algorithms.random as random_alg
import code.algorithms.breadth_1 as breadth_1
import code.algorithms.a_star as a_star
import code.visualisation.visualisation as visual
import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csvfile", default="data/Rushhour6x6_1.csv", help="Add game csv path here")
    parser.add_argument("algoritme", default="random.py", help="Add algoritme here")
    args = parser.parse_args()

    # get grid size from file name
    size = int(re.findall(r"[0-9]+", f"{args.csvfile}")[0])

    # create grid object
    grid_object = Grid(size)
    
    # load cars on grid
    grid_object.load_vehicles(args.csvfile)
    
    # run random algorithm
    if args.algoritme == "random" or args.algoritme == "r":
        # run code x times
        total_iterations = 1

        # initialize list to add random solutions
        data = []

        for _ in range(total_iterations):
            # create grid object
            grid_object = Grid(size)
            
            # load cars on grid
            grid_object.load_vehicles(args.csvfile)

            # run random algorithm
            random_solution = random_alg.random_solver(grid_object)
            print(random_solution)

            # add solution to data list
            data.append(random_solution)

            # # plot random solutions data
            # visual.outputCsv(workload=args.csvfile, data=data)
            # visual.scatterPlot(workload=args.csvfile, data=data)
    
    # run breadth first algorithm
    elif args.algoritme == "breadth-first" or args.algoritme == "b":  
        breadth_1.breadth_first_search(grid_object)

    # run a star algorithm
    elif args.algoritme == "a-star" or args.algoritme == "a":
        a_star.a_star(grid_object)


if __name__ == '__main__':

    main()
