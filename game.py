import sys

import pygame

from scripts.util import load_image, load_images

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("dino game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.movement = [False, False]

        self.assets = {
            'player/idle' : load_image('01')
        }

        self.x_scroll = 0

    def run(self):
        while True:
            self.display.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_SPACE:
                        self.movement[0] = True
                    if event.type == pygame.K_UP:
                        self.movement[0] = True
                    if event.type == pygame.K_w:
                        self.movement[0] == True
                    if event.type == pygame.K_DOWN:
                        self.movement[1] = True
                    if event.type == pygame.K_s:
                        self.movement[1] == True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.movement[0] = False
                    if event.type == pygame.K_UP:
                        self.movement[0] = False
                    if event.type == pygame.K_w:
                        self.movement[0] == False
                    if event.type == pygame.K_DOWN:
                        self.movement[1] = False
                    if event.type == pygame.K_s:
                        self.movement[1] == False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
                    

Game().run()