import pygame


class Button:
    def __init__(self, x, y, image, scale):
        """Stwórz guzik pasujący do obrazka"""
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_button(self, surface):
        """Narysuj guzik"""
        action = False
        # pobierz pozycje myszki
        pos = pygame.mouse.get_pos()

        # sprawdź warunek kliknięcia
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # narysuj guzik
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
