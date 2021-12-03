import pygame

class Player(object):
    def __init__(self, player_position, player_width, player_height, player_speed):
        self.player_rect = pygame.Rect(player_position[0], player_position[1], player_width, player_height)
        self.player_width = player_width
        self.player_height = player_height
        self.player_speed = player_speed
        self.player_bounds_x_min = self.player_rect.center[0]-player_width/2
        self.player_bounds_x_max = self.player_rect.center[0]+player_width/2
        self.player_bounds_y_min = self.player_rect.center[1]-player_height/2
        self.player_bounds_y_max = self.player_rect.center[1]+player_height/2

    def collide(self, opposing_obj_pos, opposing_obj_width, opposing_obj_height):
        if (opposing_obj_pos[0] >= self.player_bounds_x_min and opposing_obj_pos[0] < self.player_bounds_x_max)  and (opposing_obj_pos[1] >= self.player_bounds_y_min and opposing_obj_pos[1] < self.player_bounds_y_max):
            return True
        else:
            return False

    def drawPlayer(self, bounds, color):
        pygame.draw.rect(bounds, color, self.player_rect)




