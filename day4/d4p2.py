# open and read the input file
input_file = open("day4/input.txt", "r")
input_lines = input_file.read().split("\n")

# Count of partial overlaps
count_partial_overlaps = 0

# Iterate the file 
for line in input_lines:
    # I could probably do this more succinctly with a regexp but I'm rushing
    (pair1, pair2) = line.split(",")
    (p1_start, p1_end) = pair1.split("-")
    (p2_start, p2_end) = pair2.split("-")

    # Convert the numbers to integers
    (p1_start, p1_end, p2_start, p2_end) = (int(p1_start), int(p1_end), int(p2_start), int(p2_end))

    # Check if start and end are the same as or inside the range of the other pair. Check both ways round
    if(p2_start <= p1_start <= p2_end) or (p2_start <= p1_end <= p2_end) \
        or (p1_start <= p2_start <= p1_end) or (p1_start <= p2_end <= p1_end):
        count_partial_overlaps += 1

# Print the total sum of priorities
print(count_partial_overlaps)