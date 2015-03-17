import pygame 
import random 
from Player import Player
from Player import Key
from Player import Caged_Bunny
from Player import Snake
from Player import Snake_limits
import Constants
from Platforms import Platform


 
width = 1366
hight = 768


def level_three(color):
    pygame.init()
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
    mouse_x = 0
    key_collected = False
    mouse_y = 0 
    key_x = 1740
    key_y = 300
    floor_x = 0  
    
    
    if color == "Blue":
        player_color = Player.blue_bunny
    elif color == "Brown":
        player_color = Player.brown_bunny
    elif color == "Purple":
        player_color = Player.purple_bunny
    elif color == "Green":
        player_color = Player.green_bunny 
    elif color == "Yellow":
        player_color = Player.green_bunny   
    elif color == "White":
        player_color = Player.green_bunny
    elif color == "Pink":
        player_color = Player.green_bunny
    else:
        player_color = Player.black_bunny
        
        
    caged_bunny_list = pygame.sprite.Group()
    platform_list = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    key_list = pygame.sprite.Group()
     
    platform_test = Platform(floor_x,674,0)
    platform1 = Platform(400,450,1)
    platform2 = Platform(925,250,1)
    platform3 = Platform(1600,430,1)
    platform6 = Platform(2400,250,1)
    
    player = Player(25,400,platform_list,True,player_color, hight)
    snake = Snake(400,370)
    caged_bunny = Caged_Bunny(3050,525,platform_list) 
    key = Key(key_x,key_y,player.change_x)
    
    #snake limits
    
    
    key_list.add(key)
    
    caged_bunny_list.add(caged_bunny)
    platform_list.add(platform_test, platform2, platform1,platform3,platform6)
    active_sprite_list.add(caged_bunny,player,platform_test,platform2,platform1,platform3,platform6,key)
    
    background_y_change = 0 
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    
    clock = pygame.time.Clock()
    done = False
    
    background_image = pygame.image.load("Up_Down.png")
    background_x = 0
    background_y = 11000
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                
                elif event.key == pygame.K_SPACE:
                    player.jump()
                    
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                    background_x_change = 0 
                elif event.key == pygame.K_RIGHT:
                    player.stop()
                    background_x_change = 0 
                elif event.type == pygame.QUIT:
                    done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                    done = True
                    raise SystemExit

            
        background_y += Player.rect.y                            
        print(background_y)    
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [background_x, background_y])
        
        #quit
        screen.blit(text11, [1200,650])    
        pos = pygame.mouse.get_pos()
        if background_x > 0:
            background_x = -7
        if floor_x > 0:
            floor_x = -7
        mouse_x = pos[0]
        mouse_y = pos[1]
        
        caged_bunny_list.draw(screen)
        block_hit_list = pygame.sprite.spritecollide(player, key_list, False)
        for block in block_hit_list:
            key.move_key()
            key_collected = True
            
          
        block_hit_list = pygame.sprite.spritecollide(player, caged_bunny_list, False)
        for block in block_hit_list:
            pass
            if key_collected == True:
                caged_bunny.free()
            if key_collected == False:
                caged_bunny.get_the_key()
            

        
        if key_collected == False and player.change_x > 0:
            Key.key_move_x += player.change_x + 2
        elif key_collected == False and player.change_x < 0:
            Key.key_move_x += player.change_x - 2    
            
        
             

        Platform.platform_move_y = background_y_change
            
        background_y += background_y_change 
        
        if player.rect.x == width:
            Platform.platform_move_x += 3
        active_sprite_list.update()
        active_sprite_list.draw(screen)    
        if player.rect.x >= 1300 and key_collected == True:
            Constants.level = 2
            break
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
if __name__ == "__main__":
    level_three("white") 
    
