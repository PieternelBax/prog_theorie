class Vehicle(object):

    def __init__(self, vehicle_id, row, column, orientation, length):
        self._id = vehicle_id
        self._row = row
        self._col = column
        self._orientation = orientation
        self._length = length


    def __str__(self):
        return f"Vehicle: {self._id} Orientation: {self._orientation} Row: {self._row} Column: {self._col} Length: {self._length}" 