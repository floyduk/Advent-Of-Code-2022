import re

# open and read the input file
input_file = open("day15/input.txt", "r")
input = input_file.read().split("\n")

# Lambda function to calculate manhattan distance
manhattan_distance = lambda s, b: abs(s[0] - b[0]) + abs(s[1] - b[1])

# A list of sensors (key) and beacons (value) locations
sensors = dict()

# min_xy, max_xy define the search area
min_xy, max_xy = 0, 4000000

# Parse the input file
for line in input:
    # Grab values from the input string. Convert them too integers and store them in sensors dict.
    m = re.match("^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$", line)
    sx, sy, bx, by = [int(n) for n in m.groups()]
    sensors[(sx, sy)] = (bx, by)

# Check if a point is covered by any sensor. Stop when we find one that isn't. This is the answer.
count=0
def check_point(x: int, y: int):
    global count
    if min_xy <= x <= max_xy and min_xy <= y <= max_xy:
        count += 1
        if count%10000 == 0:
            print(".", end="")

        for s, b in sensors.items():
            if manhattan_distance(s, (x, y)) <= manhattan_distance(s, b):
                return
        
        # If we get here then we found an answer
        print("\nAnswer:" + str(x * 4000000 + y))
        exit(0)

# Iterate the sensors. s is sensor coordinates. b is beacon coordinates. d is manhattan distance.
# Looking for points that are exactly 1 step outside the range of each sensor then call check_point()
# on each one to check if it is covered by any other sensor.
points = set()
for s, b in sensors.items():
    # Calculate the manhattan distance between the sensor and beacon and then the extents of the diamond 
    # of points just out of range of the beacon
    d = manhattan_distance(s, b)
    top_y, bottom_y = s[1] - d - 1, s[1] + d + 1
    right_x, left_x = s[0] + d + 1, s[0] - d - 1

    print("\nSensor: " + str(s) + " range " + str(d) + ": ", end="")

    r = manhattan_distance(s, b) + 1
    for dy in range(-r, r+1):
        check_point(s[0] - (r - dy), s[1] + dy)
        check_point(s[0] + (r - dy), s[1] + dy)
