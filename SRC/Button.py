class Button: 
  xpos = 0
  ypos = 0
  wid = 0
  hei = 0
  r = 0
  g = 0
  b = 0
  bLable = ""
  def __init__(self, bLable= ''):
    self.bLable = bLable
    self.xpos = 0
    self.ypos = 0
    self.wid = 0
    self.hei = 0
    self.r= 0
    self.g= 0
    self.b= 0

  def draw(self, win, outline=None):
    # Call this method to draw the button on the screen
    if outline:
        pygame.draw.rect(win, outline, (self.xpos-2, self.ypos-2, self.wid+4, self.hei+4), 0)

    pygame.draw.rect(win, self.bLable, (self.xpos, self.ypos, self.wid, self.hei), 0)

    if self.bLable != '':
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.bLable, 1, (0, 0, 0))
        win.blit(text, (self.xpos + (self.wid/2 - text.get_width()/2), self.ypos + (self.hei/2 - text.get_height()/2)))
      
  def isOver(self, pos):

    if self.xpos < pos[0] < self.xpos + self.wid and self.ypos < pos[1] < self.ypos + self.hei:
      return True
    return False
