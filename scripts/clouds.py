import random

class Cloud:
    def __init__(self, pos, speed, img, depth=16):
        self.pos = pos
        self.speed = speed
        self.img = img
        self.depth = depth

        self.screen_width = 320

    def update(self):
        self.pos[0] -= self.speed
        if self.pos[0] < -self.img.get_width():
            self.pos[0] = self.screen_width

    def render(self, surf):
        surf.blit(surf, (self.pos[0], self.pos[1]))

class Clouds:
    def __init__(self, cloud_images, count=16):
        self.clouds = []
        for i in range(count):
            self.clouds.append(Cloud([random.random() * 99999, random.random() * 99999], random.random() * 0.5 + 0.5, random.choice(cloud_images), random.random() * 0.6 + 0.2))

        self.clouds.sort(key=lambda x: x.depth)
        print(self.clouds)


    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def render(self, surf):
        for cloud in self.clouds:
            cloud.render(surf) 