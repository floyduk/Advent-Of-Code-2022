# open and read the input file
input_file = open("day14/input.txt", "r")
lines = input_file.read().split("\n")

# We keep a set of all blocked nodes. Doesn't matter if they're rock or sand.
# Nodes are (x, y) tuples
blocked_nodes = set()

# A count of how many sand blocks came to rest
sand_count = 0          

# Iterate the input file creating a set of blocked nodes where there is rock
for line in lines:
    # Turn this line into a list of nodes
    nodes = [[int(xy) for xy in n.split(",")] for n in line.split(" -> ")]

    # Turn the nodes into lines
    for i in range(len(nodes)-1):
        if nodes[i][0] != nodes[i+1][0]:
            for x in range(nodes[i][0], nodes[i+1][0] + (1 if nodes[i][0]<nodes[i+1][0] else -1), 1 if nodes[i][0]<nodes[i+1][0] else -1):
                blocked_nodes.add((x, nodes[i][1]))
        else:
            for y in range(nodes[i][1], nodes[i+1][1] + (1 if nodes[i][1]<nodes[i+1][1] else -1), 1 if nodes[i][1]<nodes[i+1][1] else -1):
                blocked_nodes.add((nodes[i][0], y))

# Get the lowest point in our rock system. Any sand that goes below this (y>lowest_point) is falling into the void and lost
# And this means we can stop processing sand blocks.
lowest_point = max([n[1] for n in blocked_nodes])

# Simulate sand falling until we encounter one that falls into the void
while True:
    # Create a sand block at 500,0
    sand = (500, 0)

    # Move the new sand block until it comes to rest or falls into the void
    while True:
        # Can sand move down?
        if (sand[0], sand[1]+1) in blocked_nodes:
            # Can sand move down and left?
            if (sand[0]-1, sand[1]+1) in blocked_nodes:
                # Can sand move down and right?
                if (sand[0]+1, sand[1]+1) in blocked_nodes:
                    # Sand cannot move and comes to rest - add it to the blocked_nodes set
                    blocked_nodes.add(sand)
                    sand_count += 1
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
        
        if sand[1] > lowest_point:
            # Sand is falling into the void
            break

    # Did the last block of sand fall into the void?
    if sand[1] > lowest_point:
        # Sand is falling into the void - stop simulation
        break

# Print the number of nodes in blocked_nodes
print(sand_count)