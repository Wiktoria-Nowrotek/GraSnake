import pygame
import random
from pygame.math import Vector2


class Point:
    def __init__(self, cell_number):
        """Stwórz pozycje x i y"""
        self.randomize(cell_number)

    def draw_normal_point(self, screen, cell_size):
        """Narysuj kółko w odpowiedniej pozycji"""
        r = int(cell_size/2)
        vector = Vector2(int(self.pos.x * cell_size + r), int(self.pos.y * cell_size + r))
        pygame.draw.circle(screen, (255, 0, 0), vector, r, r)

    def randomize(self, cell_number):
        """Stwórz nowy losowy punkt"""
        self.cell_number = cell_number
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
