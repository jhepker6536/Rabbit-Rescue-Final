import pygame
from Spritesheet import SpriteSheet
import Constants
import random 
import Player
#Player Colors

class Spikes(pygame.sprite.Sprite):
    spike = []
    spike_move_x = 0
    spike_move_y = 0 
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
        
        super().__init__()
 
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(26, 562, 468, 108)
        image.set_colorkey(Constants.WHITE)
        self.spike.append(image)
        
        
        self.image = self.spike[0]
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = self.x - self.spike_move_x
        self.rect.y = self.y + self.spike_move_y
    
class Snake_limits(pygame.sprite.Sprite):
    limit_move = 0 
    snake_limit_list = []
    def __init__(self,x,y,speed,platform):
        super().__init__()
        
        self.x = x
        self.y = y
        self.platform = platform
        self.speed = speed
        
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(589, 70, 2, 12)
        self.snake_limit_list.append(image)
          
        self.image = self.snake_limit_list[0]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x = self.x - self.limit_move
        self.rect.y = self.y
                
    
class Snake(pygame.sprite.Sprite):
    snake_right = []
    snake_left = []
    change_x = 0
    change_y = 0
    direction = "R"
    move_x = 0
    snake_screen_adjust = 0
      
    def __init__(self,x,y):
        self.x = x
        
        self.y = y
        super().__init__()
        sprite_sheet = SpriteSheet("Snakes.png")
        image = sprite_sheet.get_image(4, 1, 115, 82)
        self.snake_right.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(124, 2,87, 89)
        self.snake_right.append(image)
        image.set_colorkey(Constants.WHITE)
        
        image = sprite_sheet.get_image(4, 1, 115, 82)
        image = pygame.transform.flip(image, True, False)
        self.snake_left.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(124, 2,87, 89)
        image = pygame.transform.flip(image, True, False)
        self.snake_left.append(image)
        image.set_colorkey(Constants.WHITE)
        
        self.image = self.snake_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self): 
        self.change_x = 3
        self.rect.x += self.change_x
        pos = self.rect.x 
        self.limit 
        self.limit2
        
        
        
        if self.direction == "R":
            frame = (pos // 20) % len(self.snake_right)
            self.image = self.snake_right[frame]
        elif self.direction == "L":
            frame = (pos // 20) % len(self.snake_left)
            self.image = self.snake_left[frame]
            
        if self.rect.x >= self.limit2: 
            self.turn_around()   
        if self.rect.x >= self.limit:    
            self.turn_around()
            
        print(self.move_x, self.change_x)
    def turn_around(self):
        self.change_x = self.change_x * -1
        
    
class Caged_Bunny(pygame.sprite.Sprite):
    caged_bunny_list = []
    Cage_move_x = 0 
    image_num = 0
    def __init__(self,x,y,platform):
        self.x = x
        self.y = y
        self.platform = platform
        image_num = 0
        super().__init__()
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(11, 7, 175, 150)
        self.caged_bunny_list.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(531, 395, 220, 343)
        self.caged_bunny_list.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(759, 89, 215, 641)
        self.caged_bunny_list.append(image)
        image.set_colorkey(Constants.WHITE)
        
        
        self.image = self.caged_bunny_list[self.image_num]
        self.rect = self.image.get_rect()
       
    def update(self):
        self.image = self.caged_bunny_list[self.image_num]
        if self.image_num == 0:
            self.rect.y = self.y
        elif self.image_num == 1:
            self.rect.y = self.y - 190
        elif self.image_num == 2: 
            self.rect.y = self.y - 494
        self.rect.x = self.x - self.Cage_move_x
    def free(self):
        self.image_num = 2
    def get_the_key(self):
        self.image_num = 1
class Key(pygame.sprite.Sprite):
    key_list = []
    key_move_x = 0 
    move = False
    def __init__(self, x,y,change):
        self.x = x
        self.change = change
        self.player = list
        self.y = y
        super().__init__()
        sprite_sheet = SpriteSheet("Sprites.png")
        image = sprite_sheet.get_image(544,4,82,86)
        self.key_list.append(image)
        image.set_colorkey(Constants.WHITE)
        
        self.image = self.key_list[0]
        self.rect = self.image.get_rect()        
        self.rect.x =self.x
        self.rect.y =self.y 
    def update(self):
        if self.move == False:
            self.rect.x = self.x - self.key_move_x
        elif self.move == True:
            self.rect.x = 10
        
    def move_key(self):
        self.rect.x = 10
        self.rect.y = 20
        self.move = True
    
    
        
class Player(pygame.sprite.Sprite):
 
    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    brown_bunny = ([35,2,95,88],[20,101,110,122],[5,226,137,116])
    black_bunny = ([179,0,102,88],[183,89,111,113],[175,198,137,130])
    green_bunny = ([389,14,99,88],[389,114,115,123],[367,232,139,127])
    blue_bunny = ([595,0,93,88],[612,92,115,123],[535,214,141,122])
    purple_bunny =([475,350,98,85],[486,470,110,112],[460,580,132,94])
    white_bunny = ([25,339,101,93],[44,449,111,110],[40,565,135,97])
    yellow_bunny = ([656,305,104,91],[636,419,113,113],[605,545,134,94])
    pink_bunny = ([234,331,101,91],[235,443,114,107],[232,556,138,103])
    direction = "R"

    
    level = None

    
    def __init__(self,x,y,list_platform,grav,bunny_color,hight,spike_list): 
        self.height = hight
        self.grav = grav
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.list = list_platform
        self.spike_list = spike_list

        super().__init__()
        sprite_sheet = SpriteSheet("Rabbit_Sprite.png")
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        image = sprite_sheet.get_image(99, 57, 56, 79)
        self.walking_frames_u.append(image)
        
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()        
        image.set_colorkey(Constants.YELLOW)
        self.rect.y = self.y
        self.rect.x = self.x

    def update(self):
        
        
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        pos = self.rect.x 
         
        if self.direction == "R" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "U":
            frame = self.walking_frames_u[0]

        elif self.direction == "L" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if self.grav == True:
            self.calc_grav()
        
        if self.rect.y == 0:
            self.rect.y = 0
            self.change_y = 1
               
        block_hit_list = pygame.sprite.spritecollide(self, self.list, False)
        for block in block_hit_list:
            
            if self.change_y >= 1:
                self.rect.bottom = block.rect.top
            elif self.change_y < 1:
                self.rect.top = block.rect.bottom
            
 
            # Stop our vertical movement
            self.change_y = 0
        block_hit_list = pygame.sprite.spritecollide(self, self.spike_list, False)
        for block in block_hit_list:
            
            self.change_x = 0
           
 
            # Stop our vertical movement
            self.change_y = 0
            
            Constants.game_over = True
        

        if self.rect.x <= 5:
            self.rect.x = 5    
            
        
        
              
    def calc_grav(self):    
        
        if self.rect.y <= 655:
            if self.change_y == 0:
                self.change_y += 1
            else:
                self.change_y += .45
                
            if self.rect.y <= self.height - 96 and self.change_y == 0:
                self.rect.y = self.height - 95  
        else:
            None 

    def go_right(self):
        self.change_x = 3
        self.direction = "R"
    def stop(self):
        self.change_x = 0
        if self.direction == "R":
            self.image = self.walking_frames_r[0]
        elif self.direction == "L":
            self.image = self.walking_frames_l[0]
 
     
    def go_left(self):
        self.change_x -= 3
        self.direction = "L"
    def jump(self):
        if self.change_y <= 0:
            if self.rect.y >= 70:
                self.change_y = -13
            else:
                self.change_y = 5
        else:
            None
    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        
class Animated_Player(pygame.sprite.Sprite):
    
    
    change_x = 0
    change_y = 0
    
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    brown_bunny = ([35,2,95,88],[20,101,110,122],[5,226,137,116])
    black_bunny = ([179,0,102,88],[183,89,111,113],[175,198,137,130])
    green_bunny = ([389,14,99,88],[389,114,115,123],[367,232,139,127])
    blue_bunny = ([595,0,93,88],[612,92,115,123],[535,214,141,122])
    purple_bunny =([475,350,98,89],[486,470,110,112],[460,580,132,94])
    bunny_list = (brown_bunny, black_bunny, green_bunny, blue_bunny,purple_bunny)
    direction = "R"

    
    level = None

    
    def __init__(self,bunny_color,width,left): 
        
        self.width = width 
        self.going_left = left
        self.bunny_color = bunny_color 
        super().__init__()
        sprite_sheet = SpriteSheet("Rabbit_Sprite.png")
        image = sprite_sheet.get_image(self.bunny_color[0][0],self.bunny_color[0][1],self.bunny_color[0][2],self.bunny_color[0][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(self.bunny_color[1][0],self.bunny_color[1][1],self.bunny_color[1][2],self.bunny_color[1][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(self.bunny_color[2][0],self.bunny_color[2][1],self.bunny_color[2][2],self.bunny_color[2][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        
        image = sprite_sheet.get_image(self.bunny_color[0][0],self.bunny_color[0][1],self.bunny_color[0][2],self.bunny_color[0][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(self.bunny_color[1][0],self.bunny_color[1][1],self.bunny_color[1][2],self.bunny_color[1][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(self.bunny_color[2][0],self.bunny_color[2][1],self.bunny_color[2][2],self.bunny_color[2][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        image = sprite_sheet.get_image(99, 57, 56, 79)
        self.walking_frames_u.append(image)
        
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()        
        image.set_colorkey(Constants.YELLOW)
        
        
        if self.going_left == False:
            self.x = random.randrange(-500, -50)
            self.y = random.randrange(100, 400)
        else:
            self.x = random.randrange(1000, 1300)
            self.y = random.randrange(300, 700)
        self.rect.y = self.y
        self.rect.x = self.x
    def update(self):
        
        
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        pos = self.rect.x 
        
        if self.direction == "R":
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "U":
            frame = self.walking_frames_u[0]

        else:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if self.rect.x >= self.width:
            self.rect.x = random.randrange(-100,-50)
        
        if self.going_left == False:
            self.change_x = 3
        self.direction = "R"
    
        if self.going_left == True:
            self.go_left()
     
    def go_left(self):
        self.change_x = -3
        self.direction = "L"
class Not_Moving_Bunny():
    
    brown_bunny = ([35,2,95,88],[20,101,110,122],[5,226,137,116])
    black_bunny = ([179,0,102,88],[183,89,111,113],[175,198,137,130])
    green_bunny = ([389,14,99,88],[389,114,115,123],[367,232,139,127])
    blue_bunny = ([595,0,93,88],[612,92,115,123],[535,214,141,122])
    purple_bunny =([475,350,98,89],[486,470,110,112],[460,580,132,94])
    bunny_list = (brown_bunny, black_bunny, green_bunny, blue_bunny,purple_bunny)
    rabbit = None
    rabbit_list = []
    def __init__(self,c, x, y): 
        super().__init__()
        self.x = x 
        self.y = y
        self.bunny_color = c
        self.rabbit = self.bunny_list[self.bunny_color]
        self.rabbit_x = self.rabbit[0][0]
        self.rabbit_y = self.rabbit[0][1]
        self.rabbit_w = self.rabbit[0][2]
        self.rabbit_l = self.rabbit[0][3]
        
        
        sprite_sheet = SpriteSheet("Rabbit_Sprite.png")
        image = sprite_sheet.get_image(self.rabbit_x,self.rabbit_y,self.rabbit_w,self.rabbit_l)
        self.rabbit_list.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        
        self.image = self.rabbit_list[0]
        self.rect = self.image.get_rect()        
        image.set_colorkey(Constants.YELLOW)
    
        self.rect.y = self.y
        self.rect.x = self.x
class Player_climber(pygame.sprite.Sprite):
 
    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    brown_bunny = ([35,2,95,88],[20,101,110,122],[5,226,137,116])
    black_bunny = ([179,0,102,88],[183,89,111,113],[175,198,137,130])
    green_bunny = ([389,14,99,88],[389,114,115,123],[367,232,139,127])
    blue_bunny = ([595,0,93,88],[612,92,115,123],[535,214,141,122])
    purple_bunny =([475,350,98,89],[486,470,110,112],[460,580,132,94])
    white_bunny = ([25,339,101,93],[44,449,111,110],[40,565,135,97])
    yellow_bunny = ([656,305,104,91],[636,419,113,113],[605,545,134,94])
    pink_bunny = ([234,331,101,91],[235,443,114,107],[232,556,138,103])
    direction = "R"

    
    level = None

    
    def __init__(self,x,y,list_platform,grav,bunny_color,hight,spike_list): 
        self.height = hight
        self.grav = grav
        self.x = x
        self.y = y
        self.list = list_platform
        self.spike_list = spike_list

        super().__init__()
        sprite_sheet = SpriteSheet("Rabbit_Sprite.png")
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.YELLOW)
        
        image = sprite_sheet.get_image(99, 57, 56, 79)
        self.walking_frames_u.append(image)
        
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()        
        image.set_colorkey(Constants.YELLOW)
        self.rect.y = self.y
        self.rect.x = self.x

    def update(self):
        
        
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        pos = self.rect.x 
         
        if self.direction == "R" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "U":
            frame = self.walking_frames_u[0]

        elif self.direction == "L" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if self.grav == True:
            self.calc_grav()
        
        if self.rect.y == 0:
            self.rect.y = 0
            self.change_y = 1
               
        block_hit_list = pygame.sprite.spritecollide(self, self.list, False)
        for block in block_hit_list:
            
            if self.change_y >= 1:
                self.rect.bottom = block.rect.top
            elif self.change_y < 1:
                self.rect.top = block.rect.bottom
            
 
            # Stop our vertical movement
            self.change_y = 0
        block_hit_list = pygame.sprite.spritecollide(self, self.spike_list, False)
        for block in block_hit_list:
            
            self.change_x = 0
           
 
            # Stop our vertical movement
            self.change_y = 0
            
            Constants.game_over = True
        

        if self.rect.x <= 5:
            self.rect.x = 5    
            
        
        
              
    def calc_grav(self):    
        
        if self.change_y == 0:
            self.change_y += 1
        else:
            self.change_y += .45
            
    

    def go_right(self):
        self.change_x = 3
        self.direction = "R"
    def stop(self):
        self.change_x = 0
        if self.direction == "R":
            self.image = self.walking_frames_r[0]
        elif self.direction == "L":
            self.image = self.walking_frames_l[0]
 
     
    def go_left(self):
        self.change_x -= 3
        self.direction = "L"
    def jump(self):
        if self.change_y <= 0:
            if self.rect.y >= 70:
                self.change_y = -13
            else:
                self.change_y = 5
        else:
            None
        

