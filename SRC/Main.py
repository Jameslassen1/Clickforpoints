import pygame
from Button import Button
from miner import Miner
Miner.power =0
score = 0
Miner1 = Miner("Miner",10,1)

#def function1():
  #global score
  #score += 1
  #print(score)


def function2():
  Miner1.power += 1
  print("Miner1 power:",Miner1.power)
  print("Button 2 clicked")

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

button_image = pygame.image.load('temprock.gif')

button_image = pygame.transform.scale(button_image, (150, 50))

# Create a function that displays the button image on the screen
def draw_button(screen):
    screen.blit(button_image, (50, 50))

#button1 = Button(200, 200, 150, 50, (150,150,150), None,None, function1, draw_button)
button2 = Button(400,20, 150, 50, (0, 0, 255), "miner 1", font, function2)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #button1.handle_event(event)
        button2.handle_event(event)

    #button1.draw(screen)
    button2.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()



