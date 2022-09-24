import pymunk

class Player:


    def __init__(self, space: pymunk.Space):
    #### Maybe change this to be imported or inherited from the camera class
        player = pymunk.Body() # create the player body
        player.position = 100,100

        shape = pymunk.Poly.create_box(player)
        shape.mass = 10
        space.add(player, shape)
        