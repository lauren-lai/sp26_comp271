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
    "SSSSSSSS "
]

P = [
    "PPPPPPPP ",
    "P      P ",
    "PPPPPPPP ",
    "P        ",
    "P        ",
    "P        "
]

def compose_horizontal(letters):
    # assumes that each letter has the same height
    height = len(letters[0])

    for line in range(height):
        for letter in letters:
            print(letter[line], end ="")
        print()

RIVER_NAME = [M, I , S, S, I, S, S, I, P, P, I]
compose_horizontal(RIVER_NAME)