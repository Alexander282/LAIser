import attributes
import pygame
import attributes
props = {
    # "name":attributes.Attributes(name, deadly, pushable, player, ai_controlled, laser_redirect)
    "Wood_Box": attributes.Attributes("Wood_Box", True, False, True, False, False, "", False, pygame.image.load("sprites\\Wood_Box.png").convert_alpha()),
    "AI_Box": attributes.Attributes("AI_Box", True, False, False, False, True, "", False, pygame.image.load("sprites\\AI_Box.png").convert_alpha()),
    "Block": attributes.Attributes("Block", True, False, False, False, False, "", False, pygame.image.load("sprites\\Block.png").convert_alpha()),
    "Player": attributes.Attributes("Player", True, False, False, True, False, "", False, pygame.image.load("sprites\\Player.png").convert_alpha()),
    "Goal": attributes.Attributes("Player", True, False, False, False, False, "", True, pygame.image.load("sprites\\Goal.png").convert_alpha()),
}

def stage_data():
    return{
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
                [3, 2, props["Goal"]],
                [3, 3, props["Block"]],
                [4, 1, props["Block"]],
                [4, 2, props["Block"]],
                    [4, 3, props["Block"]]
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
                    [6, 6, props["Goal"]]
                ]
            ],
            3: [  # starting tile:
                [3, 3], [  # props:
                    [0, 1, props["Wood_Box"]],
                    [4, 1, props["Wood_Box"]],
                    [0, 2, props["AI_Box"]],
                    [3, 2, props["AI_Box"]],
                    [2, 2, props["Player"]]
                ]
            ]
        }