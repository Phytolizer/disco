from abc import abstractmethod

from pygame.draw import polygon

from disco.transformable import Transformable


class Renderable(Transformable):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def render(self, surface, color):
        pass
