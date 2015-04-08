import pygame 

from Player import Player_Falling, Bird,Missle
import Constants
from Platforms import Platform 

width = 1366
hight = 768


def level_five(color):
    pygame.init()
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
    mouse_x = 0
    mouse_y = 0 
    floor_x = 0 
    
    bird_list = pygame.sprite.Group() 
    active_sprite_list = pygame.sprite.Group()
    spike_list =[]
    list_platform = []
    
    missle_speed = -3 
    if Constants.difficulty == "Easy":
        missle_speed = -3
    elif Constants.difficulty == "Medium":
        missle_speed = -5
    else:
        missle_speed = -8

    if color == "Blue":
        player_color = Player_Falling.blue_bunny
    elif color == "Brown":
        player_color = Player_Falling.brown_bunny
    elif color == "Purple":
        player_color = Player_Falling.purple_bunny
    elif color == "Green":
        player_color = Player_Falling.green_bunny 
    elif color == "Yellow":
        player_color = Player_Falling.yellow_bunny   
    elif color == "White":
        player_color = Player_Falling.white_bunny
    elif color == "Pink":
        player_color = Player_Falling.pink_bunny
    else:
        player_color = Player_Falling.black_bunny
        
        
    
    player = Player_Falling(200,10,list_platform,True,player_color,hight,spike_list)
    missle = Missle(missle_speed)
    bird1 = Bird(1000,300)
    active_sprite_list.add(player,bird1,missle)
    bird_list.add(bird1)
    
    background_y_change = 0 
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    
    mute_button = pygame.image.load("Mute_Button.png")
    unmute_button = pygame.image.load("Muted_Button.png")
    sound_button = mute_button
    play_counter = 0
    pygame.mixer.music.load("BoxCat_Games_-_10_-_Epic_Song.wav")
    pygame.mixer.music.play(-1,0.0)
    
    clock = pygame.time.Clock()
    done = False
    
    background_image = pygame.image.load("SkyLevel.png")
    game_over_image = pygame.image.load("game over_bird.png")
    background_y = 0
    
    while not done:
    
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x >= 600:
                        done = True
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                     
                    
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                    player.direction = "S"
                    background_y_change = 0 
                elif event.key == pygame.K_RIGHT:
                    player.stop()
                    player.direction = "S"
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
                    screen.blit(background_image,[0, background_y])
                    player.reset()
                    bird1.reset()
                    background_y = 0
                    
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
        player.rect.y += .5
        
        if player.rect.x <=0:
            player.rect.x = 0
        elif player.rect.x >= width - 50:
            player.rect.x = width - 50
        #quit
        screen.blit(text11, [1200,650])    
        pos = pygame.mouse.get_pos()
        if background_y > -8000:
            background_y -= 12
        if floor_x > 0:
            floor_x = -7
        mouse_x = pos[0]
        mouse_y = pos[1]    
            
        block_hit_list = pygame.sprite.spritecollide(player, bird_list, False)
        for block in block_hit_list:
            Constants.game_over = True
        
        if player.rect.y >= 768:
            break
        if missle.rect.y == -417:
            missle.reset()   
        background_y = background_y + background_y_change 
        
        if player.rect.x == width:
            Platform.platform_move_x += 3
        active_sprite_list.update()
        active_sprite_list.draw(screen)
        
          
        if Constants.game_over == True:
            screen.blit(game_over_image,[0,0])    
               
        screen.blit(sound_button,[12,700])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    level_five("Green")
