import pygame as pyg
import time
pyg.init()

screen = pyg.display.set_mode((800, 400))

pyg.display.set_caption("Build The City")
icon = pyg.image.load("images/Icon.png")
pyg.display.set_icon(icon)

#Buttons
lightStartButton = pyg.image.load("images/startButtonBTC.png")
darkStartButton = pyg.image.load("images/darkStartButtonBTC.png")

lightExitButton = pyg.image.load("images/exitButtonBTC.png")
darkExitButton = pyg.image.load("images/darkExitButtonBTC.png")
def button():
    pass

startButtonImg = lightStartButton
exitButtonImg = lightExitButton
startButtonX = 300
startButtonY = 200

exitButtonX = 600
exitButtonY = 200
#Tried def start(): 
# if pyg.mouse.get_pos() == startButtonX: 
#       startButtonImg = darkStartButton
class start(pyg.sprite.Sprite):
    def __init__(self):
        pass
    mouseCoord = pyg.mouse.get_pos()
    
    if mouseCoord[0] == startButtonX:
       startButtonImg = darkStartButton
    
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
    start()
    #mouseCoord = pyg.mouse.get_pos()
    #if mouseCoord[0] == startButtonX:
    #    startButtonImg = darkStartButton
    displayButtons()
    
    #This updates the screen
    pyg.display.update()