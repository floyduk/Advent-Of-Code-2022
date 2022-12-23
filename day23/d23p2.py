debug = False

# open and read the input file
input_file = open("day23/input.txt", "r")
input = input_file.read().split("\n")

# Moving and checking stuff
move = lambda c, v: (c[0]+v[0], c[1]+v[1])
clear_in_direction = lambda x, y, d: (move((x,y), direction[d]) not in elves)
direction = {
    "N": (0,-1), "S": (0,1), "E": (1,0), "W": (-1,0),
    "NW": (-1,-1), "NE": (1,-1), "SW": (-1,1), "SE": (1,1)
}

# Direction stuff
propose_direction = 0
propose_directions = "NSWE"

# Build a list of elf positions
elves = []
for y in range(len(input)):
    positions = [i for i in range(len(input[y])) if input[y][i] == "#"]
    for x in positions:
        elves.append((x, y))

print(f"Total elves: {len(elves)}")

#############
# MAIN LOOP #
#############

round_number = 0
while True:
    round_number += 1

    # Loop through the elves proposing a new position for each and building the new positions into elves_new_loc[]
    elves_new_loc = []
    count_didnt_move = 0
    for e in elves:
        # Is the elf surrounded by empty space? If so then do nothing
        if clear_in_direction(e[0], e[1], "N") and clear_in_direction(e[0], e[1], "S") and \
            clear_in_direction(e[0], e[1], "E") and clear_in_direction(e[0], e[1], "W") and \
            clear_in_direction(e[0], e[1], "NW") and clear_in_direction(e[0], e[1], "NE") and \
            clear_in_direction(e[0], e[1], "SW") and clear_in_direction(e[0], e[1], "SE"):
            elves_new_loc.append(e)
            count_didnt_move += 1
            continue

        move_proposed = False
        for i in range(4):
            d = propose_directions[(propose_direction+i) % 4]
            if d == "N" and clear_in_direction(e[0], e[1], "N") and clear_in_direction(e[0], e[1], "NE") and clear_in_direction(e[0], e[1], "NW"):
                elves_new_loc.append(move((e[0], e[1]), direction["N"]))
                move_proposed = True
                break
            elif d == "S" and clear_in_direction(e[0], e[1], "S") and clear_in_direction(e[0], e[1], "SE") and clear_in_direction(e[0], e[1], "SW"):
                elves_new_loc.append(move((e[0], e[1]), direction["S"]))
                move_proposed = True
                break
            elif d == "W" and clear_in_direction(e[0], e[1], "W") and clear_in_direction(e[0], e[1], "NW") and clear_in_direction(e[0], e[1], "SW"):
                elves_new_loc.append(move((e[0], e[1]), direction["W"]))
                move_proposed = True
                break
            elif d == "E" and clear_in_direction(e[0], e[1], "E") and clear_in_direction(e[0], e[1], "NE") and clear_in_direction(e[0], e[1], "SE"):
                elves_new_loc.append(move((e[0], e[1]), direction["E"]))
                move_proposed = True
                break

        # If elf can't move then new loc is the same as old loc
        if move_proposed == False:
            elves_new_loc.append(e)
    
    if count_didnt_move == len(elves):
        break
    else:
        if debug:
            print(round_number, ":", count_didnt_move, " ", end="")

    # Update propose direction
    propose_direction = (propose_direction+1) % 4

    # Now loop through the elves looking for clashes and setting any we find to not move
    for j in range(len(elves)):
        if len([e for e in elves_new_loc if e == elves_new_loc[j]]) > 1:
            elves_new_loc = [e if e != elves_new_loc[j] else elves[i] for i, e in enumerate(elves_new_loc)]

    # Move the elves to their new locations
    elves = elves_new_loc

print("\n", round_number)