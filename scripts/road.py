class Road:
    def __init__(self, game, floor_y, scroll_speed=2):
        self.game = game
        self.scroll_speed = scroll_speed
        self.screen_width = 320
        self.road_x1 = 0
        self.road_x2 = self.screen_width
        self.floor_y = floor_y


    def update(self, game_run):
        if game_run:
            self.road_x1 -= self.scroll_speed
            self.road_x2 -= self.scroll_speed

            if self.road_x1 <= -self.screen_width:
                self.road_x1 = self.screen_width
            if self.road_x2 <= -self.screen_width:
                self.road_x2 = self.screen_width

        

    def render(self, surf):
        surf.blit(self.game.assets['road'], (self.road_x1, self.floor_y))
        surf.blit(self.game.assets['road'], (self.road_x2, self.floor_y))