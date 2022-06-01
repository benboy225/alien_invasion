import pygame as pg
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        
        # getting the alien image and getting the rect of the image
        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()


        #positioning the alien fleet on the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save the position of the aliean
        self.x = float(self.rect.x)

