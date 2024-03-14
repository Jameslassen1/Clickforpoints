import pygame
from Button import Button
from miner import Miner
from ImageButton import ImageButton

score = 0
clickPower = 1
Miner1 = Miner("Miner", 10, 0, 0)
Tnt = Miner("TNT", 100, 0, 0)
sDrill = Miner("StoneDrill", 1000, 0, 0)
Drill = Miner("Drill", 10000, 0, 0)
DDrill = Miner("DimondDrill", 100000, 0, 0)
PDrill = Miner("PlatnumDrill", 1000000, 0, 0)


play = False

# Initialize timer variables
current_time = 0
timer_interval = 100

def pebbleclick():
    global score
    score += clickPower
    print(score)

def function1():
    global score
    if score >= Miner1.cost:
        score -=  Miner1.cost
        Miner1.power += 1
        Miner1.amount += 1
        Miner1.cost = round(10 * ((1.25) ** Miner1.amount))
        print("Miner1 power:", Miner1.power)
        print("Miner1 Amount:", Miner1.amount)
        print("Miner1 cost:", Miner1.cost)

def function2():
    global score
    if score >= Tnt.cost:
        score = score - Tnt.cost
        Tnt.power += 10
        Tnt.amount += 1
        Tnt.cost = round(100 * ((1.25) ** Tnt.amount))
        print("TNT power:", Tnt.power)
        print("TNT Amount:", Tnt.amount)
        print("TNT cost:", Tnt.cost)

def function3():
    global score
    if score >= sDrill.cost:
        score = score - sDrill.cost
        sDrill.power += 100
        sDrill.amount += 1
        sDrill.cost = round(1000 * ((1.25) ** sDrill.amount))
        print("StoneDrill power:", sDrill.power)
        print("StoneDrill Amount:", sDrill.amount)
        print("StoneDrill cost:", sDrill.cost)

def function4():
    global score
    if score >= Drill.cost:
        score -= Drill.cost
        Drill.power += 1000
        Drill.amount += 1
        Drill.cost = round(10000 * ((1.25) ** Drill.amount))
        print("Drill power:", Drill.power)
        print("Drill Amount:", Drill.amount)
        print("Drill cost:", Drill.cost)

def function5():
    global score
    if score >= DDrill.cost:
        score = score - DDrill.cost
        DDrill.power += 10000
        DDrill.amount += 1
        DDrill.cost = round(100000 * ((1.25) ** DDrill.amount))
        print("Drill power:", DDrill.power)
        print("Drill Amount:", DDrill.amount)
        print("Drill cost:", DDrill.cost)

def function6():
    global score
    if score >= PDrill.cost:
        score-= PDrill.cost
        PDrill.power += 100000
        PDrill.amount += 1
        PDrill.cost = round(1000000 * ((1.25) ** PDrill.amount))
        print("Drill power:", PDrill.power)
        print("Drill Amount:", PDrill.amount)
        print("Drill cost:", PDrill.cost)

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None,20)

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
SDrill = pygame.image.load("images/EthanStoneDrill.png")
Idrill = pygame.image.load("images/EthanDrill.png")
Ddrill = pygame.image.load("images/EthanDiamondDrill.png")
Pdrill = pygame.image.load("images/EthanPlatinumDrill.png")

pebblebutton1 = ImageButton(100, 300, pebblebutton1_image, pebbleclick)
button1 = Button(400, 20, 200, 90, (128,128,128), f"{Miner1.cost}", font, function1, MinerImage)
button2 = Button(400, 100, 200, 90, (128,128,128), "TNT", font, function2, TNT)
button3 = Button(400, 180, 200, 90, (128,128,128), "Stone Drill", font, function3, SDrill)
button4 = Button(400, 260, 200, 90, (128,128,128), "Drill", font, function4, Idrill)
button5 = Button(400, 340, 200, 90, (128,128,128), "Drill", font, function5, Ddrill)
button6 = Button(400, 420, 200, 90, (128,128,128), "Drill", font, function6, Pdrill)

# Main game loop
while play:
  
    screen.fill((255, 255, 255))
    pebblescore = font.render(f"Score: {score}", True, (0, 0, 0))
    allminers = Miner1.power + Tnt. power + sDrill.power + Drill.power + DDrill.power + PDrill.power
    minerpow = font2.render(f"+{allminers}/s", True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        pebblebutton1.handle_event(event)
        button1.handle_event(event)
        button2.handle_event(event)
        button3.handle_event(event)
        button4.handle_event(event)
        button5.handle_event(event)
        button6.handle_event(event)


    # Check the elapsed time for the timer
    current_time += clock.get_rawtime()
    clock.tick()
    
    # Update score every second
    if current_time >= timer_interval:
        score += allminers
        print(f"Score: {score}")
        current_time = 0

    pebblebutton1.draw(screen)
    button1.text = f"Miner ({Miner1.cost})"
    button1.draw(screen)

    button2.text = f"TNT ({Tnt.cost})"
    button2.draw(screen)

    button3.text = f"Stone Drill ({sDrill.cost})"
    button3.draw(screen)

    button4.text = f"Drill ({Drill.cost})"
    button4.draw(screen)

    button5.text = f"Diamond Drill ({DDrill.cost})"
    button5.draw(screen)

    button6.text = f"Platinum Drill ({PDrill.cost})"
    button6.draw(screen)

    screen.blit(pebblescore,(10,10))
    screen.blit(minerpow,(10,40))




    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
