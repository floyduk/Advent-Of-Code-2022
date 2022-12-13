# open and read the input file
input_file = open("day13/sample.txt", "r")
lines = input_file.read().split("\n")

# This function MUST be given 2 lists. 
# If an item in the list is a list then it calls itself recursively with the sublists
def order_correct(left, right) -> str:
    print(f"Compare {left} vs {right}")
    for i in range(1000):   # Giving this a max iterations to avoid lockups
        # First check if we've run out of values in one of the lists
        if i >= len(left) and i >= len(right):
            # Both ran out at the same time
            return "ambiguous"
        elif i >= len(left) and i < len(right):
            # Left ran out first - pair correctly ordered
            return "correct"
        elif i < len(left) and i >= len(right):
            # Right ran out first - pair incorrectly ordered
            return "incorrect"

        # Grab the left and right values - just for readability
        lv, rv = left[i], right[i]

        # left and right are both integers - just compare them
        if type(lv) == int and type(rv) == int:
            print(f"Compare {lv} vs {rv}")
            if lv < rv:
                return "correct"
            elif rv < lv:
                return "incorrect"
            
        # left is int and right is list - turn the int into a list and call again
        elif type(lv) == int and type(rv) == list:
            retval = order_correct([lv], rv)
            if retval != "ambiguous":
                return retval

        # left is list and right is int - turn the int into a list and call again
        elif type(lv) == list and type(rv) == int:
            retval = order_correct(lv, [rv])
            if retval != "ambiguous":
                return retval

        # left and right are both lists - call again using the lists
        elif type(lv) == list and type(rv) == list:
            retval = order_correct(lv, rv)
            if retval != "ambiguous":
                return retval

    return "ambiguous"

# Read in the file and create a pairs list
next_up = "left"
pairs = []
for line in lines:
    if line == "":
        pairs.append((left, right))
        next_up = "left"
    else:
        if next_up == "left":
            left = eval(line)
            next_up = "right"
        else:
            right = eval(line)
pairs.append((left, right))

# Iterate the pairs checking for ordering
sum_of_correctly_ordered_indices = 0
for i in range(len(pairs)):
    sum_of_correctly_ordered_indices += (i+1) if order_correct(pairs[i][0], pairs[i][1]) == "correct" else 0
    print("")

# Print the solution
print(sum_of_correctly_ordered_indices)
