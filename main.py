# Start of Setup
import pygame
pygame.init()
screen =  pygame.display.set_mode((600, 600))
running = True
# End of Setup

while running:
    pygame.display.update()
    for event in pygame.event.get():



    # Start of QUIT
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
# End of QUIT