M = [
    "M       M",
    "M M    MM",
    "M  M  M M",
    "M   M   M",
    "M       M",
    "M       M"
]

I = [
    "    I    ",
    "    I    ",
    "    I    ",
    "    I    ",
    "    I    ",
    "    I    "
]

S = [
    "  SSSSSSS",
    "SS       ",
    " SSSSSSS ",
    "       SS",
    "       SS",
    "SSSSSSSS"
]

P = [
    "PPPPPPPP ",
    "PP     PP",
    "PPPPPPPP ",
    "PP       ",
    "PP       ",
    "PP       "
]

def compose_horizontal(letters):
    # assume that each letter has the same height
    height = len(letters[0])
    for line in range(height):
        for letter in letters:
            print(letter[line], end ="")
    # break a line
    print()

RIVER_NAME = [M, I , S, S, I, S, S, P, P, I]

def compose_horizontal(RIVER_NAME)