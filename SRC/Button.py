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

        max_text_width = self.rect.width * 0.8  # 80% of button width
        font_size = self.font.size(self.text)
        while font_size[0] > max_text_width:
            self.font = pygame.font.Font(None, self.font.get_height() - 1)
            font_size = self.font.size(self.text)


        font_surface = self.font.render(self.text, True, (0, 0, 0))
        font_rect = font_surface.get_rect(midright=(self.rect.right - 5, self.rect.centery))

        screen.blit(font_surface, font_rect)
        if self.image:
            image_rect = self.image.get_rect()
            image_rect.topleft = (self.rect.left-10, self.rect.centery - image_rect.height // 2)
            screen.blit(self.image, image_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.function()
