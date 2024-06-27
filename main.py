import pygame
from pygame.math import Vector2
import game
import button


pygame.init()
# rozmiary siatki gry
cell_size = 40
cell_number = 20
# tworzenie ekranu
screen_size = cell_number * cell_size
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Game of Snake")
clock = pygame.time.Clock()
# tworzenie gry
main_game = game.SnakeGame(screen, cell_size, cell_number)
# stany gry
game_paused = False
menu_state = "main"
# definicje czcionek
text_font = pygame.font.Font("font/pixel_digivolve/Pixel Digivolve.otf", 35)
TEXT_COLOR = (255, 255, 255)
# pobranie obrazków na przyciski
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
score_img = pygame.image.load("images/button_score.png").convert_alpha()
back_img = pygame.image.load("images/button_back.png").convert_alpha()

# tworzenie przycisków
resume_button = button.Button(304, 250, resume_img, 1)
score_button = button.Button(320, 375, score_img, 1)
quit_button = button.Button(336, 500, quit_img, 1)
back_button = button.Button(cell_size*cell_number - 200, cell_size*cell_number - 100, back_img, 1)


def draw_text(text, font, text_col, x, y):
    """Narysuj tekst na ekranie"""
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# szybkość poruszania węża
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 300)

# pętla gry
run = True

while run:
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    if game_paused:
        if menu_state == "main":
            # wyświetlanie menu
            if resume_button.draw_button(screen):
                game_paused = False
            if score_button.draw_button(screen):
                menu_state = "score"
            if quit_button.draw_button(screen):
                run = False
        if menu_state == "score":
            score_file = open("score.txt", "r")
            lines = score_file.readlines()
            score_file.close()
            text_x = 400
            text_y = 100
            for line in lines:
                draw_text(line, text_font, TEXT_COLOR, text_x, text_y)
                text_y += text_font.get_height() + 10
            if back_button.draw_button(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to pause", text_font, TEXT_COLOR, 40, 20)
    for event in pygame.event.get():
        # zamknięcie okna
        if event.type == pygame.QUIT:
            run = False
        # aktualizacja gry
        if event.type == SCREEN_UPDATE and not game_paused:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
            # zmiana kierunku
            if event.key == pygame.K_UP and int(main_game.snake.direction.y) != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and int(main_game.snake.direction.y) != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT and int(main_game.snake.direction.x) != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT and int(main_game.snake.direction.x) != 1:
                main_game.snake.direction = Vector2(-1, 0)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
