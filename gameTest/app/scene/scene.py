from abc import ABCMeta, abstractmethod


class Scene:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @property
    @abstractmethod
    def is_finished(self):
        pass

    @property
    @abstractmethod
    def next_scene(self):
        pass
