from code.classes.grid import Grid
import code.algorithms.random as random_alg
import code.algorithms.breadth_1 as breadth_1
import code.algorithms.a_star as a_star
import code.visualisation.visualisation as visual
import argparse
import time
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', default="data/Rushhour6x6_1.csv", help="Add game csv path here")
    parser.add_argument('algoritme', default="random.py", help="Add algoritme here")
    args = parser.parse_args()

    # get grid size from file name
    size = int(re.findall(r'[0-9]+', f"{args.csvfile}")[0])

    # create grid object
    grid_object = Grid(size)
    
    # load cars on grid
    grid_object.load_vehicles(args.csvfile)
    
    if args.algoritme == 'random' or args.algoritme == 'r':
        # run code x times
        total_iterations = 1

        # initialize list to add random solutions
        data = []

        for _ in range(total_iterations):
        
            # create grid object
            grid_object = Grid(size)
            
            # load cars on grid
            grid_object.load_vehicles(args.csvfile)

            #-----------------------------------run random algorithm-----------------------------------#
            random_solution = random_alg.random_solver(grid_object)
            print(random_solution)

            #add solution to data list
            data.append(random_solution)

            #--------------------------------plot random solutions data--------------------------------#
            visual.outputCsv(workload=args.csvfile, data=data)
            visual.scatterPlot(workload=args.csvfile, data=data)
    
    if args.algoritme == 'breadth-first' or args.algoritme == 'b':
        #-------------------------------run breadth first algorithm--------------------------------#
        start = time.time()
        breadth_1.breadth_first_search(grid_object)
        end = time.time()
        print(f"Breath first solver took {end - start} seconds\n")
    
    if args.algoritme == 'a*' or args.algoritme == 'a':
        #-----------------------------------run a star algorithm-----------------------------------#
        start = time.time()
        a_star.a_star(grid_object)
        end = time.time()
        print(f"A-star solver took {end - start} seconds\n")

if __name__ == '__main__':

    main()
