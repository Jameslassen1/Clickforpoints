import pygame
import sys
from Button import Button
#Testing testing testing
pygame.init()
res = (750, 500)
screen = pygame.display.set_mode(res)

b1 = Button()
b1.xpos = 20
b1.ypos = 20
b1.wid = 100
b1.hei = 50
b1.bLable = "Button 1"
b1.r = 0
b1.g = 255
b1.b = 0

for ev in pygame.event.get():
  if ev.type == pygame.QUIT:
        pygame.quit()

      #checks if a mouse is clicked
  if ev.type == pygame.MOUSEBUTTONDOWN:

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[
            1] <= height / 2 + 40:
          score = score + 1

    # fills the screen with a color
    screen.fill((60, 25, 60))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()


    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[
        1] <= height / 2 + 40:
      pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
      pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    # superimposing the text onto our button
    screen.blit(text, (width / 2 + 39, height / 2 + 9))
    screen.blit(smallfont.render('pebbles: ' + str(score), True, color),
                (20, 10))
    # updates the frames of the game
    pygame.display.update()
