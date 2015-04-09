#Imports 
import pygame 
from Player import Player, Key, Caged_Bunny,Bird
import Constants
from Platforms import Platform
#size variables for screen
width = 1366
hight = 768
#Level One function 
def level_one(color):
    pygame.init()
    #Creat the screen
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
    #Random Variables, checking key collection, mouse position, key position, and the floors starting point
    key_collected = False
    mouse_x = 0
    mouse_y = 0 
    key_x = 1740
    key_y = 300
    floor_x = 0  
    background_x_change = 0
    #tells level one what color to make the rabbit based on user choice
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
        
    
    #Create Sprite lists   
    caged_bunny_list = pygame.sprite.Group()
    platform_list = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    key_list = pygame.sprite.Group()
    
    #Creats Instences of platforms, player,caged bunny and the key 
    platform_test = Platform(floor_x,674,0)
    platform1 = Platform(400,450,1)
    platform2 = Platform(925,250,1)
    platform3 = Platform(1600,430,1)
    platform6 = Platform(2300,270,1)
    player = Player(25,400,platform_list,True,player_color, hight,spike_list=())
    caged_bunny = Caged_Bunny(3050,525,platform_list) 
    key = Key(key_x,key_y,player.change_x)
    
    #Music
    mute_button = pygame.image.load("Mute_Button.png")
    unmute_button = pygame.image.load("Muted_Button.png")
    sound_button = mute_button
    play_counter = 0
    pygame.mixer.music.load("BoxCat_Games_-_10_-_Epic_Song.wav")
    pygame.mixer.music.play()
    #Arrow image for instruction
    arrow_buttons = pygame.image.load("Buttons.png")
    arrow_buttons.set_colorkey(Constants.YELLOW)
    #Add instences to the appropriate list
    key_list.add(key)
    caged_bunny_list.add(caged_bunny)
    platform_list.add(platform_test, platform2, platform1,platform3,platform6)
    active_sprite_list.add(caged_bunny,player,platform_test,platform2,platform1,platform3,platform6,key)
    #Text
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    #Clock and are we done?
    clock = pygame.time.Clock()
    done = False
    #background
    background_image = pygame.image.load("field_background2.png")
    background_x = 0
    
    while not done:
        for event in pygame.event.get():
            #Check if the user hits a button 
            if event.type == pygame.KEYDOWN:
                #Move left
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    background_x_change += 2
                #Move Right
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                    background_x_change -= 2 
                #Jump
                elif event.key == pygame.K_SPACE:
                    player.jump()
            #Check if the user let go of button 
            elif event.type == pygame.KEYUP:
                #Stop Moving
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                    background_x_change = 0 
                #Stop Moving
                elif event.key == pygame.K_RIGHT:
                    player.stop()
                    background_x_change = 0 
                #Quit game
                elif event.type == pygame.QUIT:
                    done = True 
            #see if the user shuts off the music
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
                        
            
                                    
        #Creat Moving BAckground    
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [background_x, 0])
        if background_x > 0:
            background_x = -7
        background_x += background_x_change
        
        #Put instructional arrows on the screen
        if player.rect.x <= 300:
            screen.blit(arrow_buttons,[100,20])
        #Mouse 
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        
        #keep floor coverage
        if floor_x > 0:
            floor_x = -7
        #stop player from falling through the floor
        if player.rect.y <= 0:
            player.rect.y = 0 
        
        
        #DOes the player hit the key
        block_hit_list = pygame.sprite.spritecollide(player, key_list, False)
        for block in block_hit_list:
            key.move_key()
            key_collected = True
        #Does the player hit the cage with or without the key 
        block_hit_list = pygame.sprite.spritecollide(player, caged_bunny_list, False)
        for block in block_hit_list:
            pass
            if key_collected == True:
                caged_bunny.free()
            if key_collected == False:
                caged_bunny.get_the_key()
        #move the key with the player
        if key_collected == False and player.change_x > 0:
            Key.key_move_x += player.change_x + 2
        elif key_collected == False and player.change_x < 0:
            Key.key_move_x += player.change_x - 2    
        #move the other sprites with the player     
        if player.change_x > 0:
            Platform.platform_move_x += player.change_x + 2
            Caged_Bunny.Cage_move_x += player.change_x + 2     
        elif player.change_x < 0:
            Platform.platform_move_x += player.change_x - 2
            Caged_Bunny.Cage_move_x += player.change_x - 2
            
        if player.rect.x == width:
            Platform.platform_move_x += 3
        #Draw the sprites to the screen 
        active_sprite_list.update()
        active_sprite_list.draw(screen) 
        caged_bunny_list.draw(screen)
        #draw the exit and mute button 
        screen.blit(sound_button,[12,700])
        screen.blit(text11, [1200,710])
        
        #Does the user want to end the game or have they beat the level
        if Constants.game_over == True:
            break  
        if player.rect.x >= 1300 and key_collected == True:
            Constants.level = 2
            break
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
if __name__ == "__main__":
    level_one("White") 
    
