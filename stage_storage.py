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
def dialogue(stage_number):
    text = {1: "Player uses WASD to move",
            2: "Player can push wooden boxes",
            3: "AI uses arrow keys to move, AI cannot push player",
            4: "Ai cannot push boxes either (remember this)"}
    if stage_number in text.keys():
        return text[stage_number]
def stage_data():
    return{
        # stage number: [ [starting tile], [xpos, ypos, prop]]
        1: [  # starting tile:
            [3, 3], [  # props:
                [0, 0, props["Block"]],
                [0, 1, props["Block"]],
                [0, 2, props["Block"]],
                [0, 3, props["Block"]],
                [0, 4, props["Block"]],

                [1, 0, props["Block"]],
                [1, 1, props["Player"]],
                [1, 4, props["Block"]],

                [2, 0, props["Block"]],
                [2, 4, props["Block"]],


                [3, 0, props["Block"]],
                [3, 4, props["Block"]],

                [4, 0, props["Block"]],
                [4, 1, props["Block"]],
                [4, 2, props["Goal"]],
                [4, 3, props["Block"]],
                [4, 4, props["Block"]],

                [5, 0, props["Block"]],
                [5, 1, props["Block"]],
                [5, 2, props["Block"]],
                [5, 3, props["Block"]],
                [5, 4, props["Block"]],
            ]
        ],  # props end
        2: [  # starting tile:
            [3, 1], [  # props:
                [0, 0, props["Block"]],
                [0, 1, props["Block"]],
                [0, 2, props["Block"]],
                [0, 3, props["Block"]],
                [0, 4, props["Block"]],
                [0, 5, props["Block"]],
                [0, 6, props["Block"]],
                [0, 7, props["Block"]],


                [1, 0, props["Block"]],
                [1, 1, props["Player"]],
                [1, 3, props["Block"]],
                [1, 4, props["Block"]],
                [1, 5, props["Block"]],
                [1, 6, props["Block"]],
                [1, 7, props["Block"]],

                [2, 0, props["Block"]],
                [2, 3, props["Block"]],
                [2, 4, props["Block"]],
                [2, 5, props["Block"]],
                [2, 6, props["Block"]],
                [2, 7, props["Block"]],

                [3, 0, props["Block"]],
                [3, 2, props["Wood_Box"]],
                [3, 7, props["Block"]],

                [4, 0, props["Block"]],
                [4, 1, props["Block"]],
                [4, 2, props["Block"]],
                [4, 3, props["Block"]],
                [4, 4, props["Block"]],
                [4, 5, props["Goal"]],
                [4, 6, props["Block"]],
                [4, 7, props["Block"]],

                [5, 0, props["Block"]],
                [5, 1, props["Block"]],
                [5, 2, props["Block"]],
                [5, 3, props["Block"]],
                [5, 4, props["Block"]],
                [5, 5, props["Block"]],
                [5, 6, props["Block"]],
                [5, 7, props["Block"]],

            ]
        ],  # props end
        3: [  # starting tile:
            [1, 2], [  # props:
                [0, 0, props["Block"]],
                [0, 1, props["Block"]],
                [0, 2, props["Block"]],
                [0, 3, props["Block"]],

                [1, 0, props["Block"]],
                [1, 1, props["Block"]],
                [1, 2, props["Player"]],
                [1, 3, props["Block"]],

                [2, 0, props["Block"]],
                [2, 1, props["Block"]],
                [2, 3, props["Block"]],

                [3, 0, props["Block"]],
                [3, 2, props["AI_Box"]],
                [3, 3, props["Block"]],

                [4, 0, props["Block"]],
                [4, 3, props["Block"]],

                [5, 0, props["Block"]],
                [5, 3, props["Block"]],

                [6, 0, props["Block"]],
                [6, 1, props["Block"]],
                [6, 2, props["Goal"]],
                [6, 3, props["Block"]],

                [7, 0, props["Block"]],
                [7, 1, props["Block"]],
                [7, 2, props["Block"]],
                [7, 3, props["Block"]],

            ]
        ],  # props end
        4: [  # starting tile:
            [2, 2], [  # props:
                [0, 0, props["Block"]],
                [0, 1, props["Block"]],
                [0, 2, props["Block"]],
                [0, 3, props["Block"]],
                [0, 4, props["Block"]],

                [1, 0, props["Block"]],
                [1, 1, props["Block"]],
                [1, 2, props["Block"]],
                [1, 3, props["Player"]],
                [1, 4, props["Block"]],

                [2, 0, props["Block"]],
                [2, 4, props["Block"]],

                [3, 0, props["Block"]],
                [3, 1, props["AI_Box"]],
                [3, 2, props["AI_Box"]],
                [3, 3, props["AI_Box"]],
                [3, 4, props["Block"]],

                [4, 0, props["Block"]],
                [4, 4, props["Block"]],

                [5, 0, props["Block"]],
                [5, 1, props["Goal"]],
                [5, 2, props["Block"]],
                [5, 3, props["Block"]],
                [5, 4, props["Block"]],

                [6, 0, props["Block"]],
                [6, 1, props["Block"]],
                [6, 2, props["Block"]],
                [6, 3, props["Block"]],
                [6, 4, props["Block"]]

            ]
        ],
        5: [  # starting tile:
            [1, 0], [  # props:
                [0, 0, props["Block"]],
                [0, 1, props["Block"]],
                [0, 2, props["Block"]],
                [0, 3, props["Block"]],
                [0, 4, props["Block"]],
                [0, 5, props["Block"]],
                [0, 6, props["Block"]],
                [0, 7, props["Block"]],
                [0, 8, props["Block"]],
                [0, 9, props["Block"]],

                [1, 0, props["Block"]],
                [1, 1, props["Block"]],
                [1, 2, props["Block"]],
                [1, 3, props["Block"]],
                [1, 4, props["Goal"]],
                [1, 5, props["Block"]],
                [1, 6, props["Block"]],
                [1, 7, props["Block"]],
                [1, 8, props["Block"]],
                [1, 9, props["Block"]],

                [2, 0, props["Block"]],
                [2, 1, props["AI_Box"]],
                [2, 9, props["Block"]],

                [3, 0, props["Block"]],
                [3, 1, props["Block"]],
                [3, 2, props["Block"]],
                [3, 3, props["Block"]],
                [3, 4, props["AI_Box"]],
                [3, 5, props["Block"]],
                [3, 6, props["Block"]],
                [3, 7, props["Block"]],
                [3, 9, props["Block"]],

                [4, 0, props["Block"]],
                [4, 1, props["Block"]],
                [4, 2, props["Block"]],
                [4, 3, props["Wood_Box"]],
                [4, 4, props["AI_Box"]],
                [4, 5, props["AI_Box"]],
                [4, 9, props["Block"]],

                [5, 0, props["Block"]],
                [5, 1, props["Block"]],
                [5, 2, props["Block"]],
                [5, 4, props["Wood_Box"]],
                [5, 6, props["Block"]],
                [5, 7, props["Block"]],
                [5, 8, props["Block"]],
                [5, 9, props["Block"]],

                [6, 0, props["Block"]],
                [6, 1, props["Block"]],
                [6, 2, props["Block"]],
                [6, 3, props["Block"]],
                [6, 7, props["Block"]],
                [6, 8, props["Block"]],
                [6, 9, props["Block"]],

                [7, 0, props["Block"]],
                [7, 1, props["Block"]],
                [7, 2, props["Block"]],
                [7, 3, props["Block"]],
                [7, 4, props["Player"]],
                [7, 5, props["Block"]],
                [7, 6, props["Block"]],
                [7, 7, props["Block"]],
                [7, 8, props["Block"]],
                [7, 9, props["Block"]],

                [8, 0, props["Block"]],
                [8, 1, props["Block"]],
                [8, 2, props["Block"]],
                [8, 3, props["Block"]],
                [8, 4, props["Block"]],
                [8, 5, props["Block"]],
                [8, 6, props["Block"]],
                [8, 7, props["Block"]],
                [8, 8, props["Block"]],
                [8, 9, props["Block"]],

            ]
        ]
    }