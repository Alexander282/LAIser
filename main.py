# Start of Setup
import pygame
import attributes

pygame.init()
pygame.font.init()

tile_size = 60  # pixels
tile_amount = 10  # tiles
screen_width = tile_size * tile_amount
screen_height = tile_size * tile_amount
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
# End of Setup
pygame.display.set_caption("LAIser")
# picture = pygame.image.load("folder/name.png").conver_alpha
# screen.blit(picture, (x,y))
props = {
    # "name":attributes.Attributes(name, deadly, pushable, player, ai_controlled, laser_redirect)
    "Wood_Box": attributes.Attributes("Wood_Box", False, True, False, False, "", False),
    "AI_Box": attributes.Attributes("AI_Box", False, False, False, True, "", False),
    "Block": attributes.Attributes("Block", False, False, False, False, "", False),
    "Player": attributes.Attributes("Player", False, False, True, False, "", False),
    "Goal": attributes.Attributes("Player", False, False, False, False, "", True),
}

player_x = 0
player_y = 0
AI_x = 0
AI_y = 0

stages = {
    # stage number: [ [starting tile], [xpos, ypos, prop]]
    1: [  # starting tile:
        [2, 2], [  # props:
            [0, 1, props["Block"]],
            [0, 2, props["Block"]],
            [0, 3, props["Block"]],
            [1, 0, props["Block"]],
            [1, 1, props["Block"]],
            [1, 2, props["Player"]],
            [1, 3, props["Block"]],
            [2, 0, props["Block"]],
            [2, 2, props["AI_Box"]],
            [2, 3, props["Block"]],
            [3, 0, props["Block"]],
            [3, 1, props["Block"]],
            [3, 1, props["Goal"]],
            [3, 3, props["Block"]],
            [4, 1, props["Block"]],
            [4, 2, props["Block"]],
            [4, 3, props["Block"]],


        ]
    ]  # props end

}

print(stages[1][1][1][2].type)
status = "menu"

# statuses:
# menu = main menu

menu_buttons = {
    # "name" : [xpos, ypos, color, width, height]
    "play": {"xpos": int(screen_width / 2 - 75),
             "ypos": int(screen_height / 2 - 50 - 200),
             "color": (155, 255, 97),
             "highlight": (187, 255, 148),
             "width": 150,
             "height": 100,
             "active": False},
    "settings": {"xpos": int((screen_width / 2 - 75)),
                 "ypos": int(screen_height / 2 - 50),
                 "color": (97, 189, 255),
                 "highlight": (148, 210, 255),
                 "width": 150,
                 "height": 100,
                 "active": False},
    "quit": {"xpos": int((screen_width / 2 - 75)),
             "ypos": int(screen_height / 2 - 50 + 200),
             "color": (255, 97, 97),
             "highlight": (255, 148, 148),
             "width": 150,
             "height": 100,
             "active": False}
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
            if mousex in range(cur_but["xpos"], cur_but["xpos"] + cur_but["width"]) and mousey in range(cur_but["ypos"],
                                                                                                        cur_but[
                                                                                                            "ypos"] +
                                                                                                        cur_but[
                                                                                                            "height"]):
                pygame.draw.rect(screen, cur_but["highlight"],
                                 (cur_but["xpos"], cur_but["ypos"], cur_but["width"], cur_but["height"]))

                cur_but["active"] = True
            else:
                pygame.draw.rect(screen, cur_but["color"],
                                 (cur_but["xpos"], cur_but["ypos"], cur_but["width"], cur_but["height"]))
                cur_but["active"] = False
            text_surface = button_font.render(str(button), False, (0, 0, 0))
            screen.blit(text_surface, (
                cur_but["xpos"] + int(cur_but["width"] / 2) - int(button_font.size(str(button))[0] / 2),
                cur_but["ypos"] + int(cur_but["height"] / 2) - int(button_font.size(str(button))[1] / 2)))
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
        selection = 1
        # (where, (colour R,G,B), (xpos, ypos, xsize, ysize)
        screen.fill((128, 128, 128))

        for xgrid in range(11):
            pygame.draw.rect(screen, (190, 190, 190), (xgrid * 60 - 3, 0, 6, 600))
        for ygrid in range(11):
            pygame.draw.rect(screen, (190, 190, 190), (0, ygrid * 60 - 3, 600, 6))
        pygame.time.delay(100)
        for event in pygame.event.get():

            # Start of QUIT
            if event.type == pygame.KEYDOWN:
                save = [player_x, player_y, AI_x, AI_y]
                collision = []
                for object in stages[selection][1]:
                    if object[2].type == "Player":
                        collision.append([object[0] + player_x, object[1] + player_y])
                    elif object[2].type == "AI_Box":
                        collision.append([object[0] + AI_x, object[1] + AI_y])
                    else:
                        collision.append([object[0], object[1]])
                if event.key == pygame.K_a:
                    player_x -= 1
                elif event.key == pygame.K_d:
                    player_x += 1
                elif event.key == pygame.K_w:
                    player_y -= 1
                elif event.key == pygame.K_s:
                    player_y += 1

                elif event.key == pygame.K_LEFT:
                    AI_x -=1
                elif event.key == pygame.K_RIGHT:
                    AI_x +=1
                elif event.key == pygame.K_UP:
                    AI_y -=1
                elif event.key == pygame.K_DOWN:
                    AI_y +=1

                for object in stages[selection][1]:
                    if object[2].type == "Player" and [object[0] + player_x, object[1] + player_y] in collision:
                        print(save)
                        player_x = save[0]
                        player_y = save[1]
                        print("collision")
                    if object[2].type == "AI_Box" and [object[0] + AI_x, object[1] + AI_y] in collision:
                        print(save)
                        AI_x = save[2]
                        AI_y = save[3]
                        print("collision")
            elif event.type == pygame.QUIT:
                running = False
        # elif x < 0:
        # 1 frame
        offsetx, offsety = stages[selection][0]
        for object in stages[selection][1]:
            pos_x = object[0]
            pos_y = object[1]
            name = object[2].type
            if name == "Player":
                pygame.draw.rect(screen, (255, 250, 50),
                                 ((offsetx + pos_x + player_x) * tile_size, (offsety + pos_y + player_y) * tile_size, 50, 50))
            elif name == "AI_Box":
                pygame.draw.rect(screen, (155, 250, 50),
                                 ((offsetx + pos_x + AI_x) * tile_size, (offsety + pos_y + AI_y) * tile_size, 50, 50))

            elif name == "Block":
                pygame.draw.rect(screen, (255, 50, 50),
                                 ((offsetx + pos_x) * tile_size, (offsety + pos_y) * tile_size, 50, 50))
    # pygame.time.Clock.tick(60)
    pygame.display.update()
    pygame.time.wait(int(1000 / fps))
pygame.quit()
# End of QUIT
