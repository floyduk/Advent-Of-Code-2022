# open and read the input file
input_file = open("day8/input.txt", "r")
trees = input_file.read().split("\n")
rows = len(trees)
cols = len(trees[0])

# A list of scenic scores of every interior tree
scenic_scores = []

# Function to calculate the view distance based on a view. This function receives the
# current tree height and a list that is the view from this tree in a direction. This
# function looks along that view and stops when it finds a tree that is the same height
# or taller. It returns the count of how far it got. Views arrive in reverse order.
def view_distance(view, this_tree_height) -> int:
    view.reverse()
    for count in range(len(view)):
        if view[count] >= this_tree_height:
            break
    return count+1

# Look at all the trees in the middle and figure out how far we can see from there in each direction
for y in range(1, rows-1):
    for x in range(1, cols-1):
        # Get this tree height. If there are only smaller trees between here and the edge
        # then this tree is visible
        this_tree_height = int(trees[y][x])

        # Get the view in each direction from this tree. The slicing method I used works 
        # inward from the edge of the array and so the views have to be reversed to make
        # them look outward from the target tree. We then pass the view to view_distance()
        # to calculate how far we can see in that direction.
        view_left_distance = view_distance([int(t) for t in trees[y][:x]], this_tree_height)
        view_right_distance = view_distance([int(t) for t in trees[y][:x:-1]], this_tree_height)
        view_up_distance = view_distance([int(t[x]) for t in trees[:y]], this_tree_height)
        view_down_distance = view_distance([int(t[x]) for t in trees[:y:-1]], this_tree_height)

        # Calculate the scenic score by multiplying the view distances
        scenic_scores.append(view_left_distance * view_right_distance * view_up_distance * view_down_distance)

# Print the answer
print(max(scenic_scores))