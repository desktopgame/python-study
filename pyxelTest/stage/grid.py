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

    def __getitem__(self, row_count):
        return self.__grid[row_count]
