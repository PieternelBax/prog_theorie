from matplotlib.colors import LogNorm
from code.classes.vehicle import Vehicle
# import code.loader as loader
import matplotlib.pyplot as plt
import numpy as np
import csv

class Grid(object):
    # load the file (in this case: source_file)
    def __init__(self, size):
        self._size = size
        self._board = [["_" for i in range(self._size)] for j in range(self._size)]
        
        # dict to store vehicles on a board
        self._vehicles = {}
        
        # # the move to the exit
        # self.end_move = end_move

    def load_vehicle_dict(self, file):
        """Load all vehicles from the csv file and store them in a dictionary."""

        # initialize list to store car ids
        vehicle_ids = []

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

                # add car ids to list
                vehicle_ids.append(row["vehicle"])

        # print(car_ids)
        # print(self._vehicles["A"])
        # print(self._vehicles.keys())
        return self._vehicles

    def load_vehicle(self, file):
        """Load cars on grid."""
        vehicle_dict = self.load_vehicle_dict(file)

        # print(car)
        for vehicle in vehicle_dict:
            # if orientation is horizontal
            if vehicle_dict[vehicle]._orientation == "H":
                # if length is 2 add the car to row + 1
                if vehicle_dict[vehicle]._length == 2:
                    self._board[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._board[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col] = vehicle_dict[vehicle]._id
                # if length is 3 add the car to row + 2
                else:
                    self._board[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._board[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col] = vehicle_dict[vehicle]._id
                    self._board[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col + 1] = vehicle_dict[vehicle]._id
            # if orientation is verticle
            else:
                # if car length is equal to 2, add car to collumn + 1
                if vehicle_dict[vehicle]._length == 2:
                    self._board[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._board[vehicle_dict[vehicle]._row][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                # if car length is equal to 3, add car to collumn + 2
                else:
                    self._board[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._board[vehicle_dict[vehicle]._row][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._board[vehicle_dict[vehicle]._row + 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
        
        print(self._board)
        

                    
            # Add cars to grid
            # Load cars
            # Loop through cars
            # check orientation
            # check lenght
            # add car in array




    def __str__(self):
        return f"Board -> Width: {self._size}, Height: {self._size} \n {self.board}"
