import pygame as pyg
pyg.init()

screen = pyg.display.set_mode((800, 400))

pyg.display.set_caption("Build The City")
icon = pyg.image.load("images/Icon.png")
pyg.display.set_icon(icon)

running = True
while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    screen.fill((66, 63, 63))
    screen.convert
    pyg.display.update()