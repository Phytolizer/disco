from abc import abstractmethod
from disco.transformable import Transformable


class Collidable(Transformable):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def collides(other: "Collidable") -> bool:
        pass
