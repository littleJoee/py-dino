import pygame

class Entity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = pos
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'down': False}

        self.action = ''
        self.anim_offset = (0, 0)

    def update(self, y_floor=190, movement=(0, 0)):

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.pos[1] >= y_floor:
            self.collisions['down'] = True
        else:
            self.collisions['down'] = False

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

        if self.pos[1] >= y_floor:
            self.pos[1] = y_floor

        if self.collisions['down']:
            self.velocity[0] = 0

    def set_action(self, action):
        if self.action != action:
            self.action = action
            self.animation = self.game.asset[self.e_type + '/' + self.action].copy()

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def render(self, surf):
        surf.blit(self.game.assets['player/idle'], (self.pos[0], self.pos[1]))


class Cactus(Entity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'cactus', pos, size)

    def update(self, y_floor=190, movement=(0, 0)):
        return super().update(y_floor, movement)

class Player(Entity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.can_jump = True

    def update(self, movement, dead, y_floor=200):
        if not dead:
            super().update(movement=movement)
            if self.collisions['down'] == True:
                if not self.can_jump:
                    self.game.game_run = True
                self.can_jump = True
            else:
                self.can_jump = False
        else:
            pass
        
    def jump(self):
        if self.can_jump:
            self.velocity[1] = -3