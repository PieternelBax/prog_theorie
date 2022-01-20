from tkinter import TRUE
from code.classes.vehicle import Vehicle
import csv

class Grid(object):
    def __init__(self, size):
        self._size = size
        self._grid = [["_" for i in range(self._size)] for j in range(self._size)]
        
        # dict to store vehicles on a board
        self._vehicles = {}
        self.winning_move

    def win_red_car(self, file):
        """Checks if the red car (X) is at the exit coordinates."""
        if "6x6" in file:
            # coordinates of exit
            self.winning_move = ['X', [5, 2]]
        elif "9x9" in file:
            self.winning_move = ['X', [8, 4]]
        elif "12x12" in file:
            self.winning_move = ['X', [11, 5]]
        else:
            return False

    def load_vehicle_dict(self, file):
        """Load all vehicles from the csv file and store them in a dictionary."""

        with open(file, "r") as csv_file:
            # create dict with vehicle info
            csv_reader = csv.DictReader(csv_file, delimiter = ",") # try without delimiter

            # create vehicle for each row in file
            for row in csv_reader:
                # create vehicle
                vehicle = Vehicle(row["vehicle"], int(row["row"]), int(row["col"]), row["orientation"], int(row["length"]))
                # print(vehicle)

                # add each vehicle to a dict
                self._vehicles[row["vehicle"]] = vehicle

        return self._vehicles

    def load_vehicles(self, file):
        """Load vehicles on grid."""
        vehicle_dict = self.load_vehicle_dict(file)

        for vehicle in vehicle_dict:
            # if orientation is horizontal
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
            # if orientation is verticle
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
        # for row in self._grid:
        #     print(' '.join(map(str, row)))

        print("\n".join([str(row) for row in self._grid]))

    def move(self, direction,vehicle_id):
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
            # check horizontaal vs verticaal
                if self._vehicles[vehicle_id]._orientation == "H":

                    if direction == "left" and self._grid[row_count][col - 1] == "_":
                        self._grid[row_count][col - 1] = vehicle_id
                        self._grid[row_count][col + self._vehicles[vehicle_id]._length - 1] = "_"

                        self.visualize_grid()
                        return True
                    elif direction == "right" and self._grid[row_count][col + self._vehicles[vehicle_id]._length] == "_":
                        self._grid[row_count][col + self._vehicles[vehicle_id]._length] = vehicle_id
                        self._grid[row_count][col] = "_"
                        self.visualize_grid()
                        return True
                elif self._vehicles[vehicle_id]._orientation == "V":
                    if direction == "up" and self._grid[row_count - 1][col] == "_":
                        self._grid[row_count - 1][col] = vehicle_id
                        self._grid[row_count + self._vehicles[vehicle_id]._length - 1][col] = "_"
                        self.visualize_grid()
                        return True
                    elif direction == "down" and self._grid[row_count + self._vehicles[vehicle_id]._length][col] == "_":
                        self._grid[row_count + self._vehicles[vehicle_id]._length][col] = vehicle_id
                        self._grid[row_count][col] = "_"
                        self.visualize_grid()
                        return True
            else:
                    # go to next row
                    row_count += 1

        # Opgeslagen coordinaten aanpassen naar coordinaten van richting
        # Terug plaatsen in lijst

    def __str__(self):
        return f"Board -> Width: {self._size}, Height: {self._size} \n pprint(self._grid)"
