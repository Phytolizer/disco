from disco.transformable import Transformable


class Renderable(Transformable):
    def __init__(self,sprite):
        self.sprite = sprite
