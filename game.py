import sys

import pygame

from scripts.util import load_image, load_images, draw_text
from scripts.entities import Player
from scripts.road import Road
from scripts.clouds import Clouds

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("dino game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player/idle' : load_image('player/idle/01.png'),
            'road': load_image('road.png'),
            'clouds': load_images('clouds'),
            'big_menu_font': pygame.font.Font('data/font/monogram.ttf', 64),
        }

        self.player = Player(self, [50, 200], [32, 18])
        self.road = Road(self, 200, 2)
        self.clouds = Clouds(self.assets['clouds'])

        self.x_scroll = 2
        self.dead = 0
        self.game_run = True
        self.menu = True

    def run(self):
        while True:
            self.display.fill((255, 255, 255))

            if self.menu:
                draw_text('PY DINO', self.assets['big_menu_font'], (0, 0, 0), self.display, 160, 100)

            self.clouds.update()
            self.clouds.render(self.display)

            self.road.update(self.game_run)
            self.road.render(self.display)

            self.player.update((self.movement[1] - self.movement[0], 0), self.dead)
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.menu = False
                        self.player.jump()
                    if event.key == pygame.K_UP:
                       self.menu = False
                       self.player.jump()
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
                    

Game().run()