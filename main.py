# Start of Setup
import pygame
import attributes
pygame.init()
screen_width = 600
screen_height = 600
screen =  pygame.display.set_mode((screen_width, screen_height))
running = True
# End of Setup
pygame.display.set_caption("LAIser")
#picture = pygame.image.load("folder/name.png").conver_alpha
#screen.blit(picture, (x,y))
props = {"Wood_Box":attributes.Attributes(False, True, False, ""),
         "AI_Box":attributes.Attributes(False,False,True,"")



}
x = 0
y = 0




while running:
    #               (where, (colour R,G,B), (xpos, ypos, xsize, ysize)
    screen.fill((128,128,128))

    for xgrid in range(11):
        pygame.draw.rect(screen, (190,190,190), (xgrid*60-3, 0, 6, 600))
    for ygrid in range(11):
        pygame.draw.rect(screen, (190, 190, 190), (0, ygrid * 60-3, 600, 6))
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
    if x > screen_height-60:
        x -= 60
    #elif x < 0:
    # 1 frame
    pygame.draw.rect(screen, (255,50,50), (x+5, y+5, 50, 50))
    pygame.display.update()

pygame.quit()
# End of QUIT