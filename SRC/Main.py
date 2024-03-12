import pygame
from Button import Button
from miner import Miner
from ImageButton import ImageButton

score = 0
Miner1 = Miner("Miner", 10, 0, 0)
Tnt = Miner("TNT", 100, 0, 0)
sDrill = Miner("StoneDrill", 1000, 0, 0)
Drill = Miner("Drill", 10000, 0, 0)


play = False

# Initialize timer variables
current_time = 0
timer_interval = 100

def pebbleclick():
    global score
    score += 1
    print(score)

def function1():
    Miner1.power += 1
    Miner1.amount += 1
    Miner1.cost = round(10 * ((1.25) ** Miner1.amount))
    print("Miner1 power:", Miner1.power)
    print("Miner1 Amount:", Miner1.amount)
    print("Miner1 cost:", Miner1.cost)

def function2():
    Tnt.power += 10
    Tnt.amount += 1
    Tnt.cost = round(100 * ((1.25) ** Tnt.amount))
    print("TNT power:", Tnt.power)
    print("TNT Amount:", Tnt.amount)
    print("TNT cost:", Tnt.cost)

def function3():
    sDrill.power += 100
    sDrill.amount += 1
    sDrill.cost = round(1000 * ((1.25) ** sDrill.amount))
    print("StoneDrill power:", sDrill.power)
    print("StoneDrill Amount:", sDrill.amount)
    print("StoneDrill cost:", sDrill.cost)

def function4():
    Drill.power += 1000
    Drill.amount += 1
    Drill.cost = round(10000 * ((1.25) ** Drill.amount))
    print("Drill power:", Drill.power)
    print("Drill Amount:", Drill.amount)
    print("Drill cost:", Drill.cost)

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Main game loop
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

# Create buttons and timer
pebblebutton1_image = pygame.image.load("images/EthanRock.png")
MinerImage = pygame.image.load("images/EthanViking_Miner.png")
TNT = pygame.image.load("images/EthanTNT-1.png")

pebblebutton1 = ImageButton(100, 300, pebblebutton1_image, pebbleclick)
button1 = Button(400, 20, 200, 90, (0, 0, 255), "Miner", font, function1, MinerImage)
button2 = Button(400, 140, 200, 90, (0, 0, 255), "TNT", font, function2, TNT)
button3 = Button(400, 260, 200, 90, (0, 0, 255), "Stone Drill", font, function3, TNT)
button4 = Button(400, 380, 200, 90, (0, 0, 255), "Drill", font, function4, TNT)

# Main game loop
while play:
  
    screen.fill((255, 255, 255))
    pebblescore = font.render(f"Score: {score}", True, (0, 0, 0))
    allminers = Miner1.power + Tnt. power + sDrill.power + Drill.power
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        pebblebutton1.handle_event(event)
        button1.handle_event(event)
        button2.handle_event(event)
        button3.handle_event(event)
        button4.handle_event(event)


    # Check the elapsed time for the timer
    current_time += clock.get_rawtime()
    clock.tick()
    
    # Update score every second
    if current_time >= timer_interval:
        score += allminers
        print(f"Score: {score}")
        current_time = 0

    pebblebutton1.draw(screen)
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)

    screen.blit(pebblescore,(10,10))



    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
