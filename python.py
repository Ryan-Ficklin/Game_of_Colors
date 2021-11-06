# importing libraries
import pygame
import time
import random
 
snake_speed = 15
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(100, 0, 100)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Game of Colors')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
player_width = 50;
player_height = 50;
player_position = [100, 50]

 
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,random.randrange(1, (window_y//10)) * 10]

 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
# Main Function
while True:
    #creating player and fruit rectangles before any use of them
    player_rect = pygame.Rect(player_position[0], player_position[1], player_width, player_height)
    fruit_rect = pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)

    # handling key events, the commented out direct position changes are to debug with incremental movement instead of continuous
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
                #player_position[1] -= 10
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
                #player_position[1] += 10
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
                #player_position[0] -= 10
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                #player_position[0] += 10
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        player_position[1] -= 10
    if direction == 'DOWN':
        player_position[1] += 10
    if direction == 'LEFT':
        player_position[0] -= 10
    if direction == 'RIGHT':
        player_position[0] += 10
 
    # if fruits and snakes collide then scores
    # will be incremented by 10
    player_bounds_x_min = player_rect.center[0]-player_width/2
    player_bounds_x_max = player_rect.center[0]+player_width/2
    player_bounds_y_min = player_rect.center[1]-player_height/2
    player_bounds_y_max = player_rect.center[1]+player_height/2
    if (fruit_position[0] >= player_bounds_x_min and fruit_position[0] < player_bounds_x_max)  and (fruit_position[1] >= player_bounds_y_min and fruit_position[1] < player_bounds_y_max):
        score += 10
        fruit_spawn = False
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(purple)
     
    

    pygame.draw.rect(game_window, red, fruit_rect)
    pygame.draw.rect(game_window, black, player_rect)
 
    # Game Over conditions
    if player_position[0] < 0 or player_position[0] > window_x-10:
        game_over()
    if player_position[1] < 0 or player_position[1] > window_y-10:
        game_over()
 
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)
    #print(player_bounds_x_min, player_bounds_x_max, player_bounds_y_min, player_bounds_y_max, fruit_position)
    
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refres Rate
    fps.tick(snake_speed)
