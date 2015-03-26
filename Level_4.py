import pygame 
from Player import Player, Key, Caged_Bunny
import Constants
from Platforms import Platform


 
width = 1366
hight = 768


def level_four(color):
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
        player_color = Player.yellow_bunny   
    elif color == "White":
        player_color = Player.white_bunny
    elif color == "Pink":
        player_color = Player.pink_bunny
    else:
        player_color = Player.black_bunny
        
    
        
    caged_bunny_list = pygame.sprite.Group()
    platform_list = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    key_list = pygame.sprite.Group()
     
    platform_test = Platform(floor_x,700,3)
    platform1 = Platform(400,450,3)
    platform2 = Platform(925,250,3)
    platform3 = Platform(1600,430,3)
    platform6 = Platform(2400,250,3)
    platform7 = Platform(3000, 670,3)
    player = Player(25,400,platform_list,True,player_color, hight,spike_list=())
    caged_bunny = Caged_Bunny(3170,524,platform_list) 
    key = Key(key_x,key_y,player.change_x)
    
    #snake limits
    
    mute_button = pygame.image.load("Mute_Button.png")
    unmute_button = pygame.image.load("Muted_Button.png")
    sound_button = mute_button
    play_counter = 0
    
    key_list.add(key)
    caged_bunny_list.add(caged_bunny)
    platform_list.add(platform_test,platform2,platform7,platform1,platform3,platform6)
    active_sprite_list.add(caged_bunny, platform7, player,platform_test,platform2,platform1,platform3,platform6,key)
    
    background_x_change = 0
    pygame.mixer.music.load("BoxCat_Games_-_10_-_Epic_Song.wav")
    pygame.mixer.music.play()
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    game_over_image = pygame.image.load("game over.png")
    
    clock = pygame.time.Clock()
    done = False
    background_image = pygame.image.load("Space_Level.png")
    background_x = -20
     
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    background_x_change += 2
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                    background_x_change -= 2 
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
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 710 and mouse_y <= 778:
                    done = True
                    raise SystemExit
                elif mouse_x >= 12 and mouse_x <= 97 and mouse_y >= 675 and mouse_y <= 775:
                        play_counter += 1 
                        if play_counter % 2 != 0:
                            pygame.mixer.music.pause()
                            sound_button = unmute_button
                        else:
                            pygame.mixer.music.play()
                            sound_button = mute_button
                elif mouse_x >= 598 and mouse_x <= 1100 and mouse_y >= 400 and mouse_y <= 460:
                    print("hit")
                    Constants.game_over = False
                    screen.blit(background_image,[0,0])
                    player.reset()
                    Platform.platform_move_x = 0 
                    Caged_Bunny.Cage_move_x = 0 
                    Key.key_move_x = 0
                        
            
                                    
            
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [background_x, 0])
        
        #quit
        print(play_counter)    
        pos = pygame.mouse.get_pos()
        if background_x > 0:
            background_x = -7
        if floor_x > 0:
            floor_x = -7
        if player.rect.y <= 0:
            player.rect.y = 0 
        mouse_x = pos[0]
        mouse_y = pos[1]
        
        caged_bunny_list.draw(screen)
        block_hit_list = pygame.sprite.spritecollide(player, key_list, False)
        for block in block_hit_list:
            key.move_key()
            key_collected = True
        if player.rect.y >= 768:
            Constants.game_over = True   
          
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
            
        if player.change_x > 0:
            Platform.platform_move_x += player.change_x + 2
            Caged_Bunny.Cage_move_x += player.change_x + 2
            
            
             
        elif player.change_x < 0:
            Platform.platform_move_x += player.change_x - 2
            Caged_Bunny.Cage_move_x += player.change_x - 2
            
        background_x += background_x_change 
        
        if player.rect.x == width:
            Platform.platform_move_x += 3
        active_sprite_list.update()
        active_sprite_list.draw(screen) 
        screen.blit(sound_button,[12,700])
        screen.blit(text11, [1200,710])
        if Constants.game_over == True:
            screen.blit(game_over_image,[0,0])  
        if player.rect.x >= 1500 and key_collected == True:
            Constants.level = 2
            break
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
if __name__ == "__main__":
    level_four("White") 
    
