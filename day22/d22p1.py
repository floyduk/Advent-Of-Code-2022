# open and read the input file
input_file = open("day22/input.txt", "r")
input = input_file.read().split("\n")

# Find the blank line and from that get the map and the movedata
blank = input.index("")
map = input[0:blank]
movedata = []
debug = True

# Fill every line of the map to the same length and add spaces all around the edge
# This makes detecting where to wrap to MUCH simpler
max_map_line_length = max([len(line) for line in map])
for i,line in enumerate(map):
    if len(line) < max_map_line_length:
        map[i] = " " + map[i] + (" " * (max_map_line_length-len(line))) + " "
    else:
        map[i] = " " + map[i] + " "
map.insert(0, " " * (max_map_line_length+2))
map.append(" " * (max_map_line_length+2))

# Get start location
x, y, d = map[1].index("."), 1, 0

# Turn movedata into a list
s=""
for c in input[blank+1]:
    if c in "LR":
        movedata.append(int(s))
        s = ""
        movedata.append(c)
    else:
        s += c
if s != "":
    movedata.append(int(s))

move = lambda c, v: (c[0]+v[0], c[1]+v[1])
direction = [(1,0), (0,1), (-1,0), (0,-1)]
direction_char = ">v<^"

def is_off_the_board(nx, ny):
    if map[ny][nx] == " ":
        return True
    else:
        return False

def wrap(x, y, d):
    search_direction = (d+2) % 4

    sx, sy = x, y
    while True:
        sx, sy = move((sx,sy), direction[search_direction])

        # If we find a space then stop, go back 1 step and return
        if map[sy][sx] == " ":
            sx, sy = move((sx,sy), direction[d])
            return (sx,sy)

if debug:
    print(wrap(6,8,1))
    print(wrap(12,7,0))
    print(wrap(6,5,3))
    print(wrap(1,7,2))

#############
# MAIN LOOP #
#############

# Iterate the movedata making the moves by altering x, y, and d
for m in movedata:
    if type(m) == int:
        # If it's an integer then move forward
        for i in range(m):
            # Put a char in the map for debugging
            if debug:
                map[y] = ''.join([direction_char[d] if i == x else c for i,c in enumerate(list(map[y]))])

            nx, ny = move((x,y), direction[d])

            if is_off_the_board(nx, ny):
                nx,ny = wrap(x,y,d)

            if map[ny][nx] == "#":
                # There's a block in the way. Stop moving here.
                break
            else:
                # Looks safe to move ahead so do it.
                x, y = nx, ny

    else:
        # If it's an L or R then change direction
        d = (d+1) % 4 if m == "R" else (d-1) % 4

# Print the map
if debug:
    for line in map:
        print(line)

# Print the answer
print((y * 1000)+(x * 4)+d)