# open and read the input file
input_file = open("day14/input.txt", "r")
lines = input_file.read().split("\n")

# We keep a set of all blocked nodes. Doesn't matter if it's sand or rock or floor.
# Nodes are (x, y) tuples
blocked_nodes = set()

# A count of how many sand blocks came to rest
sand_count = 0          

# Iterate the input file creating a set of blocked nodes where there is rock
for line in lines:
    # Turn this line into a list of nodes - [x, y] value pairs
    nodes = [[int(xy) for xy in n.split(",")] for n in line.split(" -> ")]

    # Turn the nodes into lines
    for i in range(len(nodes)-1):
        if nodes[i][0] != nodes[i+1][0]:
            for x in range(nodes[i][0], nodes[i+1][0] + (1 if nodes[i][0]<nodes[i+1][0] else -1), 1 if nodes[i][0]<nodes[i+1][0] else -1):
                blocked_nodes.add((x, nodes[i][1]))
        else:
            for y in range(nodes[i][1], nodes[i+1][1] + (1 if nodes[i][1]<nodes[i+1][1] else -1), 1 if nodes[i][1]<nodes[i+1][1] else -1):
                blocked_nodes.add((nodes[i][0], y))

# Get the lowest point in our rock system and add 2 to calculate the level of the floor.
floor = sorted([n[1] for n in blocked_nodes])[-1]+2
print("Floor is at: " + str(floor))

# Simulate sand falling until one comes to rest at 500,0
while True:
    # Create a sand block at 500,0
    sand = (500, 0)

    # Move the new sand block until it comes to rest
    while True:
        # Can sand move down?
        if (sand[0], sand[1]+1) in blocked_nodes:
            # Can sand move down and left?
            if (sand[0]-1, sand[1]+1) in blocked_nodes:
                # Can sand move down and right?
                if (sand[0]+1, sand[1]+1) in blocked_nodes:
                    # Sand cannot move and comes to rest - add it to the sand_nodes set
                    sand_count += 1
                    blocked_nodes.add(sand)
                    break
                else:
                    # Sand can move down and right. Move it.
                    sand = (sand[0]+1, sand[1]+1)
            else:
                # Sand can move down and left. Move it.
                sand = (sand[0]-1, sand[1]+1)
        else:
            # Sand can move down. Move it.
            sand = (sand[0], sand[1]+1)

        # If we're getting near the floor then add floor nodes in this area
        if(sand[1] >= floor - 1):
            blocked_nodes.add((sand[0]-1, floor))
            blocked_nodes.add((sand[0], floor))
            blocked_nodes.add((sand[0]+1, floor))
        
    # Did the last block of sand come to rest in the sand source location?
    if sand == (500, 0):
        # All sand has fallen. Stop the simulation
        break

# Print the number of nodes in sand_nodes
print(sand_count)