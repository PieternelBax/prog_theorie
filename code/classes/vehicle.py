class Vehicle():

    def __init__(self, car_id, row, column, orientation, length):
        self._car_id = car_id
        self._x = row
        self._y = column
        self._orientation = orientation
        self._length = length

    def __str__(self):
        return f"Car: {self._car_id} Orientation: {self._orientation} Row: {self._x} Column: {self._y} Length: {self._length}" 