class Slot(object):
    def __init__(self, point):
        self.__point = point

    def update(self):
        pass

    def draw(self, x: int, y: int, w: int, h: int):
        pass
    
    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        self.__point = point
