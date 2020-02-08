from abc import ABCMeta, abstractmethod


class Scene:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show():
        pass

    @abstractmethod
    def hide():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def draw():
        pass
