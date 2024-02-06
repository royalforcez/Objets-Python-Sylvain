from pygame.sprite import Sprite
from pygame.locals import pygame

# variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 20
GRAVITY = 2.5


class Bird(pygame.sprite.Sprite):

    def __init__(self)->None:
        pygame.sprite.Sprite.__init__(self)

        self.images =  [pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
                        pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                        pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()]

        self.SPEED = SPEED

        self.current_image = 0
        self.image = pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 6
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self)->None:
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.SPEED += GRAVITY

        # update height
        self.rect[1] += self.SPEED

    def bump(self)->None:
        self.SPEED = -SPEED

    def begin(self)->None:
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
