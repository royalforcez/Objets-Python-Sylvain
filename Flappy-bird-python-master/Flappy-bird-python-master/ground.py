from pygame.locals import pygame
from pygame.sprite import Sprite


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GAME_SPEED = 15
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT= 100


class Ground(pygame.sprite.Sprite):
    
    def __init__(self, xpos)->None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT
    def update(self)->None:
        self.rect[0] -= GAME_SPEED

    def is_off_screen(sprite:Sprite) -> Sprite:
        return sprite.rect[0] < -(sprite.rect[2])