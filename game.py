import pygame
import point
import snake


class SnakeGame:
    def __init__(self, screen, cell_size, cell_number):
        """Stwórz elementy gry"""
        self.screen = screen
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.snake = snake.Snake()
        self.point = point.Point(self.cell_number)
        self.score = 0
        self.score_font = pygame.font.Font("font/platinum_sign/Platinum Sign.ttf", 25)

    def update(self):
        """Zaktualizuj  przemieszcznie węża, punkty i sprawdź czy pzregrana gra"""
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        """Narysuj elementy gry"""
        self.draw_grass()
        self.snake.draw_snake(self.screen, self.cell_size)
        self.point.draw_normal_point(self.screen, self.cell_size)
        self.draw_score()

    def check_collision(self):
        """Sprawdź czy zdobyty punkt i wygeneruj nowy"""
        if self.point.pos == self.snake.body[0]:
            self.score += 1
            self.point.randomize(self.cell_number)
            self.snake.add_body()

        for block in self.snake.body[1:]:
            while block == self.point.pos:
                self.point.randomize(self.cell_number)

    def check_fail(self):
        """Sprawdź czy koniec gry"""
        if (not 0 <= self.snake.body[0].x < self.cell_number
                or not 0 <= self.snake.body[0].y < self.cell_number):
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        """Zresetuj stan węża i wyniki"""
        score_file = open("score.txt", "r")
        lines = score_file.readlines()
        score_file.close()

        for line in lines:
            if int(line) <= self.score:
                index = lines.index(line)
                lines.insert(index, str(self.score))
        score_file = open("score.txt", "w")
        score_file.write(str(lines))
        score_file.close()

        self.snake.reset()

    def draw_grass(self):
        """Narysuj trawe w kratkę"""
        grass_color = (167, 209, 61)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * self.cell_size,
                            row * self.cell_size,
                            self.cell_size,
                            self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * self.cell_size,
                            row * self.cell_size,
                            self.cell_size,
                            self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        """Narysuj aktualny wynik rozgrywki"""
        score_text = str(self.score)
        score_surface = self.score_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_number * self.cell_size - 60)
        score_y = int(40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        self.screen.blit(score_surface, score_rect)
