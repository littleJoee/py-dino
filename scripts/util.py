import os 

import pygame

BASE_IMG_PATH = 'data/images/'
def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

def draw_text(text, font, color, surf, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_obj, text_rect)
    

class Animation:
    def __init__(self):
        pass

    def copy(self):
        pass