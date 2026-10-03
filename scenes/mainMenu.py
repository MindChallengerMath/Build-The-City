import pygame as pyg
pyg.init()

screen = pyg.display.set_mode((800, 400))

running = True
while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False