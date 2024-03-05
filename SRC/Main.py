# James L and Cannon U

import pygame
from Button import Button
from miner import Miner
from ImageButton import ImageButton
Miner.power =0
score = 0
Miner1 = Miner("Miner",10,0,0)

def function1():
  global score
  score += 1
  print(score)


def function2():
  Miner1.power += 1
  Miner1.amount += 1
  print("Miner1 power:",Miner1.power)
  print("Miner1 Amount:", Miner1.amount)
  print("Button 2 clicked")

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

button1_image = pygame.image.load("images/rock.png")
MinerImage = pygame.image.load("images/EthanViking_Miner.png")

button1 = ImageButton(300,300, button1_image, function1)
button2 = Button(400,20, 150, 50, (0, 0, 255), "miner 1", font, function2, MinerImage)

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



