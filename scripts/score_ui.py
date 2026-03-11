from scripts.util import draw_text
# more like UI than score

class Score:
    def __init__(self, font):
        self.score = 0
        self.score_speed = 0.1
        self.font = font
        self.score_assets = []
        self.dead = False
    
    def update(self, dead):
        self.dead = dead
        if not dead:
            self.score += self.score_speed

    def reset(self):
        self.score = 0
        self.score_speed = 0.1

    def render(self, surf, surf_2):
        if not self.dead:
            draw_text(str(int(self.score)), self.font, (0, 0, 0), surf, 0, 0)
            # normal display of score on top right
        else:
            # game over score at end
            draw_text(str(int(self.score)), self.font, (255, 255, 255), surf, 160, 120)