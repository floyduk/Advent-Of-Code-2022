# open and read the input file
input_file = open("day3/input.txt", "r")
input_lines = input_file.read().split("\n")

# A short function to convert a char into a priority value
to_priority = lambda a : ord(a)-38 if a.isupper() else ord(a)-96

# The total sum of priorities what will become our puzzle answer
sum_of_priorities = 0

# Iterate the file 
for line in input_lines:
    # splitting each line in half and convert each half into a set
    part_length = int(len(line)/2)
    (line_part_1, line_part_2) = (set(line[:part_length]), set(line[part_length:]))

    # find the intersation of the first and second half sets
    intersection = line_part_1 & line_part_2

    # Get the priority of the intersection and add it to our sum of priorities
    sum_of_priorities += to_priority(intersection.pop())

# Print the total sum of priorities
print(sum_of_priorities)