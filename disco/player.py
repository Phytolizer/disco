import pymunk

class Player:


    def __init__(self, level):
    #### Maybe change this to be imported or inherited from the camera class
        space = pymunk.Space() # Create a space relevant to the camera
        space.gravity = 0, -981 # set gravity for the space

        player = pymunk.Body() # create the player body
        player.position = 100,100

        shape = pymunk.Poly.create_box(player)
        shape.mass = 10
        space.add(player, shape)
        