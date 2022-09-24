from pygame.draw import polygon

class Renderable(Transformable):
    def __init__(self,sprite):
        self.sprite = sprite

    def render(self,surface,color):
        polygon(surface,color,[(self.x,self.y),(self.x+self.width,self.y),(self.x+self.width,self.y+self.height),(self.x,self.y+self.height)])
