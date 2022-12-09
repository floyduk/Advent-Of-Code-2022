# We use this to move the tail. If there is a gap of 2 then we move the tail 1. We use this in 
# both x and y dimensions and only when there is sufficient gap. 
# We'll only ever deal with -2, -1, 0, 1 and 2 so I can do this with ternary operators or 
# with (n // abs(n)) with a special case for 0. 
# I suspect ternary operators are faster because no division. 
# Integer division is slower than floating point!
#halve_and_round_up = lambda n : 0 if n == 0 else (n // abs(n))
halve_and_round_up = lambda n : 0 if n == 0 else (1 if n > 0 else -1)

# open and read the input file
input_file = open("day9/input.txt", "r")
commands = input_file.read().split("\n")

# This will contain all the locations that the tail visits. It is a set so there can be no duplicates.
tail_locations = set()
num_knots = 10

# Head and tail start at 0,0. Unlike part 1 we're using lists to store x and y values. We need a mutable
# and ordered type. So lists are it. x is [0] and y is [1]
knots = []
for i in range(num_knots):
    knots.append([0,0])

# Function to print the grid
def print_grid():
    for y in range(15, -6, -1):
        for x in range(-11, 15):
            if([x,y] in knots):
                print(str(knots.index([x,y])), end="")
            else:
                print(".", end="")
        print("")
    print("")

# Iterate the list of commands
for command in commands:
    direction, count = command.split()

    # Iterate the count - ie do the move count times
    for i in range(int(count)):
        # Move the head. Remember .x is [0] and .y is [1]
        if direction == "U":
            knots[0][1] += 1
        elif direction == "D":
            knots[0][1] -= 1
        elif direction == "L":
            knots[0][0] -= 1
        elif direction == "R":
            knots[0][0] += 1

        # Iterate the knots - make the moves for each knot in turn starting from knots[1]
        for j in range(1, num_knots):
            # Calculate the x and y distances between head and tail. 
            # We use these to determine whether to move the tail and if so then how to move it
            x_distance = knots[j-1][0] - knots[j][0]
            y_distance = knots[j-1][1] - knots[j][1]

            # As for part 1 except that now a [2,2] movement is possible as well
            if sorted([abs(x_distance), abs(y_distance)]) in [[0,2], [1,2], [2,2]]:
                knots[j][0] += halve_and_round_up(x_distance)
                knots[j][1] += halve_and_round_up(y_distance)

        # Add this tail location to the tail_locations set
        tail_locations.add((knots[num_knots-1][0], knots[num_knots-1][1]))

    # Display the grid
    #print_grid()
            
# Print the answer
print("Tail visited: " + str(len(tail_locations)) + " locations")