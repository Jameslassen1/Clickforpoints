import pygame
from Button import Button



def function1():
  print("Button 1 clicked")


#def function2():
  #print("Button 2 clicked")

pygame.init()
screen = pygame.display.set_mode((400, 200))
#clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

button1 = Button(50, 50, 150, 50, (0, 255, 0), "Button 1", font, function1)
#button2 = Button(200, 50, 150, 50, (0, 0, 255), "Button 2", font, function2)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button1.handle_event(event)
        #button2.handle_event(event)

    button1.draw(screen)
    #button2.draw(screen)

    pygame.display.flip()
    #clock.tick(60)
    pygame.display.update()



