import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        """Stwórz węża początkowego"""
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self, screen, cell_size):
        """Narysuj segmenty węża"""
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 255), snake_rect)

    def move_snake(self):
        """Przesuń  segmenty węża w danym kierunku"""
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_body(self):
        """Powiększ weża o jeden segment"""
        self.new_block = True

    def reset(self):
        """Zresetuj ustawienia węża"""
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
