# more like UI than score

class Score:
    def __init__(self):
        self.score = 0
        self.add_speed = 0.1
    
    def update(self, dead):
        if not dead:
            self.score += self.add_speed

    def render(self, dead, surf):
        if not dead:
            # normal display of score on top right
            pass
        else:
            # game over score at end
            pass