import pygame

import settings
from ui import screen

Image = pygame.Surface
flip = pygame.display.flip


def fill(color):
    screen.fill(color)


# принимает размеры картинки в координатах лабиринта
def load_image(path, size=(1, 1)):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (size[0] * settings.tile_size[0], size[1] * settings.tile_size[1]))

def draw_image(image, x, y):
    """Отрисовка изображения с учетом смещения и размера тайлов"""
    screen_x = int(x * settings.tile_size[0] + settings.view_left_top[0])
    screen_y = int(y * settings.tile_size[1] + settings.view_left_top[1])
    screen.blit(image, (screen_x, screen_y))

def draw_circle(color, x, y, r):
    """Отрисовка окружности с учетом масштабирования"""
    screen_x = int(x * settings.tile_size[0] + settings.view_left_top[0])
    screen_y = int(y * settings.tile_size[1] + settings.view_left_top[1])
    radius = int(r * settings.tile_size[0])
    pygame.draw.circle(screen, color, (screen_x, screen_y), radius)
