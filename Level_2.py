#Imports
import pygame 
from Player import Spikes, Player,Key,Caged_Bunny,Snake
import Constants
from Platforms import Platform
#Screen Size variables
width = 1366
hight = 768


def level_two(color):
    pygame.init()
    #Creat the screen
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
    #Random Variables, Mouse position, key position, key collection,floor position
    mouse_x = 0
    mouse_y = 0 
    key_collected = False
    key_x = 1940
    key_y = 100
    floor_x = -400 
    background_x_change = 0 
    #Sprite Groups  
    caged_bunny_list = pygame.sprite.Group()
    platform_list = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    key_list = pygame.sprite.Group()
    spike_list = pygame.sprite.Group()
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
        
    #Creats Instences of platforms, player,caged bunny,spikes, and the key   
    platform_test = Platform(floor_x,674,0)
    platform1 = Platform(400,450,1)
    platform2 = Platform(1200,450,1)
    platform3 = Platform(1800,230,1)
    platform6 = Platform(2400,400,1)
    player2 = Player(25,400,platform_list,True,player_color, hight,spike_list)
    spike = Spikes(755,580)
    spike2 = Spikes(736,580)
    spike3 = Spikes(1536,580)
    spike4 = Spikes(1555,580)
    caged_bunny = Caged_Bunny(3050,525,platform_list) 
    key = Key(key_x,key_y,player2.change_x)
    #Add instences to the appropriate list
    key_list.add(key)
    caged_bunny_list.add(caged_bunny)
    platform_list.add(platform_test, platform2, platform1,platform3,platform6)
    active_sprite_list.add(spike3,spike4,spike2,caged_bunny,player2,platform_test,platform2,platform1,platform3,platform6,key,spike)
    spike_list.add(spike,spike3,spike4,spike2)
    
    #blitted text
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    #clock and are we done?
    clock = pygame.time.Clock()
    done = False
    #Music
    mute_button = pygame.image.load("Mute_Button.png")
    unmute_button = pygame.image.load("Muted_Button.png")
    sound_button = mute_button
    pygame.mixer.music.load("BoxCat_Games_-_25_-_Victory.wav")
    pygame.mixer.music.play()
    play_counter = 0
    #Death Screen
    game_over_image = pygame.image.load("game over.png")
    #Background
    background_image = pygame.image.load("Forest Background2.png")
    background_x = -100
    #main loop 
    while not done:
    
        for event in pygame.event.get():
            #Check if the user hits a button
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Player died and hit play again 
                if mouse_x >= 598 and mouse_x <= 1100 and mouse_y >= 400 and mouse_y <= 460:
                    print("hit")
                    Constants.game_over = False
                    screen.blit(background_image,[0,0])
                    player2.reset()
                    Platform.platform_move_x = 0 
                    Caged_Bunny.Cage_move_x = 0 
                    spike.spike_move_x = 0 
                    spike2.spike_move_x = 0
                    spike3.spike_move_x = 0
                    spike4.spike_move_x = 0 
                    Key.key_move_x = 0
                #Player uses mute button 
                elif mouse_x >= 12 and mouse_x <= 97 and mouse_y >= 675 and mouse_y <= 775:
                        play_counter += 1 
                        if play_counter % 2 != 0:
                            pygame.mixer.music.pause()
                            sound_button = unmute_button
                        else:
                            pygame.mixer.music.play()
                            sound_button = mute_button
                #User hits quit
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                    done = True
                    raise SystemExit 
            elif event.type == pygame.KEYDOWN:
                #Move left
                if event.key == pygame.K_LEFT:
                    player2.go_left()
                    background_x_change += 2
                #move right
                elif event.key == pygame.K_RIGHT:
                    player2.go_right()
                    background_x_change -= 2 
                #jump
                elif event.key == pygame.K_SPACE:
                    player2.jump()
            #Check if the user let go of button
            elif event.type == pygame.KEYUP:
                #stop moving
                if event.key == pygame.K_LEFT and player2.change_x < 0:
                    player2.stop()
                    background_x_change = 0 
                elif event.key == pygame.K_RIGHT:
                    player2.stop()
                    background_x_change = 0 
                elif event.type == pygame.QUIT:
                    done = True 
                                  

        #Creat Moving BAckground    
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [background_x, 0])
        if background_x > 0:
            background_x = -7
        background_x += background_x_change
        #Keep player on the screen
        if player2.rect.x <=0:
            player2.rect.x = 0
        if player2.rect.y <= 0:
            player2.rect.y = 0 
        #QUit button 
        screen.blit(text11, [1200,650])    
        #mouse
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        #Keep floor coverage
        if floor_x > 0:
            floor_x = -7
        #DOes the player hit the key
        block_hit_list = pygame.sprite.spritecollide(player2, key_list, False)
        for block in block_hit_list:
            key.move_key()
            key_collected = True
        #Does the player hit the cage with or without the key  
        block_hit_list = pygame.sprite.spritecollide(player2, caged_bunny_list, False)
        for block in block_hit_list:
            pass
            if key_collected == True:
                caged_bunny.free()
            if key_collected == False:
                caged_bunny.get_the_key()
        #move the key with the player
        if key_collected == False and player2.change_x > 0:
            Key.key_move_x += player2.change_x + 2
        elif key_collected == False and player2.change_x < 0:
            Key.key_move_x += player2.change_x - 2    
        #move the other sprites with the player    
        if player2.change_x > 0:
            Platform.platform_move_x += player2.change_x + 2
            Caged_Bunny.Cage_move_x += player2.change_x + 2
            spike.spike_move_x += player2.change_x + 2
            spike2.spike_move_x += player2.change_x + 2
            spike3.spike_move_x += player2.change_x + 2
            spike4.spike_move_x += player2.change_x + 2
        elif player2.change_x < 0:
            Platform.platform_move_x += player2.change_x - 2
            Caged_Bunny.Cage_move_x += player2.change_x - 2
            spike.spike_move_x += player2.change_x - 2
            spike2.spike_move_x += player2.change_x - 2
            spike3.spike_move_x += player2.change_x - 2
            spike4.spike_move_x += player2.change_x - 2
            
        Snake.snake_screen_adjust = player2.change_x 
        background_x += background_x_change 
        
        if player2.rect.x == width:
            Platform.platform_move_x += 3
        #Draw the sprites to the screen    
        active_sprite_list.update()
        caged_bunny_list.draw(screen)
        active_sprite_list.draw(screen)  
        screen.blit(sound_button,[12,700])
        #Does the user want to end the game or have they beat the level
        if Constants.game_over == True:
            screen.blit(game_over_image,[0,0])   
        if player2.rect.x >= 1300 and key_collected == True:
            Constants.level = 3 
            break   
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    level_two("Purple")
