import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, font, function=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font
        self.function = function
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font_surface = self.font.render(self.text, True, (0, 0, 0))
        font_rect = font_surface.get_rect(center=self.rect.center)
        screen.blit(font_surface, font_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                if self.is_clicked(pos):
                    if self.function:
                        self.function()
