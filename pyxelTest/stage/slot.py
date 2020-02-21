class Slot:
    def __init__(self, point):
        self.__point = point

    def update(self):
        pass

    def draw(self):
        pass
    
    @property
    def point(self):
        return self.__point
