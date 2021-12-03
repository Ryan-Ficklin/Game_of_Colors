# importing libraries
import pygame
import time
import random
from Player import Player
 
snake_speed = 15 #
 
# Window size
window_x = 900
window_y = 650
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(100, 0, 100)
gray = pygame.Color(100, 100, 100)
 
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

fruit_position = [random.randrange(1, (window_x//10)) * 10,random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
direction = ""
score = 0
 
# displaying Score function
def show_score(color, font, size):
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

def show_intro(color, font, size):
    intro_font = pygame.font.SysFont(font, size)
    intro_surface = intro_font.render("Press any arrow key to begin", True, color)
    intro_rect = intro_surface.get_rect()
    intro_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(intro_surface, intro_rect)

 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, white)
     
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
    player_rect = Player(player_position, player_width, player_height, snake_speed)
    fruit_rect = pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)

    # handling key events, the commented out direct position changes are to debug with incremental movement instead of continuous
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
                #player_position[1] -= 10
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
                #player_position[1] += 10
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
                #player_position[0] -= 10
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
                #player_position[0] += 10
 
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
    if (player_rect.collide(fruit_position, 10, 10)):
        score += 10
        fruit_spawn = False
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(gray)
     
    

    pygame.draw.rect(game_window, red, fruit_rect)
    player_rect.drawPlayer(game_window, black)
 
    # Game Over conditions
    
 
    # displaying score countinuously
    if(direction == ""):
        show_intro(white, 'comic sans', 40)

    show_score(white, 'times new roman', 20)
    #print(player_bounds_x_min, player_bounds_x_max, player_bounds_y_min, player_bounds_y_max, fruit_position)
    
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refres Rate
    fps.tick(snake_speed)
