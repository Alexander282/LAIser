# Start of Setup

import pygame
import time

pygame.init()
pygame.font.init()

tile_size = 60  # pixels
tile_amount = 10  # tiles
screen_width = tile_size * tile_amount
screen_height = tile_size * tile_amount
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
pos_x = 0
pos_y = 0

# End of Setup
pygame.display.set_caption("LAIser")
# picture = pygame.image.load("folder/name.png").conver_alpha
# screen.blit(picture, (x,y))


player_x = 0
player_y = 0
AI_x = 0
AI_y = 0
my_font = pygame.font.SysFont("Courier", 16)
button_font = pygame.font.SysFont('Courier', 30)
frame_count = 0
frame_rate = 0
t0 = time.process_time()

from stage_storage import stage_data, dialogue

stages = stage_data()

status = "menu"
# main menu buttons
menu_buttons = {
    # "name" : [xpos, ypos, color, width, height]
    "play": {"xpos": int(screen_width / 2 - 75),
             "ypos": int(screen_height / 2 - 50 - 200),
             "color": (155, 255, 97),
             "highlight": (187, 255, 148),
             "width": 150,
             "height": 100,
             "active": False,
             "status": "select"},
    "settings": {"xpos": int((screen_width / 2 - 75)),
                 "ypos": int(screen_height / 2 - 50),
                 "color": (97, 189, 255),
                 "highlight": (148, 210, 255),
                 "width": 150,
                 "height": 100,
                 "active": False,
                 "status": "settings"},
    "quit": {"xpos": int((screen_width / 2 - 75)),
             "ypos": int(screen_height / 2 - 50 + 200),
             "color": (255, 97, 97),
             "highlight": (255, 148, 148),
             "width": 150,
             "height": 100,
             "active": False,
             "status": "quit"}
}
# settings menu buttons
settings_buttons = {"<": {"xpos": 0,
                          "ypos": 0,
                          "color": (150, 150, 150),
                          "highlight": (200, 200, 200),
                          "width": 50,
                          "height": 50,
                          "active": False,
                          "status": "menu"}

                    }
# stage select menu buttons
select_buttons = {"<": {"xpos": 0,
                        "ypos": 0,
                        "color": (150, 150, 150),
                        "highlight": (200, 200, 200),
                        "width": 30,
                        "height": 30,
                        "active": False,
                        "status": "menu"},
                  }
