# open and read the input file
input_file = open("day20/input.txt", "r")
input = [int(l) for l in input_file.read().split("\n")]
l = len(input)

# Make an array of bool that tracks which numbers have been touched
touched = [False] * l

#############
# MAIN LOOP #
#############

# print("S: ", input, "\n")

p = 0               # Location pointer
count_moved = 0     # Count now many numbers we've moved
while count_moved < l:
    # Get the value of this number
    v = input[p]

    # Never move a number more than once. If it's touched then it has been moved
    if touched[p]:
        p = (p+1) % l
        continue

    # Move it
    if v != 0:
        new_p = (p + v + 1) % l if v >= 0 else (p + v) % l
        if new_p == 0:
            new_p = l
        input.insert(new_p, v)
        touched.insert(new_p, True)
        if(new_p < p):
            input.pop(p+1)
            touched.pop(p+1)
        else:
            input.pop(p)
            touched.pop(p)
    else:
        new_p = p
        touched[p] = True
    
    # Keep track of how many numbers we've moved. Quit the loop when it's all of them
    count_moved += 1

    # print(f"{v} moved from {p} to {new_p}\n", input, "\n")

zero_index = input.index(0)
print(input[(zero_index+1000) % l] + input[(zero_index+2000) % l] + input[(zero_index+3000) % l])