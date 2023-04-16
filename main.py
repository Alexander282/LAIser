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
            [3, 1, props["Block"]],
            [3, 3, props["Block"]],
            [4, 1, props["Block"]],
            [4, 2, props["Block"]],
            [4, 3, props["Block"]],

        ]
    ],  # props end
    2: [  # starting tile:
        [0, 0], [  # props:
            [0, 0, props["AI_Box"]],
            [1, 0, props["AI_Box"]],
            [2, 0, props["AI_Box"]],
            [3, 0, props["AI_Box"]],
            [4, 0, props["AI_Box"]],
            [0, 1, props["AI_Box"]],
            [4, 1, props["AI_Box"]],
            [0, 2, props["AI_Box"]],
            [2, 2, props["Player"]],
            [4, 2, props["AI_Box"]],
            [0, 3, props["AI_Box"]],
            [4, 3, props["AI_Box"]],
            [0, 4, props["AI_Box"]],
            [1, 4, props["AI_Box"]],
            [2, 4, props["AI_Box"]],
            [3, 4, props["AI_Box"]],
            [4, 4, props["AI_Box"]],

        ]
    ],
    3: [  # starting tile:
        [3, 3], [  # props:
            [0, 1, props["Wood_Box"]],
            [4, 1, props["Wood_Box"]],
            [0, 2, props["AI_Box"]],
            [2, 2, props["Player"]],

        ]
    ]
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

select_buttons = {}
button_count = 0
for key in stages.keys():
    select_buttons[key] = {"xpos": int((screen_width / 5 * (button_count % 5 + 1) - 25)),
                           "ypos": int(screen_height / 5 * (button_count // 5 + 1) - 25),
                           "color": (161, 161, 161),
                           "highlight": (204, 204, 204),
                           "width": 50,
                           "height": 50,
                           "active": False}
    button_count += 1

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
                    status = "select"
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
        for button in select_buttons:
            cur_but = select_buttons[button]
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
                for level in select_buttons.keys():
                    if select_buttons[level]["active"]:
                        status = "level"
                        selection = level

    elif status == "level":
        active_level = stages[selection]
        # (where, (colour R,G,B), (xpos, ypos, xsize, ysize)
        screen.fill((128, 128, 128))

        # drawing the grid
        for xgrid in range(11):
            pygame.draw.rect(screen, (190, 190, 190), (xgrid * 60 - 3, 0, 6, 600))
        for ygrid in range(11):
            pygame.draw.rect(screen, (190, 190, 190), (0, ygrid * 60 - 3, 600, 6))
        pygame.time.delay(100)

        # movement & collision
        offsetx, offsety = active_level[0]
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                player_move = False
                AI_move = False
                player_collision = []
                AI_collision = []
                pushable_collision = []
                other_collision = []

                for object in stages[selection][1]:
                    if object[2].player:
                        player_collision.append([object[0], object[1]])
                    elif object[2].ai_controlled:
                        AI_collision.append([object[0], object[1]])
                    elif object[2].pushable:
                        pushable_collision.append([object[0], object[1]])
                    else:
                        other_collision.append([object[0], object[1]])
                print(pushable_collision, player_collision)
                player_x = 0
                player_y = 0
                AI_x = 0
                AI_y = 0
                if event.key == pygame.K_a:
                    player_x = -1
                    player_move = True
                elif event.key == pygame.K_d:
                    player_x = 1
                    player_move = True
                elif event.key == pygame.K_w:
                    player_y = -1
                    player_move = True
                elif event.key == pygame.K_s:
                    player_y = 1
                    player_move = True

                elif event.key == pygame.K_LEFT:
                    AI_x = -1
                    AI_move = True
                elif event.key == pygame.K_RIGHT:
                    AI_x = 1
                    AI_move = True
                elif event.key == pygame.K_UP:
                    AI_y = -1
                    AI_move = True
                elif event.key == pygame.K_DOWN:
                    AI_y = 1
                    AI_move = True
                # Collision
                for object in stages[selection][1]:
                    if player_move and object[2].player:
                        if [object[0] + player_x, object[1] + player_y] in AI_collision or [object[0] + player_x, object[1] + player_y] in other_collision:
                            player_x = 0
                            player_y = 0
                        else:
                            if [object[0] + player_x, object[1] + player_y] in pushable_collision:
                                for object2 in stages[selection][1]:
                                    if object2[2].pushable and object2[0] == object[0] + player_x and object2[1] == object[1] + player_y:
                                        if [object2[0] + player_x, object2[1] + player_y] in AI_collision or [object2[0] + player_x, object2[1] + player_y] in other_collision or [object2[0] + player_x, object2[1] + player_y] in pushable_collision:
                                            player_x = 0
                                            player_y = 0
                                        else:
                                            object[0] += player_x
                                            object[1] += player_y
                                            object2[0] += player_x
                                            object2[1] += player_y
                            else:
                                object[0] += player_x
                                object[1] += player_y
                    elif AI_move and object[2].ai_controlled:
                        if [object[0] + AI_x, object[1] + AI_y] in player_collision or [object[0] + AI_x, object[1] + AI_y] in other_collision or [object[0] + AI_x, object[1] + AI_y] in pushable_collision:
                            AI_x = 0
                            AI_y = 0
                        else:
                            object[0] += AI_x
                            object[1] += AI_y

            elif event.type == pygame.QUIT:
                running = False

        # rendering everything

        for object in active_level[1]:

            # in-game, no object should ever reach the outside border.
            '''if object[0] < 0-offsetx:
                object[0] = 0-offsetx
            elif object[0] > tile_amount-offsetx - 1:
                object[0] = tile_amount-offsetx - 1'''
            pos_x = object[0]
            '''if object[1] < 0-offsety:
                object[1] = 0-offsety
            elif object[1] > tile_amount-offsety - 1:
                object[1] = tile_amount-offsety - 1'''
            pos_y = object[1]
            name = object[2].type
            # move:

            # render:
            if name == "Player":
                pygame.draw.rect(screen, (255, 250, 50),
                                 ((offsetx + pos_x) * tile_size, (offsety + pos_y) * tile_size, 50, 50))
            elif name == "AI_Box":
                pygame.draw.rect(screen, (155, 250, 50),
                                 ((offsetx + pos_x) * tile_size, (offsety + pos_y) * tile_size, 50, 50))

            elif name == "Block":
                pygame.draw.rect(screen, (255, 50, 50),
                                 ((offsetx + pos_x) * tile_size, (offsety + pos_y) * tile_size, 50, 50))
            elif name == "Wood_Box":
                pygame.draw.rect(screen, (100, 150, 50),
                                 ((offsetx + pos_x) * tile_size, (offsety + pos_y) * tile_size, 50, 50))
    pygame.display.update()
pygame.quit()
# End of QUIT
