import pygame
<<<<<<< HEAD
from Button import Button

score = 0

def function1():
  score= score+1
    print("Button 1 clicked")

def function2():
    print("Button 2 clicked")
=======
import sys
from Buttons import Button
>>>>>>> aa9860a63ac591975e96971c4e226c5c2c4c09d5

pygame.init()
screen = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

button1 = Button(50, 50, 150, 50, (0, 255, 0), "Button 1", font, function1)
button2 = Button(200, 50, 150, 50, (0, 0, 255), "Button 2", font, function2)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button1.handle_event(event)
        button2.handle_event(event)

    button1.draw(screen)
    button2.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
