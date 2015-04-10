#Imports 
import pygame 
from Player import Player, Key, Caged_Bunny
import Constants
from Platforms import Platform
#size variables for screen
width = 1366
hight = 768
#Level four function 
def level_four(color):
    pygame.init()
    #Creat the Screen
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
     #Random Variables, checking key collection, mouse position, key position, and the floors starting point
    mouse_x = 0
    mouse_y = 0 
    key_collected = False
    key_x = 2000
    key_y = 350
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
    #Creat Sprites Lists  
    caged_bunny_list = pygame.sprite.Group()
    platform_list = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    key_list = pygame.sprite.Group()
    #Creats Instences of platforms, player,caged bunny and the key 
    platform_test = Platform(0,650,3)
    platform1 = Platform(400,470,3)
    platform2 = Platform(935,300,3)
    platform3 = Platform(1400,630,3)
    platform6 = Platform(2200,630,3)
    platform7 = Platform(2800, 460,3)
    player = Player(25,400,platform_list,True,player_color, hight,spike_list=())
    caged_bunny = Caged_Bunny(2870,314,platform_list) 
    key = Key(key_x,key_y,player.change_x)
    #Music
    mute_button = pygame.image.load("Mute_Button.png")
    unmute_button = pygame.image.load("Muted_Button.png")
    sound_button = mute_button
    play_counter = 0
    pygame.mixer.music.load("BoxCat_Games_-_10_-_Epic_Song.wav")
    pygame.mixer.music.play()
    #Add instences to the sprite groups 
    key_list.add(key)
    caged_bunny_list.add(caged_bunny)
    platform_list.add(platform_test,platform2,platform7,platform1,platform3,platform6)
    active_sprite_list.add(caged_bunny, platform7, player,platform_test,platform2,platform1,platform3,platform6,key)
    #Blitted text
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    #death screen 
    game_over_image = pygame.image.load("game over_falling.png")
    #Clock and are we done
    clock = pygame.time.Clock()
    done = False
    #background
    background_image = pygame.image.load("Space_Level.png")
    background_x = -20
     
    #main while loop
    while not done:
        for event in pygame.event.get():
            #Check if the user hits any buttons
            if event.type == pygame.KEYDOWN:
                #move left
                if event.key == pygame.K_LEFT:
                    player.go_left()
                    background_x_change += 2
                    #move right
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                    background_x_change -= 2 
                #jump
                elif event.key == pygame.K_SPACE:
                    player.jump()
            #Check if the user lef go of the button 
            elif event.type == pygame.KEYUP:
                #stop 
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                    background_x_change = 0 
                elif event.key == pygame.K_RIGHT:
                    player.stop()
                    background_x_change = 0 
                elif event.type == pygame.QUIT:
                    done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Does the user hit the end button 
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 710 and mouse_y <= 778:
                    done = True
                    raise SystemExit
                #Does the user hit the mute button 
                elif mouse_x >= 12 and mouse_x <= 97 and mouse_y >= 675 and mouse_y <= 775:
                        play_counter += 1 
                        if play_counter % 2 != 0:
                            pygame.mixer.music.pause()
                            sound_button = unmute_button
                        else:
                            pygame.mixer.music.play()
                            sound_button = mute_button
                #does the user die and hit play again 
                elif mouse_x >= 598 and mouse_x <= 1100 and mouse_y >= 400 and mouse_y <= 460:
                    print("hit")
                    Constants.game_over = False
                    screen.blit(background_image,[0,0])
                    player.reset()
                    Platform.platform_move_x = 0 
                    Caged_Bunny.Cage_move_x = 0 
                    Key.key_move_x = 0
                        
            
                                    
        #Creat Moving background    
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [background_x, 0])
        if background_x > 0:
            background_x = -7
        background_x += background_x_change 
        #Mouse    
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        #Keep the floor covered 
        if floor_x > 0:
            floor_x = -7
        #keep the player on the level 
        if player.rect.y <= 0:
            player.rect.y = 0
        #Does the player hit the key 
        block_hit_list = pygame.sprite.spritecollide(player, key_list, False)
        for block in block_hit_list:
            key.move_key()
            key_collected = True
        #Does the player hit the cage
        block_hit_list = pygame.sprite.spritecollide(player, caged_bunny_list, False)
        for block in block_hit_list:
            pass
            if key_collected == True:
                caged_bunny.free()
            if key_collected == False:
                caged_bunny.get_the_key()   
        #Move the sprites with the player    
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
        #keep the player on the platform 
        if player.rect.x == width:
            Platform.platform_move_x += 3
        #Draw spritesd to the screen     
        active_sprite_list.update()
        active_sprite_list.draw(screen)
        caged_bunny_list.draw(screen)
        #Blit text 
        screen.blit(sound_button,[12,700])
        screen.blit(text11, [1200,710])
        #if they fall game over screen 
        if key_collected == False and player.rect.y >= 738:
            Constants.game_over = True   
        if Constants.game_over == True:
            screen.blit(game_over_image,[0,0])  
        #The player reached the end of the level     
        if player.rect.x >= 1170:
            print("hit")
            Constants.level = 5 
            break   
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
if __name__ == "__main__":
    level_four("White") 
    
