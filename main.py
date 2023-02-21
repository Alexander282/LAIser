import pygame

screen =  pygame.display.set_mode((600, 600))

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()