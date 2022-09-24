import pymunk
from disco import moveable, collidable, transformable, renderable

class Player (moveable, collidable, transformable, renderable):
    def __init__(self, space: pymunk.Space):
    #### Maybe change this to be imported or inherited from the camera class
        super.__init__(self, x=100,y=100, width=5,height=10,theta=0,sprite=None)
        player = pymunk.Body() # create the player body
        shape = pymunk.Poly.create_box(player)
        shape.mass = 10
        space.add(player, shape)
        
    