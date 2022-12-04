import re

# open and read the input file
input_file = open("day4/input.txt", "r")
input_lines = input_file.read().split("\n")

# Count of partial overlaps
count_partial_overlaps = 0

# Iterate the file 
for line in input_lines:
    # Split the line wherever there is either a , or a -. Then convert each piece into an int. Should give us 4 integer values.
    p1_start, p1_end, p2_start, p2_end = [int(a) for a in re.split("[,-]", line)]

    # Check if start and end are the same as or inside the range of the other pair. Check both ways round
    if(p2_start <= p1_start <= p2_end) or (p2_start <= p1_end <= p2_end) \
        or (p1_start <= p2_start <= p1_end) or (p1_start <= p2_end <= p1_end):
        count_partial_overlaps += 1

# Print the total sum of priorities
print(count_partial_overlaps)