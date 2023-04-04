# Start of Setup
import pygame
import attributes
pygame.init()
pygame.font.init()

screen_width = 600
screen_height = 600
screen =  pygame.display.set_mode((screen_width, screen_height))
running = True
# End of Setup
pygame.display.set_caption("LAIser")
#picture = pygame.image.load("folder/name.png").conver_alpha
#screen.blit(picture, (x,y))
props = {
    #"name":attributes.Attributes(deadly, pushable, ai_controlled, laser_redirect)
    "Wood_Box":attributes.Attributes(False, True, False, ""),
    "AI_Box":attributes.Attributes(False,False,True,""),
    "Block":attributes.Attributes(False,False,False,"")


}
x = 0
y = 0


status = "menu"

# statuses:
# menu = main menu

menu_buttons = {
    # "name" : [xpos, ypos, color, width, height]
    "play" : {"xpos": int(screen_width/2-75),
              "ypos": int(screen_height/2-50-200),
              "color": (155, 255, 97),
              "highlight": (187, 255, 148),
              "width": 150,
              "height":100,
              "active":False},
    "settings" : {"xpos": int((screen_width/2-75)),
              "ypos": int(screen_height/2-50),
              "color": (97, 189, 255),
              "highlight": (148, 210, 255),
              "width": 150,
              "height":100,
              "active":False},
    "quit" : {"xpos": int((screen_width/2-75)),
              "ypos": int(screen_height/2-50+200),
              "color": (255, 97, 97),
              "highlight": (255, 148, 148),
              "width": 150,
              "height":100,
              "active":False}
}
#
#   settings = settings menu
#   select = choose a stage
#       level = the active level
while running:
    mousex, mousey = pygame.mouse.get_pos()
    fps = 60
    if status == "menu":
        screen.fill((128, 128, 128))
        for button in menu_buttons:
            cur_but = menu_buttons[button]
            button_font = pygame.font.SysFont('swis721', 30)
            if mousex in range(cur_but["xpos"],cur_but["xpos"]+cur_but["width"]) and mousey in range(cur_but["ypos"],cur_but["ypos"]+cur_but["height"]):
                pygame.draw.rect(screen, cur_but["highlight"], (cur_but["xpos"], cur_but["ypos"], cur_but["width"], cur_but["height"]))


                cur_but["active"] = True
            else:
                pygame.draw.rect(screen,cur_but["color"],(cur_but["xpos"], cur_but["ypos"], cur_but["width"], cur_but["height"]))
                cur_but["active"] = False
            text_surface = button_font.render(str(button), False, (0, 0, 0))
            screen.blit(text_surface, (cur_but["xpos"]+int(cur_but["width"]/2)-int(button_font.size(str(button))[0]/2), cur_but["ypos"]+int(cur_but["height"]/2)-int(button_font.size(str(button))[1]/2)))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_buttons["play"]["active"]:
                    status = "level"
                elif menu_buttons["settings"]["active"]:
                    status = "settings"
                elif menu_buttons["quit"]["active"]:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
    elif status == "settings":
        screen.fill((128, 128, 128))
    elif status == "select":
        screen.fill((128, 128, 128))
    elif status == "level":
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
    #pygame.time.Clock.tick(60)
    pygame.display.update()
    pygame.time.wait(int(1000/fps))
pygame.quit()
# End of QUIT