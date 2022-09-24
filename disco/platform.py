from numpy import array

class Platform:
    def __init__(self,x,y,width,height,theta,sprite):
        self.transform = np.array(  [x,y],
                                    [width,height],
                                    [theta,0])
        self.sprite = sprite

    def collides(entity):

    