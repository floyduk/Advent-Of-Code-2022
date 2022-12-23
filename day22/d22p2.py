# open and read the input file
input_file = open("day22/input.txt", "r")
input = input_file.read().split("\n")

# Find the blank line and from that get the map and the movedata
blank = input.index("")
map = input[0:blank]
movedata = []
debug = False

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

# Sample sides are 4x4
# field_length = 4
# wrap_mappings = {
#     "A":[{"direction":"vu", "turn":"L", "start":(13,8)},    {"direction":"hr", "turn":"R", "start":(13,8)}],
#     "B":[{"direction":"hl", "turn":"R", "start":(8,9)},     {"direction":"vd", "turn":"L", "start":(8,9)}],
#     "C":[{"direction":"vu", "turn":"R", "start":(8,4)},     {"direction":"hl", "turn":"L", "start":(8,4)}],
#     "D":[{"direction":"hr", "turn":"B", "start":(9,0)},     {"direction":"hl", "turn":"B", "start":(4,4)}],
#     "E":[{"direction":"vu", "turn":"L", "start":(0,8)},     {"direction":"hr", "turn":"R", "start":(13,13)}],
#     "F":[{"direction":"vd", "turn":"B", "start":(17,9)},    {"direction":"vu", "turn":"B", "start":(13,4)}],
#     "G":[{"direction":"hl", "turn":"B", "start":(4,9)},     {"direction":"hr", "turn":"B", "start":(9,13)}],
# }

# Sides of the cube are 50x50 so all we need are starting points in each direction
field_length = 50
wrap_mappings = {
    "A":[{"direction":"hr", "turn":"L", "start":(101,51)},    {"direction":"vd", "turn":"R", "start":(101,51)}],
    "B":[{"direction":"vu", "turn":"R", "start":(50,100)},     {"direction":"hl", "turn":"L", "start":(50,100)}],
    "C":[{"direction":"hr", "turn":"L", "start":(51,151)},     {"direction":"vd", "turn":"R", "start":(51,151)}],
    "D":[{"direction":"hr", "turn":"N", "start":(101,0)},     {"direction":"hr", "turn":"N", "start":(1,201)}],
    "E":[{"direction":"vu", "turn":"B", "start":(50,50)},     {"direction":"vd", "turn":"B", "start":(0,101)}],
    "F":[{"direction":"vd", "turn":"R", "start":(0,151)},    {"direction":"hr", "turn":"L", "start":(51,0)}],
    "G":[{"direction":"vu", "turn":"B", "start":(151,50)},     {"direction":"vd", "turn":"B", "start":(101,101)}],
}

def is_off_the_board(nx, ny):
    if map[ny][nx] == " ":
        return True
    else:
        return False

def wrap(x, y, d):
    def position_in_field(x,y,d,wrap_field):
        if wrap_field["direction"] == "hr" and d in [1,3]:
            if y == wrap_field["start"][1] and wrap_field["start"][0] <= x < wrap_field["start"][0] + field_length:
                return x - wrap_field["start"][0]

        if wrap_field["direction"] == "hl" and d in [1,3]:
            if y == wrap_field["start"][1] and wrap_field["start"][0] - field_length < x <= wrap_field["start"][0]:
                return wrap_field["start"][0] - x

        if wrap_field["direction"] == "vd" and d in [0,2]:
            if x == wrap_field["start"][0] and wrap_field["start"][1] <= y < wrap_field["start"][1] + field_length:
                return y - wrap_field["start"][1]

        if wrap_field["direction"] == "vu" and d in [0,2]:
            if x == wrap_field["start"][0] and wrap_field["start"][1] - field_length < y <= wrap_field["start"][1]:
                return wrap_field["start"][1] - y

        return -1

    def mapped_position_in_field(d, wrap_field, position):
        nx, ny, nd = wrap_field["start"][0], wrap_field["start"][1], d

        if wrap_field["direction"] == "hr":
            nx = wrap_field["start"][0] + position
        elif wrap_field["direction"] == "hl":
            nx = wrap_field["start"][0] - position
        elif wrap_field["direction"] == "vd":
            ny = wrap_field["start"][1] + position
        elif wrap_field["direction"] == "vu":
            ny = wrap_field["start"][1] - position

        if wrap_field["turn"] == "L":
            nd = (d-1) % 4
        elif wrap_field["turn"] == "R":
            nd = (d+1) % 4
        elif wrap_field["turn"] == "B":
            nd = (d+2) % 4
        
        nx, ny = move((nx,ny), direction[nd])

        return nx, ny, nd

    # Search through the wrap mappings to find which one we're in
    for key in wrap_mappings.keys():
        position = position_in_field(x, y, d, wrap_mappings[key][0])
        if position != -1:
            return mapped_position_in_field(d, wrap_mappings[key][1], position)

        position = position_in_field(x, y, d, wrap_mappings[key][1])
        if position != -1:
            return mapped_position_in_field(d, wrap_mappings[key][0], position)

    print("NO WRAP FIELD FOUND - CRISIS!")
    exit(1)

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

            nd = d
            nx, ny = move((x,y), direction[d])

            if is_off_the_board(nx, ny):
                nx, ny, nd = wrap(nx,ny,d)

            if map[ny][nx] == "#":
                # There's a block in the way. Stop moving here.
                break
            else:
                # Looks safe to move ahead so do it.
                x, y, d = nx, ny, nd

    else:
        # If it's an L or R then change direction
        d = (d+1) % 4 if m == "R" else (d-1) % 4

# Print the map
if debug:
    for line in map:
        print(line)

# Print the answer
print((y * 1000)+(x * 4)+d)