import heapq

# open and read the input file
input_file = open("day12/input.txt", "r")
lines = input_file.read().split("\n")

# Get the dimensions of the grid
grid_width = len(lines[0])
grid_height = len(lines)

# Get a list of adjascent coordinates as a list of tuples
adjacents = lambda x, y: [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]

# Is the given point within the bounds of our data grid?
is_valid_coordinate = lambda p: (0 <= p[0] < grid_width and 0 <= p[1] < grid_height)

# Find the location of point S - the start point
for sy in range(grid_height):
    if "S" in lines[sy]:
        sx = lines[sy].find("S")
        break

# Add the source location to the list of points that need to be searched. I use a heapq
# here because it means that whenever I use heappop to grab the next node in the list it
# always gives me the node with the lowest cost - which is what I want for the Dijkstra 
# algorithm
search_points = []
heapq.heappush(search_points, (0, (sx, sy)))

# This is Dijykstra's algorithm for finding the shortest path between two points.
# There is an excellent explanation of this alogirthm here: 
# https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
visited_nodes = set()
while search_points:
    cost, here = heapq.heappop(search_points)
    here_char = lines[here[1]][here[0]]             # The char at location here
    if here_char == "S":
        here_char = "a"

    # If we've reached the destination then stop and show the answer
    if here_char == "E":
        print("Solution: ", cost)
        exit()

    # Move on if this node has already been visited
    if here in visited_nodes: 
        continue

    # Add this point to the list of visited nodes
    visited_nodes.add(here)

    # Adjacent nodes
    for p in adjacents(here[0], here[1]):
        # Move on if this adjacent node isn't valid
        if is_valid_coordinate(p):
            point_char = lines[p[1]][p[0]]          # The char at point p
            if point_char == "E":
                point_char = "z"

            # A node is only adjascent if it's at most one char greater
            if ord(point_char) - ord(here_char) <= 1:
                heapq.heappush(search_points, (cost + 1, p))