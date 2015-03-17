import pygame
import Constants
class SpriteSheet(object):
   
    sprite_sheet = None
 
    def __init__(self, file_name):
    
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
    def get_image(self, x, y, width, height):
       
        image = pygame.Surface([width, height])
 
       
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        
        image.set_colorkey(Constants.GREEN)
       
 
        
        return image