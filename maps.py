def Maps(a):
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
                [3, 2, props["Goal"]],
                [3, 3, props["Block"]],
                [4, 1, props["Block"]],
                [4, 2, props["Block"]],
                [4, 3, props["Block"]],

            ]
        ],  # props end
        2: [  # starting tile:
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
        3: [  # starting tile:
            [3, 3], [  # props:
                [0, 1, props["Wood_Box"]],
                [4, 1, props["Wood_Box"]],
                [0, 2, props["AI_Box"]],
                [3, 2, props["AI_Box"]],
                [2, 2, props["Player"]],

            ]
        ]
    }
    if a is None:
        return stages
    else:
        return stages[a]