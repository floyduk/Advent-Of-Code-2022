# open and read the input file
input_file = open("day3/input.txt", "r")

# A short function to convert a char into a priority value
to_priority = lambda a : ord(a)-38 if a.isupper() else ord(a)-96

# The total sum of priorities what will become our puzzle answer
sum_of_priorities = 0

# Iterate the file in bunches of 3 lines
while True:
    # Grab 3 lines from the input and convert them to sets
    (line1, line2, line3) = (set(input_file.readline().rstrip()), \
                             set(input_file.readline().rstrip()), \
                             set(input_file.readline().rstrip()))

    # If the first of the 3 lines is empty then we're done with this loop. Break out of it.
    if len(line1) == 0:
        break

    # Find the intersection of the 3 sets
    intersection = line1 & line2 & line3

    # Add the priority of the intersection to the sum of priorities
    sum_of_priorities += to_priority(intersection.pop())

# Print the total sum of priorities
print(sum_of_priorities)