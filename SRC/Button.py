#James L

import pygame
import sys

class Button:
    #setting the variable for the button position size color and word on the button
    def __init__(self, x, y, width, height, color, text, font, function, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font
        self.function = function
        self.image = image
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font_surface = self.font.render(self.text, True, (0, 0, 0))
        font_rect = font_surface.get_rect(center=self.rect.center)
        screen.blit(font_surface, font_rect)
        if self.image:
            screen.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.is_clicked(pos):
                    if self.function:
                        self.function()
