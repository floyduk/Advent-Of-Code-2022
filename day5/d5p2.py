import re

# open and read the input file
input_file = open("day5/input.txt", "r")
input_lines = input_file.read().split("\n")

# Start by figuring out where stuff is in our input file. First find a blank line
line_number, blank_line_number = 0, 0
for line in input_lines:
    if line == "":
        blank_line_number = line_number
    else:
        line_number += 1

# Now we know where the blank line is we also know that the column labels are the line above
# So grab that and parse it to learn how many columns we have
num_columns = len(input_lines[blank_line_number-1].split())

# So now we know how many columns we have an where the bottom element is of each column.
# So we can now read UP from there until we find the top of the file or a blank to populate 
# our starting columns
stack_num = 0
stacks = []     # This will be a list of lists. Each sublist will be used as a stack
for x in range(1, num_columns*4, 4):    # x becomes the x position in the line for this column
    stacks.append([])                   # Create a new blank list
    for y in range(blank_line_number-2, -1, -1):
        if(input_lines[y][x] != " "):
            stacks[stack_num].append(input_lines[y][x])
    stack_num += 1

# Now we have our stacks loaded in correctly. Next we iterate the move instructions.
for line_number in range(blank_line_number+1, len(input_lines)):
    # Pull the line into words and grab the ones we are interested in. Then convert
    # those values to integers and adjust values for zero order array indexes.
    words = input_lines[line_number].split()
    count, from_stack, to_stack = int(words[1]), int(words[3])-1, int(words[5])-1   

    # Perform the move
    stacks[to_stack].extend(stacks[from_stack][-count:])
    stacks[from_stack] = stacks[from_stack][:-count]

# Finally print our answer by printing the top value from each stack
for stack in stacks:
    print(stack[-1], end="")