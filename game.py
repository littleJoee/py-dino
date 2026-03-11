import sys

import pygame

from scripts.util import load_image, load_images, draw_text, Animation
from scripts.entities import Player
from scripts.road import Road
from scripts.clouds import Clouds
from scripts.cactus_spawner import Obstacles
from scripts.score_ui import Score

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("dino game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240), pygame.SRCALPHA)
        self.display_2 = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player/idle' : Animation(load_image('player/idle/01.png')),
            'player/run' : Animation(load_images('player/run'), 8),
            'player/jump' : Animation(load_images('player/jump')),
            'player/crouch/run' : Animation(load_images('player/crouch/run')),
            'player/crouch/jump' : Animation(load_images('player/crouch/jump')),
            'player/hit' : Animation(load_images('player/hit')),
            'player/death' : Animation(load_images('player/death')),
            'road': load_image('road.png'),
            'clouds': load_image('clouds/0.png'),
            'big_menu_font': pygame.font.Font('data/font/monogram.ttf', 64),
            'mono': pygame.font.Font('data/font/monogram.ttf', 13),
            'score': pygame.font.Font('data/font/monogram.ttf', 16),
            'cactus': load_image('obstacles/cactus.png'),
            'bird': load_images('obstacles/bird'),
            'game_over': load_image('game_over.png'),
        }

        self.player = Player(self, [50, 200], [32, 18])
        self.spawner = Obstacles(self.assets)

        self.road = Road(self, 200, 2)     

        self.clouds = Clouds(self.assets['clouds'])

        self.score_ui = Score(self.assets['score'])

        self.x_scroll = 2
        self.dead = 0
        self.game_run = True
        self.game_speed = 2
        self.menu = False
        self.game_over_timer = 0
        self.transition = False

    def revive(self):
         self.dead = False
         self.score_ui.reset()
         self.spawner = Obstacles(self.assets)

    def run(self):
        while True:
            self.display.fill((255, 255, 255))

            if self.dead:
                self.game_speed = 0
                self.game_over_timer = max(100, self.game_over_timer + 1)
            else:
                self.game_speed = 2

            self.clouds.update(self.dead)
            self.clouds.render(self.display)

            self.road.update(self.game_speed)
            self.road.render(self.display)

            self.spawner.update(self.game_speed)
            self.spawner.render(self.display)

            self.player.update((self.movement[1] - self.movement[0], 0), self.dead)

            for obstacle_rect in self.spawner.obstacle_rects():
                if self.player.rect().collidepoint(obstacle_rect[0], obstacle_rect[1]):
                    self.dead += 1
                    self.transition = True
                    
            self.score_ui.update(self.dead)
            self.score_ui.render(self.display, self.display_2)

            if self.dead:
                self.display.fill((0, 0, 0))

            self.display_2.blit(self.display, (0, 0))
            self.player.render(self.display_2)
            

            if self.game_over_timer > 60:
                self.display_2.blit(self.assets['game_over'], (160, 100))
                draw_text('PRESS SPACE TO RESTART', self.assets['mono'], (255, 255, 255), self.display_2, 130, 230)

                #draw_text('PY DINO', self.assets['big_menu_font'], (0, 0, 0), self.display, 160, 100)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.menu = False
                        self.player.jump(self.dead)
                    if event.key == pygame.K_UP:
                       self.menu = False
                       self.player.jump(self.dead)
                    if event.key == pygame.K_DOWN:
                        self.player.crouch(self.dead)
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player.uncrouch()
                    if event.key == pygame.K_UP and self.dead:
                         self.run()
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display_2, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
                    

Game().run()