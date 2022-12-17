import time

start_time = time.process_time()

# open and read the input file
input_file = open("day17/input.txt", "r")
gasses = input_file.read()

blocks = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (0,1), (1,1), (2,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (0,1), (1,0), (1,1)]
]

impulses = {">": (1,0), "<": (-1,0), "V": (0,-1)}

calc_x = lambda x, p, i: x + p[0] + i[0]
calc_y = lambda y, p, i: y + p[1] + i[1] - cf

# We must also keep a grid
grid = [[0,1,2,3,4,5,6]]

# Keep track of which gas jet is next
gas_jet = 0

# Cull everything below this mark. We only keep 1000 rows above this
window_size = 5000
cf = 0                  # Culling floor

def check_move(direction, block, x, y):
    # Get the impulse vector for this direction
    i = impulses[direction]

    # Check each point in the block
    for p in block:
        if not (len(grid) <= calc_y(y,p,i)) and (calc_x(x,p,i)) in grid[calc_y(y,p,i)]:
            return (x,y, False) # Crashed into another block or ground
        if calc_x(x,p,i) < 0 or calc_x(x,p,i) >= 7:
            return (x,y, False) # Crashed into a wall
    
    # Not crashed into anything. Return the modified x,y coordinates.
    return (x+i[0], y+i[1], True)

#########################
#### MAIN LOOP START ####
#########################

# Drop 2022 blocks keeping track of the col_tops
for i in range(1000000000000):
    if i % 100000 == 0:
        print(i, ": execution time (in ms): ",(time.process_time()-start_time)*1000) 

    # Choose a block and set its location
    block = blocks[i % len(blocks)]
    x = 2
    y = len(grid) + cf + 3

    # Drop it till it stops
    while True:
        # Push sideways
        (x,y, result) = check_move(gasses[gas_jet % len(gasses)], block, x, y)
        gas_jet += 1

        # Fall down
        (x,y, result) = check_move("V", block, x, y)
        if result == False:
            break   # Block has landed so stop this block moving
    
    # Make the block part of col_tops
    for p in block:
        # Create new grid rows until we have enough
        if len(grid) >= window_size:
            while (y+p[1]-cf) - len(grid) >= 0:
                grid.append([])
                cf += 1
                del grid[0]
            grid[-1].append(x+p[0])

        else:
            while (y+p[1]-cf) - len(grid) >= 0:
                grid.append([])
            grid[y+p[1]-cf].append(x+p[0])

# I consider row 0 to be the floor. Eric has it at -1. So I was off by 1.
print(len(grid)-1+cf)