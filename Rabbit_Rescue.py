# Imports 
import pygame 
import random 
from Player import Caged_Bunny,Key, Not_Moving_Bunny,Animated_Player
from Platforms import Platform
from Level_1 import level_one
from Level_2 import level_two
from Level_3 import level_three
from Level_4 import level_four
from Level_5 import level_five
import Constants
 

# Screen Size and creation
width = 1366
hight = 768
screen = pygame.display.set_mode((width, hight), pygame.FULLSCREEN, 32)
#Main Game Function 
def Rabbit_Rescue():
    """ Main function for the game. """
    pygame.init()   
    #Music
    pygame.mixer.music.load("BoxCat_Games_-_25_-_Victory.wav")
    pygame.mixer.music.play(1)  
    
    #Sprit Lists  
    active_sprite_list = pygame.sprite.Group()
    sitting_bunny_list = pygame.sprite.Group()
    #Stationary Bunnies for settings screen
    Brown_Bunny = Not_Moving_Bunny(0,100,200)
    Black_Bunny = Not_Moving_Bunny(1,300,200)
    Green_Bunny = Not_Moving_Bunny(2,500,200)
    Blue_Bunny = Not_Moving_Bunny(3,100,400)
    Purple_Bunny = Not_Moving_Bunny(4,300,400)
    
    #Created objects from Classes 
    running_bunny = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,False)
    running_bunny2 = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,False)
    running_bunny3 = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,True)
    running_bunny4 = Animated_Player(Animated_Player.bunny_list[random.randrange(0, 4)], width,True)
    
    #Add objects to sprite lists
    active_sprite_list.add(running_bunny,running_bunny2,running_bunny3,running_bunny4) 
    
    # All blitted Text
    font2 = pygame.font.SysFont('Calibri', 50, True, False)
    font = pygame.font.SysFont('Calibri', 70, True, False)
    text1 = pygame.image.load('PlayGameButton.png')
    text2 = pygame.image.load('Settingsbutton.png')
    text1.set_colorkey(Constants.WHITE)
    text2.set_colorkey(Constants.WHITE)
    text6 = font.render("<-BACK", True, Constants.RED)
    text7 = font2.render("DIFFICULTY", True, Constants.RED)
    text11 = font2.render("Exit", True, Constants.RED)
    COLOR4 = Constants.RED
    COLOR5 = Constants.RED
    COLOR6 = Constants.RED   
   
    
    # load logo screen
    logo = pygame.image.load('LOADER.png')
    title = pygame.image.load('title_logo.png')
    title.set_colorkey(Constants.WHITE) 
    
    # Loop until the user clicks the close button.
    done = False
    really_done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # What screen we see and background
    background_image = pygame.image.load("Field.png")
    background_image2 = pygame.image.load("Field_old_look.png")
    color_picker = pygame.image.load('Bunny_Chooser.png')
    color_picker.set_colorkey(Constants.YELLOW)
    screen_view = 0
    frame_count = 0
    frame_rate = 60 
    
    #Rabbit Box x & y for rabbit chooser settings screen
    r_box_x = 330
    r_box_y = 300
    
    #In game variables
    Constants.level = 1
    difficulty = "easy"
    color = "Green"
    
    
    # Parent while loop
    while not really_done:
        Constants.difficulty = difficulty
        # child loop containing loading screen!
        while screen_view == 0 and done == False:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True 
                    really_done = True  
                    
            # Background logo
            screen.fill(Constants.BLACK)
            screen.blit(logo, [0, 0])
            
            # count
            total_seconds = frame_count // frame_rate
            seconds = total_seconds % 60
            frame_count += 1 
            if seconds == 2:
                screen_view = 1
            # mouse
            
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            
            
            pygame.display.flip()
            # Limit to 60 frames per second
            clock.tick(frame_rate)            
            
        # child while loop, containing menu!
        while screen_view == 1 and done == False :
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True 
                    really_done = True
                # Do they hit the bottons and change mouse anamation
                elif event.type == pygame.MOUSEBUTTONDOWN:                   
                    if mouse_x >= 399 and mouse_x <= 917 and mouse_y >= 325 and mouse_y <= 416: 
                        #WHILE LOOPS THAT CREAT THE LEVELS 
                        #LEVEL ONE
                        while (Constants.level == 1) and Constants.game_over == False:
                            level_one(color)
                           
                            print(Constants.game_over)
                        #LEVEL TWO   
                        while (Constants.level == 2) and Constants.game_over == False:
                            Platform.platform_move_x = 0 
                            Caged_Bunny.Cage_move_x = 0 
                            Key.key_move_x = 0 
                            print(Constants.game_over)
                            level_two(color)  
                        #LEVEL THREE  
                        while (Constants.level == 3) and Constants.game_over == False:
                            Platform.platform_move_x = 0 
                            Caged_Bunny.Cage_move_x = 0 
                            Key.key_move_x = 0 
                            print(Constants.game_over)
                            level_three(color)
                        #LEVEL FOUR
                        while(Constants.level == 4) and Constants.game_over == False:
                            Platform.platform_move_x = 0 
                            Caged_Bunny.Cage_move_x = 0
                            Caged_Bunny.Cage_move_y = 0 
                            Key.key_move_x = 0
                            Platform.platform_move_y = 0
                            level_four(color)
                        #LEVEL fIVE
                        while(Constants.level == 5) and Constants.game_over == False: 
                            Caged_Bunny.Cage_move_x = 0 
                            Platform.platform_move_y = 0
                            level_five(color)
                    # DO THEY HIT THE SETTINGS BUTTON?        
                    elif mouse_x >= 398 and mouse_x <= 889 and mouse_y >= 450 and mouse_y <= 541:
                        print("and again setting")
                        screen_view = 4
                    #quit button
                    elif mouse_x >= 1199 and mouse_x <= 1249 and mouse_y >= 649 and mouse_y <= 778:
                        done = True
                        really_done = True                     
                   
                    
            # Background
            screen.blit(background_image, [0, 0])
            
            
            total_seconds = frame_count // frame_rate
            seconds = total_seconds % 60
            
            frame_count += 1
            # Creat Buttons
            screen.blit(title, [250, 100])            
            screen.blit(text1, [400, 300])
            screen.blit(text2, [400, 425])
            
            # quit
            screen.blit(text11, [1200, 650])
            
            
            # Creat Bunny
            active_sprite_list.draw(screen)
            active_sprite_list.update()
    
            # Chanage mouse pic
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            
            pygame.display.flip()
    
            # Limit to 20 frames per second
            clock.tick(frame_rate)

        
        # child while loop, containing setttings screen!
        while screen_view == 4 and done == False:
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT:
                        done = True
                        really_done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                          
                        if mouse_x >= 99 and mouse_x <= 370 and mouse_y >= 649 and mouse_y <= 730:
                            screen_view = 1
                        #difficuty                        
                        elif mouse_x >= 800 and mouse_x <= 890 and mouse_y >= 259 and mouse_y <= 308:
                            difficulty = "easy"
                        elif mouse_x >= 930 and mouse_x <= 1100 and mouse_y >= 259 and mouse_y <= 308:
                            difficulty = "medium"
                        elif mouse_x >= 1150 and mouse_x <= 1250 and mouse_y >= 259 and mouse_y <= 308:
                            difficulty = "hard"
                        
                        #Are we done
                        elif mouse_x >= 1200 and mouse_x <= 1300 and mouse_y >= 649 and mouse_y <= 798:
                            done = True
                            really_done = True 
                            
                        #color picker    
                        elif mouse_x >= 200 and mouse_x <= 300 and mouse_y >= 300 and mouse_y <= 390:
                            color = "Brown"
                            r_box_x = 205
                            r_box_y = 300
                        elif mouse_x >= 325 and mouse_x <= 425 and mouse_y >= 300 and mouse_y <= 390:
                            color = "Black"
                            r_box_x = 330
                            r_box_y = 300
                        elif mouse_x >= 455 and mouse_x <= 555 and mouse_y >= 300 and mouse_y <= 390:
                            color = "Green"
                            r_box_x = 455
                            r_box_y = 300
                        elif mouse_x >= 570 and mouse_x <= 670 and mouse_y >= 300 and mouse_y <= 390:
                            color = "Blue"
                            r_box_x = 570
                            r_box_y = 299
                        elif mouse_x >= 255 and mouse_x <= 355 and mouse_y >= 400 and mouse_y <= 490:
                            color = "Yellow"
                            r_box_x = 255
                            r_box_y = 400
                        elif mouse_x >= 370 and mouse_x <= 470 and mouse_y >= 400 and mouse_y <= 490:
                            color = "Purple"
                            r_box_x = 372
                            r_box_y = 403
                        elif mouse_x >= 495 and mouse_x <= 595 and mouse_y >= 400 and mouse_y <= 490:
                            color = "Pink"
                            r_box_x = 495
                            r_box_y = 403
                        elif mouse_x >= 600 and mouse_x <= 700 and mouse_y >= 400 and mouse_y <= 490:
                            color = "White"
                            r_box_x = 602
                            r_box_y = 407
                       
                                      
                    # Background
                    screen.fill(Constants.BLACK)
                    screen.blit(background_image2, [0, 0])
                    total_seconds = frame_count // frame_rate
                    seconds = total_seconds % 60
                    #difficulty chooser 
                    if difficulty == "easy":
                        COLOR4 = Constants.WHITE
                        COLOR5 = Constants.RED
                        COLOR6 = Constants.RED
                    elif difficulty == "medium":
                        COLOR5 = Constants.WHITE
                        COLOR4 = Constants.RED
                        COLOR6 = Constants.RED
                    else:
                        COLOR6 = Constants.WHITE
                        COLOR4 = Constants.RED
                        COLOR5 = Constants.RED
                    frame_count += 1                   
                    # Creat Buttons for bunny chooser
                    sitting_bunny_list.draw(screen)
                    
                    
                    #button s for difficulty 
                    screen.blit(color_picker, [200,300])                    
                    text8 = font2.render("EASY", True, COLOR4)
                    text9 = font2.render("MEDIUM", True, COLOR5)
                    text10 = font2.render("HARD", True, COLOR6) 
                    text12 = font2.render("Pick Your Rabbit", True, Constants.RED)                   
                    screen.blit(text6, [100, 650])
                    screen.blit(text7, [900, 200])
                    screen.blit(text8, [800, 260])
                    screen.blit(text9, [930, 260])
                    screen.blit(text10, [1150, 260])
                    screen.blit(text11, [1200, 650])
                    screen.blit(text12, [300, 200])
                   
                    #box around bunny that is choosen 
                    pygame.draw.rect(screen, Constants.WHITE, [r_box_x, r_box_y, 100,95],3)
                    # Change mouse
                    pos = pygame.mouse.get_pos()
                    mouse_x = pos[0]
                    mouse_y = pos[1] 
                    
                    pygame.display.update()
                    pygame.display.flip()
                
                    # Limit to 20 frames per second
                    clock.tick(frame_rate)  
    
                    
    clock.tick(frame_rate)
    pygame.quit()    
            
                    
if __name__ == "__main__":
    Rabbit_Rescue()
