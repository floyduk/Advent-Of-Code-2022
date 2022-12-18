# open and read the input file
input_file = open("day18/input.txt", "r")
input = input_file.read().split("\n")

# Turn the input into a list of blocks
# blocks = [(int(x), int(y), int(z)) for [x, y, z] in [line.split() for line in input]]
blocks = [(int(x), int(y), int(z)) for s in input for (x, y, z) in [s.split(",")]]

# Look at the blocks one by one. Add 6 faces. 
# Look in each direction to see if there's a block there and if so then subtract a face.
count_faces = 0
for block in blocks:
    count_faces += 6
    for direction in [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]:
        if (block[0] + direction[0], block[1] + direction[1], block[2] + direction[2]) in blocks:
            count_faces -= 1

# Print the answer
print(count_faces)