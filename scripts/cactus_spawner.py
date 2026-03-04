import random
from pygame import Rect

class Obstacles:
    '''
    for randomly spawning obstacles like the bird and cactus
    '''
    def __init__(self, assets):
        self.assets = assets
        self.obstacles = []
        self.img_width = 32
        self.spawn_timer = random.random()
        self.available_obstacles = [['cactus', (320 + 32, 190)], ['bird', [(320 + 32, 200), (320 + 32, 170), (320 + 32, 150)]]] # cactus, bird

        self.frame = 0

    def obstacle_rects(self):
        rects = []
        for obstacle in self.obstacles:
            rects.append(Rect(obstacle['pos'][0], obstacle['pos'][1], 16, 16)) # (32, 18): obstacle size
        return rects

    def update(self, game_speed):
        self.spawn_timer -= 0.1
        self.frame = (self.frame + 0.1) % 2


        if self.spawn_timer <= 0:
            self.spawn()
            self.spawn_timer = random.random() * 60

        for obstacle in self.obstacles.copy():
            obstacle['pos'][0] -= game_speed
            if obstacle['pos'][0] <= -self.img_width:
                self.obstacles.remove(obstacle)

    def spawn(self):
        choice = self.available_obstacles[0]
        if choice[0] == 'bird':
            pos = random.choice(choice[1])
        else:
            pos = choice[1]
        
        self.obstacles.append({'name': choice[0], 'pos': list(pos)})

    def render(self, surf):
        for obstacle in self.obstacles:
            if self.assets[obstacle['name']] == 'bird':
                surf.blit(self.assets[obstacle['name']][int(self.frame)], obstacle['pos'])
            else:
                surf.blit(self.assets[obstacle['name']], obstacle['pos'])