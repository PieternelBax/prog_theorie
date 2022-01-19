from enum import auto
from matplotlib.colors import LogNorm
from code.classes.vehicle import Vehicle
import pprint
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
        car_ids = []

        with open(file, "r") as csv_file:
            # create dict with vehicle info
            csv_reader = csv.DictReader(csv_file, delimiter = ",") # try without delimiter

            # create vehicle for each row in file
            for row in csv_reader:
                # create vehicle
                vehicle = Vehicle(row["car"], int(row["row"]), int(row["col"]), row["orientation"], int(row["length"]))
                # print(vehicle)

                # add each vehicle to a dict
                self._vehicles[row["car"]] = vehicle

                # add car ids to list
                car_ids.append(row["car"])

        # print(car_ids)
        # print(self._vehicles["A"])
        # print(self._vehicles.keys())
        return self._vehicles

    def load_cars(self, file):
        """Load cars on grid."""
        car_dict = self.load_vehicle_dict(file)

        # print(car)
        for car in car_dict:
            # print(car_dict[car]._col)
            if car_dict[car]._orientation == "H":
                if car_dict[car]._length == 2:
                    self._board[car_dict[car]._row - 1][car_dict[car]._col - 1 ] = car_dict[car]._id
                    self._board[car_dict[car]._row - 1][car_dict[car]._col] = car_dict[car]._id
                else:
                    self._board[car_dict[car]._row - 1][car_dict[car]._col - 1 ] = car_dict[car]._id
                    self._board[car_dict[car]._row - 1][car_dict[car]._col] = car_dict[car]._id
                    self._board[car_dict[car]._row - 1][car_dict[car]._col + 1] = car_dict[car]._id
            else:
                if car_dict[car]._length == 2:
                    self._board[car_dict[car]._row - 1][car_dict[car]._col - 1 ] = car_dict[car]._id
                    self._board[car_dict[car]._row][car_dict[car]._col - 1 ] = car_dict[car]._id
                    
                else:
                    self._board[car_dict[car]._row - 1][car_dict[car]._col - 1 ] = car_dict[car]._id
                    self._board[car_dict[car]._row][car_dict[car]._col - 1 ] = car_dict[car]._id
                    self._board[car_dict[car]._row + 1][car_dict[car]._col - 1 ] = car_dict[car]._id
        
        # print(self._board)
        pprint.pprint(self._board, compact=True, width=50)

    def __str__(self):
        return f"Board -> Width: {self._size}, Height: {self._size} \n {self.board}"
