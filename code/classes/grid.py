from code.classes.vehicle import Vehicle
import csv

class Grid(object):
    def __init__(self, size):
        self._size = size
        self._grid = [["_" for i in range(self._size)] for j in range(self._size)]
        
        # dict to store vehicles on a board
        self._vehicles = {}
        
        # # the move to the exit
        # self.end_move = end_move

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

        # print(car_ids)
        # print(self._vehicles["A"])
        # print(self._vehicles.keys())
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
                # if car length is equal to 2, add car to collumn + 1
                if vehicle_dict[vehicle]._length == 2:
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                # if car length is equal to 3, add car to collumn + 2
                else:
                    self._grid[vehicle_dict[vehicle]._row - 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
                    self._grid[vehicle_dict[vehicle]._row + 1][vehicle_dict[vehicle]._col - 1 ] = vehicle_dict[vehicle]._id
        
        
    def visualize_grid(self):
        """Print grid with cars."""
        print("\n".join([str(row) for row in self._grid]))

    def move(self, direction,vehicle_id):
        # find row with count
        row_count = 0
        
        for row in self._grid:
            # check horizontaal vs verticaal
            if vehicle_id in row and self._vehicles[vehicle_id]._orientation == "H":
                # store column
                col = row.index(vehicle_id)
                if direction == "left" and self._grid[row_count][col - 1] == "_":
                    self._grid[row_count][col - 1] = vehicle_id
                    self._grid[row_count][col + self._vehicles[vehicle_id]._length - 1] = "_"
                    self.visualize_grid()
                elif direction == "right" and self._grid[row_count][col + 1] == "_":
                    self._grid[row_count][col + 1] = vehicle_id
                    self._grid[row_count][col - self._vehicles[vehicle_id]._length + 1] = "_"
                    # self.visualize_grid()

                else:
                    return False
                
                # if found stop program
                # print(f"row: {row_count} col: {index}")
                # check huidige coordinaten
            else:
                row_count += 1

                if direction == "up" and self._grid[row_count - 1][col] == "_":
                    self._grid[row_count - 1][col] = vehicle_id
                    self._grid[row_count + self._vehicles[vehicle_id]._length - 1][col] = "_"
                    # self.visualize_grid()
                elif direction == "down" and self._grid[row_count + 1][col] == "_":
                    self._grid[row_count + 1][col] = vehicle_id
                    self._grid[row_count - self._vehicles[vehicle_id]._length + 1][col] = "_"
                else:
                    return False
                
        # check of buren == _ anders illegale move
            
        else:
            print('noo')
        
        
        # Geen illegale move dan coordinaten opslaan in lijst
        # Maak huidige plaats _
        # Opgeslagen coordinaten aanpassen naar coordinaten van richting
        # Terug plaatsen in lijst

    def __str__(self):
        return f"Board -> Width: {self._size}, Height: {self._size} \n {self._grid}"
