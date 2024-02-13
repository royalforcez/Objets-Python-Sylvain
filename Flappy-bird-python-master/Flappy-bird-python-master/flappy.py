import random
import time

from pipe import Pipe
from bird import Bird
from ground import Ground

from pygame.locals import *
from pygame.locals import pygame
from pygame.sprite import Sprite

# variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 20
GRAVITY = 2.5
GAME_SPEED = 15

GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT= 100


wing = 'assets/audio/wing.wav'
hit = 'assets/audio/hit.wav'

pygame.mixer.init()



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
BEGIN_IMAGE = pygame.image.load('assets/sprites/message.png').convert_alpha()

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()

for i in range (2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

pipe_group = pygame.sprite.Group()
for i in range (2):
    pipes = Pipe.get_random_pipes(SCREEN_WIDTH * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])



clock = pygame.time.Clock()

class Game :

    def __init__(self) -> None:
        self.ended = False
        self.start_screen = True

    def is_ended(self)->bool:
        return self.ended

    def update(self, clock: pygame.time.Clock)->None:
        if self.start_screen:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_UP:
                        bird.bump()
                        pygame.mixer.music.load(wing)
                        pygame.mixer.music.play()
                        self.start_screen = False
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_UP:
                        bird.bump()
                        pygame.mixer.music.load(wing)
                        pygame.mixer.music.play()
            bird_group.update()
            ground_group.update()
            pipe_group.update()
            pygame.display.update()

    def render(self)->None:
        if self.start_screen:
            screen.blit(BACKGROUND, (0, 0))
            screen.blit(BEGIN_IMAGE, (120, 150))

            if Ground.is_off_screen(ground_group.sprites()[0]):
                ground_group.remove(ground_group.sprites()[0])

                new_ground = Ground(GROUND_WIDTH - 20)
                ground_group.add(new_ground)

            bird.begin()
            ground_group.update()

            bird_group.draw(screen)
            ground_group.draw(screen)

            pygame.display.update()
        else:
            screen.blit(BACKGROUND, (0, 0))
            #scroll
            if Ground.is_off_screen(ground_group.sprites()[0]):
                ground_group.remove(ground_group.sprites()[0])

                new_ground = Ground(GROUND_WIDTH - 20)
                ground_group.add(new_ground)

            if Ground.is_off_screen(pipe_group.sprites()[0]):
                pipe_group.remove(pipe_group.sprites()[0])
                pipe_group.remove(pipe_group.sprites()[0])

                pipes = Pipe.get_random_pipes(SCREEN_WIDTH * 2)

                pipe_group.add(pipes[0])
                pipe_group.add(pipes[1])

            bird_group.draw(screen)
            pipe_group.draw(screen)
            ground_group.draw(screen)
            if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
                pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
                pygame.mixer.music.load(hit)
                pygame.mixer.music.play()
                time.sleep(1)
                self.ended = True


game = Game()
while not game.is_ended():
    
    clock.tick(15)
    game.update(clock)
    game.render()