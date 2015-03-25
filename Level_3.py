import pygame 
from Player import Spikes, Snake_limits
from Player import Player_climber
from Player import Key
from Player import Caged_Bunny
from Player import Snake,Snake_limits
import Constants
from Platforms import Platform 
from os.path import sys
width = 1366
hight = 768


def level_three(color):
    pygame.init()
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
    mouse_x = 0  
    key_collected = False
    mouse_y = 0 
    key_x = 1000
    key_y = -2400
    floor_x = 0  
    caged_bunny_list = pygame.sprite.Group()
    platform_list = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    key_list = pygame.sprite.Group()
    spike_list = pygame.sprite.Group()
    snake_list = pygame.sprite.Group()
    
    if color == "Blue":
        player_color = Player_climber.blue_bunny
    elif color == "Brown":
        player_color = Player_climber.brown_bunny
    elif color == "Purple":
        player_color = Player_climber.purple_bunny
    elif color == "Green":
        player_color = Player_climber.green_bunny 
    elif color == "Yellow":
        player_color = Player_climber.yellow_bunny   
    elif color == "White":
        player_color = Player_climber.white_bunny
    elif color == "Pink":
        player_color = Player_climber.pink_bunny
    else:
        player_color = Player_climber.black_bunny
        
        
    platform_test = Platform(floor_x,674,0)
    platform1 = Platform(400,450,2)
    platform2 = Platform(700,250,2)
    platform3 = Platform(100,0,2)
    platform6 = Platform(700,-200,2)
    platform5 = Platform(200,-420,2)
    platform7 = Platform(800,-650,2)
    platform8 = Platform(300,-900,2)
    platform9 = Platform(100,-1200,2)
    platform10 = Platform(600,-1500,2)
    platform11 = Platform(100,-1800,2)
    platform12 = Platform(500,-2000,2)
    platform13 = Platform(900,-2300,2)
    platform14 = Platform(500,-2600,2)
    platform15 = Platform(000,-2800,2)
    platform16 = Platform(500,-3100,2)
    platform17 = Platform(900,-3400,2)
    platform18 = Platform(500,-3700,2)
    platform19 = Platform(0,-3900,2)
    platform20 = Platform(400,-4200,2)
    platform21 = Platform(800,-4400,2)
    platform22 = Platform(400,-4700,2)
    platform23 = Platform(100,-4900,2)
    
    snake = Snake(100,-75,100,475)
    snake2 = Snake(700,-275,700,1000)
    snake3 = Snake(800, -725,800,1175)
    snake4 = Snake(600, -1575,600,975)
    snake5 = Snake(500, -2075,500,875)
    snake6 = Snake(000, -2875,0,375)
    player2 = Player_climber(25,470,platform_list,True,player_color, hight,spike_list)
    caged_bunny = Caged_Bunny(150,-5035,platform_list) 
    key = Key(key_x,key_y,0)
    
    key_list.add(key)
    caged_bunny_list.add(caged_bunny)
    platform_list.add(platform_test,platform22,platform23,platform18,platform19,platform20,platform21, platform14,platform15,platform16,platform17, platform2,platform5,platform8,platform9,platform10,platform11,platform12, platform1,platform3,platform6,platform7,platform13)
    active_sprite_list.add(platform22,platform23,platform18,platform19,platform20,platform21,snake4,snake5,snake6,snake3,snake2,platform14,platform15,platform16,platform17,snake,caged_bunny,player2,platform_test,platform2,platform1,platform7,platform3,platform6,platform6,platform5,platform8,platform9,platform10,platform11,platform12,platform13,key)
    snake_list.add(snake,snake2,snake3,snake4,snake5,snake6)
    
    background_y_change = 0 
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    
    mute_button = pygame.image.load("Mute_Button.png")
    unmute_button = pygame.image.load("Muted_Button.png")
    sound_button = mute_button
    play_counter = 0
    pygame.mixer.music.load("BoxCat_Games_-_10_-_Epic_Song.wav")
    pygame.mixer.music.play(-1,0.0)
    
    screen_speed_a = 3
    screen_speed_b = 2
    if Constants.difficulty == "easy":
        screen_speed_a = 3
        screen_speed_b = 2
    elif Constants.difficulty == "medium":
        screen_speed_a = 5
        screen_speed_b = 3
    else:
        screen_speed_a = 5
        screen_speed_b = 3
    clock = pygame.time.Clock()
    done = False
    
    background_image = pygame.image.load("SkyLevel.png")
    game_over_image = pygame.image.load("game over.png")
    background_y = -8030
    
    while not done:
    
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player2.go_left()
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x >= 600:
                        done = True
                elif event.key == pygame.K_RIGHT:
                    player2.go_right()
                     
                elif event.key == pygame.K_SPACE:
                    player2.jump()
                    
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player2.change_x < 0:
                    player2.stop()
                    background_y_change = 0 
                elif event.key == pygame.K_RIGHT:
                    player2.stop()
                    background_y_change = 0 
                elif event.type == pygame.QUIT:
                    done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                    done = True
                    raise SystemExit
                if mouse_x >= 598 and mouse_x <= 1100 and mouse_y >= 400 and mouse_y <= 460:
                    print("hit")
                    Constants.game_over = False
                    screen.blit(background_image,[0,0])
                    player2.reset()
                    Platform.platform_move_y = 0 
                    Caged_Bunny.Cage_move_y = 0  
                    Key.key_move_y = 0
                    background_y = -8030
                    snake.rect.y = -75
                    snake2.rect.y = -275
                    snake3.rect.y = -725
                    snake4.rect.y = -1575
                    snake5.rect.y = -2075
                    snake6.rect.y = -2875
                elif mouse_x >= 12 and mouse_x <= 97 and mouse_y >= 675 and mouse_y <= 775:
                        play_counter += 1 
                        if play_counter % 2 != 0:
                            pygame.mixer.music.pause()
                            sound_button = unmute_button
                        else:
                            pygame.mixer.music.play()
                            sound_button = mute_button    
                    
                    

            
                                    
            
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [0, background_y])
        
        
        if player2.rect.x <=0:
            player2.rect.x = 0
        elif player2.rect.x >= width - 50:
            player2.rect.x = width - 50
        #quit
        screen.blit(text11, [1200,650])    
        pos = pygame.mouse.get_pos()
        if background_y > -20:
            background_y = -7
        if floor_x > 0:
            floor_x = -7
        mouse_x = pos[0]
        mouse_y = pos[1]
        print(key.rect.x)
        caged_bunny_list.draw(screen)
        block_hit_list = pygame.sprite.spritecollide(player2, key_list, False)
        for block in block_hit_list:
            key.move_key()
            key_collected = True
        if player2.rect.y <= 0:
            player2.rect.y = 0    
            
        block_hit_list = pygame.sprite.spritecollide(player2, caged_bunny_list, False)
        for block in block_hit_list:
            pass
            if key_collected == True:
                caged_bunny.free()
                
            if key_collected == False:
                caged_bunny.get_the_key()

            
        block_hit_list = pygame.sprite.spritecollide(player2, snake_list, False)
        for block in block_hit_list:
            Constants.game_over = True
        
          
            
        
            
        if background_y <= -20:    
            background_y_change = screen_speed_a
            Platform.platform_move_y += screen_speed_b
            Caged_Bunny.Cage_move_y -= screen_speed_b
            snake.change_y = screen_speed_b
            snake2.change_y = screen_speed_b
            snake3.change_y = screen_speed_b
            snake4.change_y = screen_speed_b
            snake5.change_y = screen_speed_b
            snake6.change_y = screen_speed_b
            key.key_move_y  = screen_speed_b
         
        if player2.rect.y >= 768:
            Constants.game_over = True
            
               
            
        background_y = background_y + background_y_change 
        
        if player2.rect.x == width:
            Platform.platform_move_x += 3
        active_sprite_list.update()
        active_sprite_list.draw(screen)  
        if Constants.game_over == True:
            screen.blit(game_over_image,[0,0])   
        if player2.rect.x >= 1300 and key_collected == True:
            Constants.level = 3 
            break   
        screen.blit(sound_button,[12,700])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    level_three("Purple")
