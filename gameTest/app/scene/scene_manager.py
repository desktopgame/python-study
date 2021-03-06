class SceneManager:
    def __init__(self, surface):
        self.__map = {}
        self.__current = ''
        self.__surface = surface

    def add(self, name, scene):
        self.__map[name] = scene
        self.__current = name

    def bind(self, name):
        self.__current = name
        self.__map[name].show()

    def update(self):
        self.__map[self.__current].update()
        if self.__map[self.__current].is_finished:
            self.__map[self.__current].hide()
            self.__current = self.__map[self.__current].next_scene
            self.__map[self.__current].show()

    def draw(self):
        self.__map[self.__current].draw(self.surface)
    
    @property
    def surface(self):
        return self.__surface
