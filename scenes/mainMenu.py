import pygame as pyg
pyg.init()

screen = pyg.display.set_mode((800, 400))

pyg.display.set_caption("Build The City")
icon = pyg.image.load("images/Icon.png")
pyg.display.set_icon(icon)

#Buttons
startButtonImg = pyg.image.load("images/startButtonBTC.png")
exitButtonImg = pyg.image.load("images/exitButtonBTC.png")
startButtonX = 300
startButtonY = 200

exitButtonX = 600
exitButtonY = 200
def displayButtons():
    screen.blit(startButtonImg, (startButtonX, startButtonY))
    screen.blit(exitButtonImg, (exitButtonX, exitButtonY))


running = True
while running:
    #For every event check to see
    #if the player hit the quit button
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.fill((66, 63, 63))
    displayButtons()
    
    #This updates the screen
    pyg.display.update()