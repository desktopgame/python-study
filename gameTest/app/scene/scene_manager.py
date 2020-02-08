class SceneManager:
    def __init__(self):
        self.__map = {}
        self.__current = ''

    def add(name, scene):
        self.__map[name] = scene
        self.__current = name

    def bind(name):
        self.__current = name
        self.__map[name].show()

    def update():
        self.__map[self.__current].update()
        if self.__map[self.__current].is_finished:
            self.__map[self.__current].hide()
            self.__current = self.__map[self.__current].next_scene
            self.__map[self.__current].show()

    def draw():
        self.__map[self.__current].draw()
