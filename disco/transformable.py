from abc import abstractmethod
from numpy import array


class Transformable:
<<<<<<< HEAD
    def __init__(self,x,y,width,height,theta):
        self.transform = array( [x,y],
                                [width,height],
                                [theta,0])
    
    def getTransform(self):
        return self.transform
=======
    @property
    @abstractmethod
    def transform(self) -> array:
        pass
>>>>>>> 1bc7b3c301b5f04bab9e911625e30515be7702d5
