import pygame
from Spritesheet import SpriteSheet
import Constants
import random 
import Player
#Player Colors

class Bird(pygame.sprite.Sprite):
    bird = []
    bird_move_x = -3
    bird_move_y = 0 
    direction = "R"
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.change_x = -3
        self.change_y = 0
        
        super().__init__()
 
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(29, 779, 236, 161)
        image.set_colorkey(Constants.WHITE)
        self.bird.append(image)
        image = sprite_sheet.get_image(497, 806, 220, 117)
        image.set_colorkey(Constants.WHITE)
        self.bird.append(image)
        image = sprite_sheet.get_image(269, 810, 207, 113)
        image.set_colorkey(Constants.WHITE)
        self.bird.append(image)
        
        self.image = self.bird[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.rect.x += self.change_x 
        self.rect.y += self.change_y
        pos = self.rect.x 
        
        if self.direction == "R":
            frame = (pos // 20) % len(self.bird)
            self.image = self.bird[frame]
    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        
#Spike Class        
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
  

#snake class   
class Snake(pygame.sprite.Sprite):
    snake_right = []
    snake_left = []
    change_x = 0
    change_y = 0
    direction = "R"
    
      
    def __init__(self,x,y,limit_one,limit_two):
        self.x = x
        self.limit_one = limit_one
        self.limit_two = limit_two
        self.y = y
        super().__init__()
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(2, 1009, 117, 83)
        self.snake_right.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(121, 1010,90, 80)
        self.snake_right.append(image)
        image.set_colorkey(Constants.WHITE)
        
        image = sprite_sheet.get_image(2, 1009, 117, 83)
        image = pygame.transform.flip(image, True, False)
        self.snake_left.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(121, 1010,90, 80)
        image = pygame.transform.flip(image, True, False)
        self.snake_left.append(image)
        image.set_colorkey(Constants.WHITE)
        
        self.image = self.snake_right[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.change_x = 3
    def update(self): 
        
        self.rect.x += self.change_x
        pos = self.rect.x 
        self.rect.y += self.change_y
        if self.direction == "R":
            frame = (pos // 20) % len(self.snake_right)
            self.image = self.snake_right[frame]
        elif self.direction == "L":
            frame = (pos // 20) % len(self.snake_left)
            self.image = self.snake_left[frame]
            
        if self.rect.x >= self.limit_two: 
            self.turn_around()   
        if self.rect.x <= self.limit_one:    
            self.turn_around()
            
        
    def turn_around(self):
        self.change_x = self.change_x * -1
        if self.direction == "L":
            self.direction = "R"
        else:
            self.direction = "L"
        
#Caged bunny class
class Caged_Bunny(pygame.sprite.Sprite):
    caged_bunny_list = []
    Cage_move_x = 0 
    Cage_move_y = 0 
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
            self.rect.y = self.y - self.Cage_move_y
        elif self.image_num == 1:
            self.rect.y = self.y - 190 - self.Cage_move_y
        elif self.image_num == 2: 
            self.rect.y = self.y - 494 - self.Cage_move_y
        
        self.rect.x = self.x - self.Cage_move_x
        
    def free(self):
        self.image_num = 2
    def get_the_key(self):
        self.image_num = 1

#Key Class
class Key(pygame.sprite.Sprite):
    key_list = []
    key_move_x = 0 
    key_move_y = 0 
    move = False
    def __init__(self, x,y,change):
        self.x = x
        self.change = change
        self.player = list
        self.y = y
        super().__init__()
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(800,789,85,89)
        self.key_list.append(image)
        image.set_colorkey(Constants.WHITE)
        
        self.image = self.key_list[0]
        self.rect = self.image.get_rect()        
        self.rect.x = self.x
        self.rect.y = self.y 
    def update(self):
        
        if self.move == False:
            self.rect.x = self.x - self.key_move_x 
            self.rect.y += + self.key_move_y        
        elif self.move == True:
            self.rect.x = 10
            self.rect.y = 0
        
    def move_key(self):
        self.rect.x = 10
        self.rect.y = 20
        self.move = True
    
    
#main player class        
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
        
        if self.rect.y >= 70:
            self.change_y = -13
        else:
            self.change_y = 5
    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        
        
#Animated bunnies for the main screen
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
        
        
#bunnies for the up level
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
        self.start_x = x
        self.start_y = y
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
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            if self.rect.top == block.rect.bottom:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
        block_hit_list = pygame.sprite.spritecollide(self, self.spike_list, False)
        for block in block_hit_list:
            
            self.change_x = 0
           
 
            # Stop our vertical movement
            self.change_y = 0
            
            Constants.game_over = True
        if self.rect.y == 0:
            self.rect.y = 0

        if self.rect.x <= 5:
            self.rect.x = 5    
            
        
        
              
    def calc_grav(self):    
        
        if self.change_y == 0:
            self.change_y += 1
        else:
            self.change_y += .25
            
    

    def go_right(self):
        self.change_x = 5
        self.direction = "R"
    def stop(self):
        self.change_x = 0
        if self.direction == "R":
            self.image = self.walking_frames_r[0]
        elif self.direction == "L":
            self.image = self.walking_frames_l[0]
 
     
    def go_left(self):
        self.change_x -= 5
        self.direction = "L"
    def jump(self):
        
        self.change_y = -8
    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y    

#still bunnies to display information         
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
#Bunnies for the down level   



class Player_Falling(pygame.sprite.Sprite):
 
    change_x = 0
    change_y = 0
    direction = "S"
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_s = []
   
    brown_bunny = ([1509,258,167,225],[1680,260,167,224],[1850,258,174,215])
    black_bunny = ([1500,711,175,225],[1684,709,166,226],[1850,707,164,221])
    green_bunny = ([1500,1379,170,226],[1684,1380,171,225],[1861,1379,173,220])
    blue_bunny = ([1500,40,172,216],[1672,38,170,222],[1842,36,174,219])
    purple_bunny =([1500,1163,173,217],[1679,1159,171,221],[1859,1159,165,216])
    white_bunny = ([1510,489,171,221],[1680,488,172,223],[1851,488,167,216])
    yellow_bunny = ([1510,1609,172,215],[1679,1608,168,220],[1850,1599,170,222])
    pink_bunny = ([1509,939,169,225],[1680,941,166,220],[1850,940,168,218])
    

    
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
        sprite_sheet = SpriteSheet("Caged Bunnies.png")
        image = sprite_sheet.get_image(bunny_color[0][0],bunny_color[0][1],bunny_color[0][2],bunny_color[0][3])
        self.walking_frames_l.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(bunny_color[1][0],bunny_color[1][1],bunny_color[1][2],bunny_color[1][3])
        self.walking_frames_s.append(image)
        image.set_colorkey(Constants.WHITE)
        image = sprite_sheet.get_image(bunny_color[2][0],bunny_color[2][1],bunny_color[2][2],bunny_color[2][3])
        self.walking_frames_r.append(image)
        image.set_colorkey(Constants.WHITE)
        
        
        
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()        
        image.set_colorkey(Constants.WHITE)
        self.rect.y = self.y
        self.rect.x = self.x

    def update(self):
        
        
        self.calc_grav()
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        pos = self.rect.x 
         
        if self.direction == "R" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "S":
            frame = self.walking_frames_s[0]

        elif self.direction == "L" and self.change_y != 1:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        
        
               
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
        
        
        self.change_y += .002
                
         

    def go_right(self):
        self.change_x = 5
        self.direction = "R"
    def stop(self):
        self.change_x = 0
        if self.direction == "R":
            self.image = self.walking_frames_s[0]
        elif self.direction == "L":
            self.image = self.walking_frames_s[0]
 
     
    def go_left(self):
        self.change_x -= 5
        self.direction = "L"
    
    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        
