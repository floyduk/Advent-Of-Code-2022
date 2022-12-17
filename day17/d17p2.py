import time

start_time = time.process_time()

# open and read the input file
input_file = open("day17/input.txt", "r")
gasses = input_file.read()
lg = len(gasses)
loop = lg * 5 # This should be the phase repetition of blocks and gasses

blocks = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (0,1), (1,1), (2,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (0,1), (1,0), (1,1)]
]

impulses = {">": (1,0), "<": (-1,0), "V": (0,-1)}

calc_x = lambda x, p, i: x + p[0] + i[0]
calc_y = lambda y, p, i: y + p[1] + i[1] % window_size

# Keep track of which gas jet is next
gas_jet = 0

# Cull everything below this mark. We only keep 1000 rows above this
window_size = 5000

# The current top point
max_y = 0

# Create a grid of window_size - we already have 1 row
grid = [[0,1,2,3,4,5,6]]
for i in range(window_size-1):
    grid.append([])

# Check if this move will work. Return the new modified or unmodified coords with success/fail
def check_move(direction, block, x, y):
    # Get the impulse vector for this direction
    i = impulses[direction]

    # Check each point in the block
    for p in block:
        cx, cy = x + p[0] + i[0], y + p[1] + i[1]
        if cx < 0 or cx >= 7:
            return (x,y, False) # Crashed into a wall
        if cx in grid[cy % window_size]:
            return (x,y, False) # Crashed into another block or ground
    
    # Not crashed into anything. Return the modified x,y coordinates.
    return (x+i[0], y+i[1], True)

#########################
#### MAIN LOOP START ####
#########################

last_max_y = 0

# These magic numbers came from a lot of testing and looking for patterns. Finally found a pattern at 215000 
# iterations. The first 215000 gives one number of rows and each thereafter gives a solidly consistant other
# value. So I iterate 215000+the remainder after dividing and modding the 1000000000 intended runs.
# 2738 height added per lg gas gusts - this wasn't useful
# 342265 for the first 215000
# 342250 for each 215000 after that
multiples = 1000000000000//215000
remainder = 1000000000000%215000
for i in range(215000 + remainder):
    if i % (5000*43) == 0:
        print(f"{max_y - last_max_y}, {5000*43}")
        # print(max_y, ": execution time (in ms): ",(time.process_time()-start_time)*1000) 
        last_max_y = max_y

    # Choose a block and set its location
    block = blocks[i % 5]
    x = 2
    y = max_y + 4
    grid[(y+4) % window_size].clear()
    grid[(y+3) % window_size].clear()
    grid[(y+2) % window_size].clear()
    grid[(y+1) % window_size].clear()
    grid[y % window_size].clear()
    grid[(y-1) % window_size].clear()
    grid[(y-2) % window_size].clear()
    grid[(y-3) % window_size].clear()

    # Drop it till it stops
    while True:
        # Push sideways
        (x,y, result) = check_move(gasses[gas_jet % lg], block, x, y)
        gas_jet += 1

        # Fall down
        (x,y, result) = check_move("V", block, x, y)
        if result == False:
            break   # Block has landed so stop this block moving
    
    # Make the block part of col_tops
    for p in block:
        cy = y+p[1]
        grid[cy % window_size].append(x+p[0])
        if cy > max_y:
            max_y = cy 

# I consider row 0 to be the floor. Eric has it at -1. So I was off by 1.
print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
print(max_y + ((multiples-1) * 342250))