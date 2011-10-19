import pygame
from pygame.locals import *

TITLE = "Mind Pong!"

class Player(object):
    def take_input(self, event):
        pass
    def update(self, game):
        pass

class Game(object):
    pass

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption(TITLE)

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render(TITLE, 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()


    # Event loop
    i = 0
    while True:
        for event in pygame.event.get():
            print event
            if event.type==QUIT:
                return
            if event.type==KEYDOWN and event.key in (K_q, K_ESCAPE):
                return

        i += 1
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
