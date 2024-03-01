import pygame
from Button import Button

score = 0

def function1():
  global score
  score += 1
  print(score)


def function2():
  print("Button 2 clicked")

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

button1 = Button(200, 200, 150, 50, (150,150,150), "rock", font, function1)
button2 = Button(400,20, 150, 50, (0, 0, 255), "miner 1", font, function2)

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
    pygame.display.update()



