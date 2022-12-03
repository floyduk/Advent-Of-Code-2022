# open and read the input file
input_file = open("day3/input.txt", "r")
input_lines = input_file.read().split("\n")

# A short function to convert a char into a priority value
to_priority = lambda a : ord(a)-38 if a.isupper() else ord(a)-96

# The total sum of priorities what will become our puzzle answer
sum_of_priorities = 0

# Iterate the file 
for line in input_lines:
    # Split each line in half, convert each half into a set and then find the intersection of the sets
    # Then convert the intersection into a priority value and add it to the total
    sum_of_priorities += to_priority((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop())

# Print the total sum of priorities
print(sum_of_priorities)