button_count = 0
for key in stages.keys():
    select_buttons[key] = {"xpos": int((screen_width / 5 * (button_count % 5) + screen_width / 5 / 2 - 25)),
                           "ypos": int(screen_height / 5 * (button_count // 5) + screen_height / 5 / 2 - 25),
                           "color": (161, 161, 161),
                           "highlight": (204, 204, 204),
                           "width": 50,
                           "height": 50,
                           "active": False,
                           "status": key}
    button_count += 1
# active level buttons
level_number = 1
level_buttons = {"<": {"xpos": 0,
                       "ypos": 0,
                       "color": (150, 150, 150),
                       "highlight": (200, 200, 200),
                       "width": 30,
                       "height": 30,
                       "active": False,
                       "status": "select"},
                 "R": {"xpos": 30,
                       "ypos": 0,
                       "color": (150, 150, 150),
                       "highlight": (200, 200, 200),
                       "width": 30,
                       "height": 30,
                       "active": False,
                       "status": "reload"},
                 }

complete_buttons = {"<": {"xpos": int(screen_height/2)-100,
                       "ypos": int(screen_height/2)-50,
                       "color": (150, 150, 150),
                       "highlight": (200, 200, 200),
                       "width": 100,
                       "height": 100,
                       "active": False,
                       "status": "select"},
                 ">": {"xpos": int(screen_height/2),
                       "ypos": int(screen_height/2)-50,
                       "color": (100, 150, 100),
                       "highlight": (100, 200, 100),
                       "width": 100,
                       "height": 100,
                       "active": False,
                       "status": "next"},
                 }

def navigator(button_dict, mousex, mousey):
    active = []
    for button in button_dict:
        cur_but = button_dict[button]
        xrange = range(cur_but["xpos"], cur_but["xpos"] + cur_but["width"])
        yrange = range(cur_but["ypos"], cur_but["ypos"] + cur_but["height"])
        if mousex in xrange and mousey in yrange:
            pygame.draw.rect(screen, cur_but["highlight"],
                             (cur_but["xpos"], cur_but["ypos"], cur_but["width"], cur_but["height"]))

            cur_but["active"] = True
            active = cur_but["status"]
        else:
            pygame.draw.rect(screen, cur_but["color"],
                             (cur_but["xpos"], cur_but["ypos"], cur_but["width"], cur_but["height"]))
            cur_but["active"] = False
        text_surface = button_font.render(str(button), False, (0, 0, 0))
        screen.blit(text_surface, (
            cur_but["xpos"] + int(cur_but["width"] / 2) - int(button_font.size(str(button))[0] / 2),
            cur_but["ypos"] + int(cur_but["height"] / 2) - int(button_font.size(str(button))[1] / 2)))
    return active


def grid_draw(grid_amount, width1, color1, width2, color2):
    for grid in range(grid_amount + 1):
        pygame.draw.rect(screen, color1,
                         (grid * int(screen_width / grid_amount) - int(width1 / 2), 0, width1, screen_height))
        pygame.draw.rect(screen, color1,
                         (0, grid * int(screen_height / grid_amount) - int(width1 / 2), screen_height, width1))
    for grid in range(grid_amount + 1):
        pygame.draw.rect(screen, color2,
                         (grid * int(screen_width / grid_amount) - int(width2 / 2), 0, width2, screen_height))
        pygame.draw.rect(screen, color2,
                         (0, grid * int(screen_height / grid_amount) - int(width2 / 2), screen_height, width2))


while running:
    mousex, mousey = pygame.mouse.get_pos()
    fps = 60
    if status == "quit":
        break
    elif status == "menu":
        screen.fill((128, 128, 128))
        grid_draw(3, 40, (192, 192, 192), 20, (255, 255, 255))
        active_button = navigator(menu_buttons, mousex, mousey)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = active_button
            elif event.type == pygame.QUIT:
                status = "quit"

    elif status == "settings":
        screen.fill((148, 210, 255))
        active_button = navigator(settings_buttons, mousex, mousey)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = active_button
            elif event.type == pygame.QUIT:
                status = "quit"
    elif status == "select":
        screen.fill((187, 255, 148))
        grid_draw(5, 40, (203, 255, 173), 20, (219, 255, 199))

        active_button = navigator(select_buttons, mousex, mousey)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                stages = stage_data()
                if active_button == "menu":
                    status = "menu"
                else:
                    level_number = active_button
                    active_level = stages[active_button]
                    status = "level"
            elif event.type == pygame.QUIT:
                status = "quit"
    elif status == "reload":
        stages = stage_data()
        active_level = stages[level_number]
        status = "level"
    elif status == "level":

        # (where, (colour R,G,B), (xpos, ypos, xsize, ysize)
        screen.fill((128, 178, 128))

        # drawing the grid
        grid_draw(10, 6, (220, 220, 220), 3, (128, 255, 128))
        active_button = navigator(level_buttons, mousex, mousey)
        # movement & collision
        offsetx, offsety = active_level[0]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                status = active_button
            elif event.type == pygame.KEYDOWN:

                player_move = False
                AI_move = False
                player_collision = []
                AI_collision = []
                pushable_collision = []
                other_collision = []
                goal_position = []

                for object in active_level[1]:
                    if object[2].player:
                        player_collision.append([object[0], object[1]])
                    elif object[2].ai_controlled:
                        AI_collision.append([object[0], object[1]])
                    elif object[2].pushable:
                        pushable_collision.append([object[0], object[1]])
                    elif object[2].goal:
                        goal_position.append([object[0], object[1]])
                    else:
                        other_collision.append([object[0], object[1]])
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
                for object in active_level[1]:
                    if player_move and object[2].player:
                        if [object[0] + player_x, object[1] + player_y] in AI_collision or [object[0] + player_x,
                                                                                            object[
                                                                                                1] + player_y] in other_collision:
                            continue
                        elif [object[0] + player_x, object[1] + player_y] in goal_position:
                            status = "complete"
                        else:
                            if [object[0] + player_x, object[1] + player_y] in pushable_collision:
                                for object2 in active_level[1]:
                                    if object2[2].pushable and object2[0] == object[0] + player_x and object2[1] == \
                                            object[1] + player_y:
                                        if [object2[0] + player_x, object2[1] + player_y] in AI_collision or [
                                            object2[0] + player_x, object2[1] + player_y] in other_collision or [
                                            object2[0] + player_x, object2[1] + player_y] in pushable_collision or [
                                            object2[0] + player_x, object2[1] + player_y] in goal_position:
                                            continue
                                        else:
                                            object[0] += player_x
                                            object[1] += player_y
                                            object2[0] += player_x
                                            object2[1] += player_y
                            else:
                                object[0] += player_x
                                object[1] += player_y
                    elif AI_move and object[2].ai_controlled:
                        if [object[0] + AI_x, object[1] + AI_y] in player_collision or [object[0] + AI_x, object[
                                                                                                              1] + AI_y] in other_collision or [
                            object[0] + AI_x, object[1] + AI_y] in pushable_collision or [object[0] + AI_x, object[
                                                                                                                1] + AI_y] in AI_collision or [
                            object[0] + AI_x, object[1] + AI_y] in goal_position:
                            continue
                        else:
                            object[0] += AI_x
                            object[1] += AI_y
                player_x = 0
                player_y = 0
                AI_x = 0
                AI_y = 0
            elif event.type == pygame.QUIT:
                running = False

        # rendering everything

        for object in active_level[1]:
            # in-game, no object should ever reach the outside border.
            pos_x = object[0]
            pos_y = object[1]
            image = object[2].sprite
            name = object[2].type

            # render:
            image = pygame.transform.scale(image, (tile_size, tile_size))
            screen.blit(image, ((offsetx + pos_x) * tile_size, (offsety + pos_y) * tile_size))
            text_surface = my_font.render(dialogue(level_number), False, (0, 0, 0))
            screen.blit(text_surface, (0, screen_height - 50))
    elif status == "complete":
        screen.fill((104, 255, 77))
        grid_draw(6, 40, (124, 217, 108), 20, (133, 179, 125))
        active_button = navigator(complete_buttons, mousex, mousey)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_button == "next":
                    level_number += 1
                    status = "reload"
                else:
                    status = active_button
            elif event.type == pygame.QUIT:
                status = "quit"
    elif status == "quit":
        break
    frame_count += 1
    if frame_count % 500 == 0:
        t1 = time.process_time()
        frame_rate = 500 / (t1 - t0)
        t0 = t1
    the_text = my_font.render("{1:.2f} fps".format(frame_count, frame_rate), True, (50, 50, 50))

    screen.blit(the_text, (10, 584))
    pygame.display.update()
pygame.quit()
# End of QUIT
