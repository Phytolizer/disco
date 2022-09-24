from abc import abstractmethod
from numpy import array


class Transformable:
    @property
    @abstractmethod
    def transform(self) -> array:
        pass
