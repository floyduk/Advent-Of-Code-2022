# open and read the input file
input_file = open("day13/input.txt", "r")
lines = input_file.read().split("\n")

# This function MUST be given 2 lists. 
# If an item in the list is a list then it calls itself recursively with the sublists
def order_correct(left, right) -> str:
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

# Read in the file and create a packets list
packets = []
for line in lines:
    if line == "":
        continue
    else:
        packets.append(line)

# Add the two divider packets
packets.append("[[2]]")
packets.append("[[6]]")

# Bubble sort the packets
swaps = 1
while swaps > 0:
    swaps = 0
    for i in range(len(packets)-1):
        if order_correct(eval(packets[i]), eval(packets[i+1])) == "incorrect":
            p = packets[i]
            packets[i] = packets[i+1]
            packets[i+1] = p
            swaps = 1

# Find the divider packets and print the solution
index1 = packets.index("[[2]]") + 1
index2 = packets.index("[[6]]") + 1
print(index1 * index2)