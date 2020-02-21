from .slot import Slot
from .point import Point


class Grid:
    def __init__(self, row_count, column_count):
        self.__column_count = column_count
        self.__row_count = row_count
        self.__grid = [
            [Slot(Point(j, i)) for j in range(column_count)] for i in range(row_count)
        ]
    
    @property
    def column_count(self):
        return self.__column_count
    
    @property
    def row_count(self):
        return self.__row_count

    def set_cell(self, row, col, slot):
        self.__grid[row][col] = slot
        slot.point = Point(col, row)
    
    def get_cell(self, row, col):
        return self.__grid[row][col]
