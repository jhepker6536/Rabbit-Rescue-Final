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
        image = sprite_sheet.get_image(20 ,19, 367, 96)
        self.platform.append(image)
        image = sprite_sheet.get_image(5, 162, 400, 100)
        self.platform.append(image)
        image = sprite_sheet.get_image(1275, 207, 376, 123)
        self.platform.append(image)
        
        
        self.image = self.platform[self.N]
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = self.x - self.platform_move_x
        self.rect.y = self.y + self.platform_move_y
    