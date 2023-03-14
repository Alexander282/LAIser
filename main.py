# Start of Setup
import pygame
pygame.init()
screen =  pygame.display.set_mode((600, 600))
running = True
# End of Setup
pygame.display.set_caption("LAIser")
class ruut:
    def __init__(self, side_length):
        self.side_length = side_length


#picture = pygame.image.load("folder/name.png").conver_alpha
#screen.blit(picture, (x,y))

x = 0
y = 0

def borderedSquare(x, y, r,g,b,width,height,borderSize):
    colors = [r, g, b]
    pygame.draw.rect(screen, (r,g,b), (x, y, width, height))
    r2 = r-20
    if r2<0:
        r2 = 0
    g2 = g - 20
    if g2 < 0:
        g2 = 0
    b2 = b - 20
    if b2 < 0:
        b2 = 0

    pygame.draw.rect(screen, (r2,g2,b2), (x, y, borderSize, height))
    pygame.draw.rect(screen, (r2, g2, b2), (x, y, width, borderSize))
    r3 = r + 20
    if r3 > 255:
        r3 = 255
    g3 = g + 20
    if g3 > 255:
        g3 = 255
    b3 = b + 20
    if b3 > 255:
        b3 = 255
    pygame.draw.rect(screen, (r3,g3,b3), (x+width-borderSize, y, borderSize, height))
    pygame.draw.rect(screen, (r3, g3, b3), (x, y+height-borderSize, width, borderSize))


while running:
    #               (where, (colour R,G,B), (xpos, ypos, xsize, ysize)
    screen.fill((128,128,128))

    for xgrid in range(10):
        for ygrid in range(10):
            pygame.draw.rect(screen, (190,190,190), (xgrid*60+5, ygrid*60+5, 50, 50))
    borderedSquare(x, y, 255, 100, 100, 60, 60, 10)
    pygame.time.delay(100)
    for event in pygame.event.get():



    # Start of QUIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x-=60
            elif event.key == pygame.K_d:
                x+=60
            elif event.key == pygame.K_w:
                y-=60
            elif event.key == pygame.K_s:
                y+=60
        elif event.type == pygame.QUIT:
            running = False
    # 1 frame
    pygame.display.update()
pygame.quit()
# End of QUIT