# Just to make our code read a little nicer let's make a Coordinate type with x and y member values
class Coordinate:
    x: int
    y: int
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

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

# Head and tail start at 0,0
head = Coordinate(0,0)
tail = Coordinate(0,0)

# Iterate the list of commands
for command in commands:
    direction, count = command.split()

    for i in range(int(count)):
        # Move the head
        if direction == "U":
            head.y += 1
        elif direction == "D":
            head.y -= 1
        elif direction == "L":
            head.x -= 1
        elif direction == "R":
            head.x += 1

        # Calculate the x and y distances between head and tail. 
        # We use these to determine whether to move the tail and if so then how to move it
        x_distance = head.x - tail.x
        y_distance = head.y - tail.y

        # Only certain moves are possible. If we have a 0 and a 2 or a 1 and a 2 in our 
        # x and y distances then we apply the tail movement. Otherwise no tail movement.
        if sorted([abs(x_distance), abs(y_distance)]) in [[0,2], [1,2]]:
            tail.x += halve_and_round_up(x_distance)
            tail.y += halve_and_round_up(y_distance)

        # Add this tail location to the tail_locations set
        tail_locations.add((tail.x, tail.y))
            
# Print the answer
print("Tail visited: " + str(len(tail_locations)) + " locations")