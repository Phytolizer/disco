from abc import ABC, abstractmethod
from numpy import array


class Transformable(ABC):
    @property
    @abstractmethod
    def transform(self) -> array:
        pass
