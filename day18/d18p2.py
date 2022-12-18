# open and read the input file
input_file = open("day18/input.txt", "r")
input = input_file.read().split("\n")

# Turn the input into a list of blocks
# blocks = [(int(x), int(y), int(z)) for [x, y, z] in [line.split() for line in input]]
blocks = [(int(x), int(y), int(z)) for s in input for (x, y, z) in [s.split(",")]]

# Find the max and min extent of the scan in each direction. Add one cube in each direction for airflow.
max_x, max_y, max_z = max([a[0] for a in blocks])+1, max([a[1] for a in blocks])+1, max([a[2] for a in blocks])+1
min_x, min_y, min_z = min([a[0] for a in blocks])-1, min([a[1] for a in blocks])-1, min([a[2] for a in blocks])-1
cube_in_range = lambda c: (min_x <= c[0] <= max_x) and (min_y <= c[1] <= max_y) and (min_z <= c[2] <= max_z)

# Lists of already found interior and exterior cubes
exterior_cubes = []
interior_cubes = []

# Function to create an extent (a bunch of connected cubes) that looks for a way to the edge. If we get to 
# an out of bounds then this is an exterior extent. If we find another cube that is exterior then this is 
# also exterior. If we find another cube that is interior then this is also interior.
def is_exterior(cube: tuple) -> bool:
    global blocks, exterior_cubes, interior_cubes

    extent = [cube]

    for e in extent:
        for direction in [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]:
            adjascent_cube = (e[0] + direction[0], e[1] + direction[1], e[2] + direction[2])
            if cube_in_range(adjascent_cube):
                # If we reach an exterior cube then this must also be an exterior cube
                if adjascent_cube in exterior_cubes:
                    exterior_cubes.extend(extent)
                    exterior_cubes = list(set(exterior_cubes))  # Remove duplicates
                    return True

                # If we reach an interior cube then this must also be an interior cube
                # This should never happen
                if adjascent_cube in interior_cubes:
                    interior_cubes.extend(extent)
                    interior_cubes = list(set(interior_cubes))  # Remove duplicates
                    return False

                # Don't add any cube multiple times
                if adjascent_cube in extent:
                    continue

                # Don't add any cube that is a block
                if adjascent_cube in blocks:
                    continue

                # Looks like a valid cube. Add it to the search list
                extent.append(adjascent_cube)
            else:
                # We have reached the edge so this is definitely an exterior extent
                exterior_cubes.extend(extent)
                exterior_cubes = list(set(exterior_cubes))  # Remove duplicates
                return True
    
    # If we run out of cubes in this extent without reaching an out of bounds then this is 
    # an interior extent
    interior_cubes.extend(extent)
    interior_cubes = list(set(interior_cubes))  # Remove duplicates
    return False

#########################
#### MAIN LOOP START ####
#########################

# Look at the blocks one by one. Add 6 faces. 
# Look in each direction to see if there's a block there and if so then subtract a face.
# If not then look at the empty adjascent block and "drop gas" there to see if the gas
# reaches out of bounds. If so then it's exterior and the face counts. 
exterior_faces = 0
possible_interior_cubes = []
for block in blocks:
    exterior_faces += 6
    for direction in [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]:
        # First check for an adjascent block. If there is one then this face can't be interior so continue
        adjascent_cube = (block[0] + direction[0], block[1] + direction[1], block[2] + direction[2])
        if adjascent_cube in blocks:
            exterior_faces -= 1
            continue
        else:
            if not is_exterior(adjascent_cube):
                exterior_faces -= 1

# Print the answer
print(exterior_faces)