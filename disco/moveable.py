from abc import abstractmethod
from disco.transformable import Transformable


class Moveable(Transformable):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def translate(self):
        #move n stuff
        pass
    
    @abstractmethod
    def rotate(self):
        #rotate n stuff
        pass