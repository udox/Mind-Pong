import random

import pygame
import pygame.locals as l
from pygame.locals import *


TITLE = "Mind Pong!"

class Player(object):
    def take_input(self, event):
        dy = random.randint(-2, 5)
        return dy

    def update(self, game):
        pass

class Game(object):
    pass

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    W, H = screen.get_size()
    print W, H
    pygame.display.set_caption(TITLE)

    # Fill background
    background = pygame.Surface((W, H))
    background = background.convert()
    background.fill((250, 250, 250))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()

    y = 20
    bat = Rect((10, y), (10, 100))
    # Event loop
    pygame.event.set_allowed([ACTIVEEVENT, NOEVENT, SYSWMEVENT, KEYDOWN, QUIT, JOYBUTTONDOWN])
    player = Player()
    while True:
        for event in pygame.event.get():
            #print [a for a in dir(l) if getattr(l, a)==event.type], event
            if event.type==QUIT:
                return
            if event.type==KEYDOWN and event.key in (K_q, K_ESCAPE):
                return

        time_passed = clock.tick(30) # in ms

        dy = player.take_input(None)
        y += dy
        print dy
        
        y = min(y, H - (10+100))
        y = max(y, 10)
        bat = Rect((10, y), (10, 100))
        print bat
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), bat)

        pygame.display.flip()


if __name__ == '__main__':
    main()
