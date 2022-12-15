import re

# open and read the input file
input_file = open("day15/input.txt", "r")
input = input_file.read().split("\n")

# Lambda function to calculate manhattan distance
manhattan_distance = lambda s, b: abs(s[0] - b[0]) + abs(s[1] - b[1])

# A list of sensors (key) and beacons (value) locations
sensors = dict()

# The y position we're interested in and a list of ranges in that row covered by sensors
target_y = 2000000
target_row = []

# Parse the input file
for line in input:
    # Grab values from the input string. Convert them too integers and store them in sensors dict.
    m = re.match("^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$", line)
    sx, sy, bx, by = [int(n) for n in m.groups()]
    sensors[(sx, sy)] = (bx, by)

# Iterate the sensors. s is sensor coordinates. b is beacon coordinates. d is manhattan distance
for s, b in sensors.items():
    # Calculate the manhattan distance between the sensor and beacon
    d = abs(s[0] - b[0]) + abs(s[1] - b[1])

    # Calculate the range of points in the target row covered by this sensor
    range_start = s[0] - (d - abs(s[1] - target_y))
    range_end =  s[0] + (d - abs(s[1] - target_y))
    target_row.append((range_start, range_end))

# Count the spaces on the target row
target_row_count = 0
smallest_range_start = min([s[0] for s in target_row])
largest_range_end = max([s[1] for s in target_row]) 
for i in range(smallest_range_start, largest_range_end):
    for r in target_row:
        if r[0] <= i <= r[1]:
            target_row_count += 1
            break

# Remove sensors and beacons from the target_row data
for s, b in sensors.items():
    # if s[1] == target_y and s[0] in target_row:
    #     target_row.remove(s[0])
    if b[1] == target_y and b[0] in target_row:
        target_row_count += -1

print(f"{target_row_count}")