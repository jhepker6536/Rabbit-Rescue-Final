#Imports 
import pygame 
from Player import Player_Falling,Missle, Snake_king
import Constants
from Platforms import Platform 
#Screen Size
width = 1366
hight = 768

#Level Five Function 
def level_five(color):
    pygame.init()
    #Creat the screen 
    screen = pygame.display.set_mode([width,hight], pygame.FULLSCREEN, 32)
    #Random veriables for snake position, mouse location, floor location, winning the game
    snake_x = 475
    snake_y = 8550
    mouse_x = 0
    mouse_y = 0
    floor_x = 0
    background_y_change = 0  
    missle_speed = -3
    game_won = False
    control = True
    #Creat Sprite groups 
    missle_list = pygame.sprite.Group() 
    active_sprite_list = pygame.sprite.Group()
    snake_list =pygame.sprite.Group()
    spike_list = []
    list_platform = []
    #Set the difficulty 
    if Constants.difficulty == "Easy":
        missle_speed = -14
    elif Constants.difficulty == "Medium":
        missle_speed = -17
    else:
        missle_speed = -18
    #Set the color for the function 
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
    #Create instences of the classes 
    player = Player_Falling(200,10,list_platform,True,player_color,hight,spike_list)
    missle = Missle(missle_speed)
    snake_king = Snake_king(snake_x,snake_y)
    #Add sprites to the groups 
    active_sprite_list.add(player,missle,snake_king)
    missle_list.add(missle)
    snake_list.add(snake_king)
    #Blitted Text
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    text11 = font2.render("Exit",True,Constants.RED)
    #Music 
    mute_button = pygame.image.load("Mute_Button.png")
    unmute_button = pygame.image.load("Muted_Button.png")
    sound_button = mute_button
    play_counter = 0
    pygame.mixer.music.load("BoxCat_Games_-_10_-_Epic_Song.wav")
    pygame.mixer.music.play(-1,0.0)
    #Clock variables
    frame_count = 0
    frame_rate = 60 
    clock = pygame.time.Clock()
    #Are we done
    done = False
    #Backgrounds 
    endscreen = pygame.image.load("Endscreen.png")
    background_image = pygame.image.load("SkyLevel.png")
    game_over_image = pygame.image.load("game over_bomb.png")
    background_y = 0
    
    while not done:
        for event in pygame.event.get(): 
            #DOES THE USER HIT A BUTTON 
            if event.type == pygame.KEYDOWN: 
                #Go left 
                if event.key == pygame.K_LEFT:
                    player.go_left()    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x >= 600:
                        done = True
                #go right
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                #jump 
                elif event.key == pygame.K_SPACE:
                    raise SystemExit
            #See if the user lifts up on the mouse button        
            elif event.type == pygame.KEYUP:
                #Stop moving 
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
                #Does the player hit quit 
                if mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                    done = True
                    raise SystemExit
                #Does the player hit play again 
                if mouse_x >= 598 and mouse_x <= 1100 and mouse_y >= 400 and mouse_y <= 460:
                    print("hit")
                    Constants.game_over = False
                    screen.blit(background_image,[0, background_y])
                    player.reset()
                    missle.reset()
                    snake_king.reset()
                    background_y = 0
                    player.gravity = False
                #deos the player hit mute   
                elif mouse_x >= 12 and mouse_x <= 97 and mouse_y >= 675 and mouse_y <= 775:
                        play_counter += 1 
                        if play_counter % 2 != 0:
                            pygame.mixer.music.pause()
                            sound_button = unmute_button
                        else:
                            pygame.mixer.music.play()
                            sound_button = mute_button    
                        
        #Create moving background
        screen.fill(Constants.WHITE)
        screen.blit(background_image, [0, background_y])
        if background_y > -8000:
            background_y -= 8
            snake_king.change_y -= 8
        else:
            missle.rect.x = 3000
            player.change_x = 0
            control = False
            player.rect.x = 400
            player.change_y = 3
            player.change_x = 1
        #Keep player on the screen     
        if player.rect.x <=0:
            player.rect.x = 0
        elif player.rect.x >= width - 100:
            player.rect.x = width - 100
        #quit
        screen.blit(text11, [1200,650])    
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
        #keep the floor under the map 
        if floor_x > 0:
            floor_x = -7
        #Is the player hit by a missle 
        block_hit_list = pygame.sprite.spritecollide(player,missle_list, False)
        for block in block_hit_list:
            snake_king.change_y = 0
            Constants.game_over = True
        #if missle goes off screen rest it to a new x and old y possiton
        if missle.rect.y <= -417:
            missle.reset() 
          
        background_y = background_y + background_y_change 
        #if the user won display winning screen 
        if game_won == False:
            active_sprite_list.update()
            active_sprite_list.draw(screen)
        elif game_won == True:
            active_sprite_list.remove() 
        #When the user hits the king snake go threw ending annimation 
        block_hit_list = pygame.sprite.spritecollide(player,snake_list, False)
        for block in block_hit_list:
            snake_king.die()
            player.change_y = 0 
            total_seconds = frame_count // frame_rate
            seconds = total_seconds % 60
            frame_count += 1 
            if seconds >= 1:
                game_won = True
                Constants.game_over = True
                
        #if the user dies what happens    
        if Constants.game_over == True and game_won == False:
            screen.blit(game_over_image,[0,0])  
        if Constants.game_over == True and game_won == True:
            screen.blit(endscreen, [0,0])
               
        screen.blit(sound_button,[12,700])
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    level_five("Blue")
