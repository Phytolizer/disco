from abc import abstractmethod
from numpy import array


class Transformable:
    def __init__(self,x,y,width,height,theta):
        self.transform = array( [x,y],
                                [width,height],
                                [theta,0])
    @property
    @abstractmethod
    def transform(self) -> array:
        pass
