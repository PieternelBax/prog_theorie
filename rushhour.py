from code.classes.grid import Grid
import argparse
import re

def main():
    # import CSV file and read to Pandas Dataframe
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="data/Rushhour6x6_1.csv")
    file = parser.parse_args()

    # get grid size from file name
    size = int(re.findall(r'[0-9]+', f"{file.csvfile}")[0])

    # create grid object
    grid_object = Grid(size)
    
    # load cars on grid
    grid_object.load_vehicles(file.csvfile)

    # show visual of grid
    # grid_object.visualize_grid()

    #move
    grid_object.move("up", "F")
    # grid_object.move("down", "B")
    # grid_object.move("right", "A")
    # grid_object.move("left", "K")





# parser for command line
if __name__ == '__main__':

    main()
