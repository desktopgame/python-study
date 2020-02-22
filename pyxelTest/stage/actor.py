from .point import Point
from .grid import Grid
from abc import ABCMeta, abstractmethod

class Actor(metaclass=ABCMeta):
    __point: Point

    def __init__(self, point: Point):
        self.__point = point

    @abstractmethod
    def update(self, grid: Grid):
        pass

    @abstractmethod
    def draw(self, grid: Grid):
        pass

    @property
    def point(self):
        return self.__point