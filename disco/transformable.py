from abc import ABC, abstractmethod
from math import cos, sin

from numpy import array


class Transformable(ABC):
    @property
    @abstractmethod
    def transform(self) -> array:
        pass

    @staticmethod
    def gen_transform(x: float, y: float, theta: float) -> array:
        return array(
            [
                [cos(theta), sin(theta), x],
                [-sin(theta), cos(theta), y],
                [0, 0, 1],
            ]
        )
