from .slot import Slot
from .point import Point


class Grid:
    __row_count: int
    __columnCount: int

    def __init__(self, row_count: int, column_count: int):
        self.__column_count = column_count
        self.__row_count = row_count
        self.__grid = [
            [Slot(Point(j, i)) for j in range(column_count)] for i in range(row_count)
        ]

    def update(self):
        for i in range(self.row_count):
            for j in range(self.column_count):
                self.__grid[i][j].update()

    def draw(self, screen_width: int, screen_height: int):
        cell_width: int = int(screen_width / self.column_count)
        cell_height: int = int(screen_height / self.row_count)
        for i in range(self.row_count):
            for j in range(self.column_count):
                self.__grid[i][j].draw(j * cell_width, i * cell_height, cell_width, cell_height)
        
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
