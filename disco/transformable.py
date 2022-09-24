from abc import abstractmethod
from numpy import array


class Transformable:
    @abstractmethod
    def getTransform(self) -> array:
        pass
