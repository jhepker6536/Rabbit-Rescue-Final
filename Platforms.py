import pygame
from Spritesheet import SpriteSheet
class Platform(pygame.sprite.Sprite):
    platform = []
    platform_move_x = 0
    platform_move_y = 0 
    def __init__(self, x,y,number):
        self.x = x
        self.y = y
        
        self.N = number
        super().__init__()
 
        sprite_sheet = SpriteSheet("plat_spritesheet.png")
        image = sprite_sheet.get_image(0, 673, 4108, 94)
        self.platform.append(image)
        image = sprite_sheet.get_image(23 ,17, 367, 98)
        self.platform.append(image)
        
        
        self.image = self.platform[self.N]
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = self.x - self.platform_move_x
        self.rect.y = self.y + self.platform_move_y
    