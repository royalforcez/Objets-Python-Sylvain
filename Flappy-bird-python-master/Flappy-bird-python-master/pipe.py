from pygame.sprite import Sprite
from pygame.locals import pygame
import random

# variables
SCREEN_HEIGHT = 600
GAME_SPEED = 15

PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 150

class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted, xpos, ysize)->None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))


        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize


        self.mask = pygame.mask.from_surface(self.image)


    def update(self)->None:
        self.rect[0] -= GAME_SPEED
    
    def get_random_pipes(xpos:int)->tuple:
        size = random.randint(100, 300)
        pipe = Pipe(False, xpos, size)
        pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
        return pipe, pipe_inverted