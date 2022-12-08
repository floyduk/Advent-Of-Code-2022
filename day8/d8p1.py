# open and read the input file
input_file = open("day8/input.txt", "r")
trees = input_file.read().split("\n")
rows = len(trees)
cols = len(trees[0])

# The number of visible trees - initialize with all the exterior trees
visible_tree_count = (2*cols) + (2*(rows-2))

# Look at all the trees in the middle and see if we can see a clear path to any edge
for y in range(1, rows-1):
    for x in range(1, cols-1):
        # Get this tree height.
        this_tree_height = int(trees[y][x])

        # Return a list of trees taller than or equal to the height of this tree 
        # between this one and the edge. If this list is empty then this tree is visible
        # LOOK LEFT
        if len([int(t) for t in trees[y][:x] if int(t) >= this_tree_height]) == 0:
            visible_tree_count += 1
            continue

        # LOOK RIGHT
        if len([int(t) for t in trees[y][:x:-1] if int(t) >= this_tree_height]) == 0:
            visible_tree_count += 1
            continue

        # LOOK UP
        if len([int(t[x]) for t in trees[:y] if int(t[x]) >= this_tree_height]) == 0:
            visible_tree_count += 1
            continue

        # LOOK DOWN
        if len([int(t[x]) for t in trees[:y:-1] if int(t[x]) >= this_tree_height]) == 0:
            visible_tree_count += 1
            continue

# Display the number of visible trees
print(visible_tree_count)
