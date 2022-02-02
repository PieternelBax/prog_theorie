from code.classes.vehicle import Vehicle
import pprint
import csv

class Grid(object):
    def __init__(self, size):
        self._size = size

        # initial empty grid
        self._grid = [["_" for _ in range(self._size)] for _ in range(self._size)]

        # dict to store vehicles on a board
        self._vehicles = {}

        # list of vehicle dict keys (id's)
        self._vehicle_ids = []

        # list of all possible moves 
        self._moves = ["right", "left", "up", "down"]


    def create_id_list(self):
        """
        Returns a list with all keys (vehicle IDs) from the vehicle dictionary.
        This function is used to generate a random vehicle in the random algorithm.
        """
        self._vehicle_ids = [*self._vehicles]
        return self._vehicle_ids


    def won(self):
        """Checks if the red car (X) is at the end of the row that contains the red car."""
        if self._grid[self._vehicles["X"]._row - 1][-1] == "X":
            return True


    def load_vehicle_dict(self, file):
        """Load all vehicles from the csv file and store them in a dictionary."""
        with open(file, "r") as csv_file:
            # create dict with vehicle info
            csv_reader = csv.DictReader(csv_file) 

            # create vehicle for each row in file
            for row in csv_reader:
                # create vehicle
                vehicle = Vehicle(row["vehicle"], int(row["row"]), int(row["col"]), row["orientation"], int(row["length"]))

                # add each vehicle to a dict
                self._vehicles[row["vehicle"]] = vehicle

        return self._vehicles


    def load_vehicles(self, file):
        """Load vehicles on grid."""
        # get dict with vehicles
        vehicle_dict = self.load_vehicle_dict(file)

        # call method to create list of vehicle IDs
        self.create_id_list()

        for vehicle in vehicle_dict:
            # orientation is horizontal
            if vehicle_dict[vehicle]._orientation == "H":
                # if length is 2 add the car to row + 1
                if vehicle_dict[vehicle]._length == 2:
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col] = vehicle_dict[vehicle]._id
                # if length is 3 add the car to row + 2
                else:
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col + 1] = vehicle_dict[vehicle]._id
            # orientation is verticle
            else:
                # if car length is equal to 2, add car to column + 1
                if vehicle_dict[vehicle]._length == 2:
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                # if car length is equal to 3, add car to column + 2
                else:
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row + 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
        

    def visualize_grid(self):
        """Prints string representation of grid with cars."""
        for row in self._grid:
            print(*row)


    def move(self, direction, vehicle_id):
        """
        Checks if move in certain direction is possible, given a vehicle id.
        If possible, vehicle id gets inserted in open space and replaces previously
        occupied spot with a "_".
        """
        # find row with count
        row_count = 0
        
        for row in self._grid:
            if vehicle_id in row:
                # store column
                col = row.index(vehicle_id)
                try:
                    # check orientation of vehicle
                    if self._vehicles[vehicle_id]._orientation == "H":
                        # check direction if move is within borders of grid and if move is possible
                        if direction == "left" and not col - 1 < 0 and self._grid[row_count][col - 1] == "_" :
                            self._grid[row_count][col - 1] = vehicle_id
                            self._grid[row_count][col + self._vehicles[vehicle_id]._length - 1] = "_"
                            
                            return True
                        elif direction == "right" and not col + self._vehicles[vehicle_id]._length > self._size and self._grid[row_count][col + self._vehicles[vehicle_id]._length] == "_" :
                            self._grid[row_count][col + self._vehicles[vehicle_id]._length] = vehicle_id
                            self._grid[row_count][col] = "_"

                            return True
                    elif self._vehicles[vehicle_id]._orientation == "V":
                        if direction == "up" and not row_count - 1 < 0 and self._grid[row_count - 1][col] == "_" :
                            self._grid[row_count - 1][col] = vehicle_id
                            self._grid[row_count + self._vehicles[vehicle_id]._length - 1][col] = "_"

                            return True
                        elif direction == "down" and not row_count + self._vehicles[vehicle_id]._length > self._size and self._grid[row_count + self._vehicles[vehicle_id]._length][col] == "_" :
                            self._grid[row_count + self._vehicles[vehicle_id]._length][col] = vehicle_id
                            self._grid[row_count][col] = "_"

                            return True
                except IndexError:
                    pass
            else:
                # go to next row
                row_count += 1


    def __str__(self):
        return f"Board -> Width: {self._size}, Height: {self._size} \n {pprint.pprint(self._grid, compact=True, width=50)}"
