debug = True

# open and read the input file
input_file = open("day24/input.txt", "r")
input = input_file.read().split("\n")

# Grab the locations of all the blizzards from the input
blizzards = {"<": [], ">": [], "^": [], "v": []}
blizzards["<"] = [[] for i in range(len(input))]
blizzards[">"] = [[] for i in range(len(input))]
blizzards["^"] = [[] for i in range(len(input[0]))]
blizzards["v"] = [[] for i in range(len(input[0]))]
for y, line in enumerate(input):
    for x in [i for i, c in enumerate(line) if c == "<"]:
        blizzards["<"][y].append(x)
    for x in [i for i, c in enumerate(line) if c == ">"]:
        blizzards[">"][y].append(x)
    for x in [i for i, c in enumerate(line) if c == "^"]:
        blizzards["^"][x].append(y)
    for x in [i for i, c in enumerate(line) if c == "v"]:
        blizzards["v"][x].append(y)

# Starting and ending point
sx, sy = input[0].index("."), 0
ex, ey = input[-1].index("."), len(input)-1

move = lambda c, v: (c[0]+v[0], c[1]+v[1])

# Function to update blizzard locations
def move_blizzards():
    global blizzards

    for y in range(1, ey):
        blizzards["<"][y] = [n-1 if sx <= n-1 else ex for n in blizzards["<"][y]]
        blizzards[">"][y] = [n+1 if n+1 <= ex else sx for n in blizzards[">"][y]]

    for x in range(sx, ex+1):
        blizzards["^"][x] = [n-1 if sy <= n-1 else ey-1 for n in blizzards["^"][x]]
        blizzards["v"][x] = [n+1 if n+1 < ey else sy+1 for n in blizzards["v"][x]]

# Return true if the requested location is available to move into right now
def is_clear(x:int, y:int) -> bool:
    global blizzards

    if (x,y) == (sx,sy) or (x,y) == (ex,ey):
        return True
    if x < sx or x > ex or y <= sy or y >= ey:
        return False
    if x in blizzards["<"][y] or x in blizzards[">"][y]:
        return False
    if y in blizzards["^"][x] or x in blizzards["v"][x]:
        return False
    return True

#############
# MAIN LOOP #
#############

directions = {"S": (0,1), "E": (1,0), "N": (0,-1), "W": (-1,0), "X": (0,0)}
possible_locations = set()
possible_locations.add((sx, sy))
minute_number = 0
while True:
    minute_number += 1

    move_blizzards()

    next_possible_locations = set()
    for (x,y) in possible_locations:
        for d in "SENWX":
            (nx,ny) = move((x,y), directions[d])

            if (nx, ny) == (ex, ey):
                # WE REACHED THE EXIT
                print(f"Minute number: {minute_number}")
                exit(0)

            if is_clear(nx, ny):
                next_possible_locations.add((nx,ny))

    possible_locations = next_possible_locations