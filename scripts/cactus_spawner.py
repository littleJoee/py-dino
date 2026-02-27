import random



class Obstacles:
    '''
    for randomly spawning obstacles like the bird and cactus
    '''
    def __init__(self, assets):
        self.assets = assets
        self.obstacles = []
        self.spawn_timer = 1
        self.available_obstacles = [['cactus', (320 + 32, 200)], ['bird', [(320 + 32, 200), (320 + 32, 170), (320 + 32, 150)]]] # cactus, bird

    def update(self, game_speed):
        if self.spawn_timer == 0:
            self.spawn()
            self.spawn_timer = random.random() * 60
        else:
            self.spawn_timer -= 0.1

        for obstacle in self.obstacles.copy():
            obstacle['pos'][0] -= game_speed
            if obstacle['pos'][0] <= -self.img_width:
                self.obstacles.remove(obstacle)

    def spawn(self):
        choice = random.choice(self.available_obstacles)
        pos = random.choice(choice[1])
        
        self.obstacles.append([{'name': choice[0], 'pos': [pos[0], pos[1]]}])

    def render(self, surf):
        for obstacle in self.obstacles:
            surf.blit(self.assets[obstacle['name']], obstacle['pos'])