# James L and Cannon U

import pygame
from Button import Button
from miner import Miner
from ImageButton import ImageButton
Miner.power =0
score = 0
Miner1 = Miner("Miner",10,0,0)
TNT = Miner("TNT",100,0,0)
play = False
def function1():
  global score
  score += 1
  print(score)


def function2():
  Miner1.power += 1
  Miner1.amount += 1
  Miner1.cost = round(10*(1.25) ** Miner1.amount)
  print("Miner1 power:",Miner1.power)
  print("Miner1 Amount:", Miner1.amount)
  print("Miner1 cost:",Miner1.cost)

def function3():
  TNT.power += 10
  TNT.amount += 1
  print("TNT power:",TNT.power)
  print("TNT Amount:", TNT.amount)

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
while not play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True
            
    screen.fill((255, 255, 255))

    welcome = font.render("Welcome to Pebbles", True, (0, 0, 0))
    screen.blit(welcome, (150, 250))

    begin_text = font.render("Click anywhere to start", True, (0, 0, 0))
    screen.blit(begin_text, (150, 300))

    pygame.display.flip()

    # Check for mouse click to start the game
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            play = True

      
button1_image = pygame.image.load("images/rock.png")
MinerImage = pygame.image.load("images/EthanViking_Miner.png")
TNT = pygame.image.load("images/EthanTNT-1.png")

button1 = ImageButton(100,300, button1_image, function1)
button2 = Button(400,20, 150, 50, (0, 0, 255), "Miner", font, function2, MinerImage)
button3 = Button(400,80, 150, 50, (0, 0, 255), "TNT", font, function3, TNT)


while play:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        button1.handle_event(event)
        button2.handle_event(event)
        button3.handle_event(event)

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()



