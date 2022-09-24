from disco.transformable import Transformable


class Collidable(Transformable):
    def __init__(self):
        pass

    def collides(other: "Collidable") -> bool:
        return False
