# Start of Setup
import pygame
pygame.init()
screen =  pygame.display.set_mode((600, 600))
running = True
# End of Setup

class ruut:
    def __init__(self, side_length):
        self.side_length = side_length

x = 0
while running:
    #               (where, (colour R,G,B), (xpos, ypos, xsize, ysize)
    if x > 60:
        x = 0
    else:
        x+=1
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 100, 100), (x, 30, 60, 60))
    for event in pygame.event.get():



    # Start of QUIT
        if event.type == pygame.QUIT:
            running = False
    # 1 frame
    pygame.display.update()
pygame.quit()
# End of QUIT