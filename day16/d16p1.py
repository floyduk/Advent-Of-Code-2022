from copy import copy
import time

start_time = time.process_time()

# open and read the input file
input_file = open("day16/input.txt", "r")
input = input_file.read().split("\n")

class valve:
    name: str
    rate: int
    leads_to: dict
    def __init__(self, name: str, rate: int, leads_to: list) -> None:
        self.name = name
        self.rate = rate
        self.leads_to = dict()
        for l in leads_to:
            self.leads_to[l] = 1
        self.valves_this_way = set()
    def sorted_leads_to(self):
        global valves
        for a in sorted(self.leads_to.items(), key=lambda item: valves[item[0]].rate, reverse=True):
            yield a

# A dict of valves
valves = dict()

# Parse input and create a dict of values
for line in input:
    words = line.split()
    valves[words[1]] = valve(words[1], int(words[4].split("=")[1][:-1]), [w.rstrip(",") for w in words[9:]])

# Get the total of all valves rates
total_max_rates = sum([valves[v].rate for v in valves])

# Function to track reported results
max_total_pressure = 0
def report_result(path: list, total_pressure: int):
    global max_total_pressure
    if(total_pressure > max_total_pressure):
        max_total_pressure = total_pressure
        print(f"Total pressure released: {total_pressure}, path: {path}")

# Function to prevent repetition
def detect_repetition(vn: str, path: list) -> bool:
    for i in range(2, 4):
        if len(path) < (i*2)-1:
            break

        part1 = [*path[-i+1:], vn]
        part2 = path[-(i*2)+1:-i+1]
        if part1 == part2:
            return True
    return False

# Check if there are any unopened valves beyond this node
# def nothing_useful_this_way(v: valve, my_remaining_valves: list) -> bool:
#     return len([r for r in my_remaining_valves if r in v.valves_this_way]) == 0

# Recursive function to traverse the tree
def go_to_valve(vname:str, path: list, mins_left: int, total_pressure: int, remaining_rate: int, remaining_valves: list, travel_time: int):
    global max_total_pressure
    global valves

    my_valve = valves[vname]

    # cull this branch if there's no way it can match the current max_total_pressure
    if total_pressure + (remaining_rate * (mins_left-len(remaining_valves))) < max_total_pressure:
        return

    my_remaining_valves = remaining_valves.copy()

    # If there is a travel time then account for it
    if travel_time > 0:
        mins_left = mins_left - travel_time             # For the travel time
        if mins_left < 1:
            report_result([*path, vname], total_pressure)
            return

    # Now go to the next valve based on their value without first opening this valve
    for vn, travel_cost in my_valve.sorted_leads_to():
        if len(my_remaining_valves) == 0:
            continue

        # Cull paths where we alternate between the last 2 nodes or 3 nodes
        if detect_repetition(vn, [*path, vname]):
            continue

        go_to_valve(vn, [*path, vname], mins_left, total_pressure, remaining_rate, my_remaining_valves, travel_cost)

    # If this valve has non zero value and this is our first time here then open it - taking 1 minute
    if my_valve.rate > 0 and vname in my_remaining_valves:
        mins_left = mins_left - 1           # For opening the valve
        total_pressure += my_valve.rate * mins_left
        remaining_rate -= my_valve.rate     # Reduce the remaining available rate
        my_remaining_valves.remove(vname)   # Remove this valve from the list of remaining valves
        if mins_left < 1:
            report_result([*path, vname], total_pressure)
            return
    
        # Now go to the next valve based on their value
        for vn, travel_cost in my_valve.leads_to.items():
            if len(my_remaining_valves) == 0:
                continue

            # Cull paths where we alternate between the last 2 nodes or 3 nodes or 4 or 5 nodes
            if detect_repetition(vn, [*path, vname]):
                continue

            go_to_valve(vn, [*path, vname], mins_left, total_pressure, remaining_rate, my_remaining_valves, travel_cost)
    
    # Nowhere else to go. Wait here until the time is up
    report_result([*path, vname], total_pressure)
    return


# Simplify the network
def simplify(vname, path) -> list:
    global valves

    my_valve = valves[vname]

    # If this node only leads to one other node AND it has a zero rate then it can be simplified out
    if len(my_valve.leads_to) == 2 and path[-1] in my_valve.leads_to.keys() and my_valve.rate == 0:
        print(f"Removing node {vname} - ", end="")
        # Get the last and next node names
        last_node = path[-1]
        last_cost = my_valve.leads_to[last_node]
        del my_valve.leads_to[last_node]
        for next_node, next_cost in my_valve.leads_to.items():
            # Add the next node to the previous nodes's leads_to
            if next_node in valves[last_node].leads_to:
                valves[last_node].leads_to[next_node] += valves[last_node].leads_to[vname]
            else:
                valves[last_node].leads_to[next_node] = valves[last_node].leads_to[vname]+next_cost

            # Delete this node from the last node's leads_to
            del valves[last_node].leads_to[vname]

            # Add the previous node to the next node's leads_to
            if last_node in valves[next_node].leads_to:
                valves[next_node].leads_to[last_node] += valves[next_node].leads_to[vname]
            else:
                valves[next_node].leads_to[last_node] = valves[next_node].leads_to[vname]+last_cost

            # Delete this node from the next node's leads_to
            del valves[next_node].leads_to[vname]
        
        # Delete the next_node from this node's leads_to
        del my_valve.leads_to[next_node]
        
        print(f"{last_node}.leads_to={valves[last_node].leads_to}, {next_node}.leads_to={valves[next_node].leads_to}")

        # Something changed so return true
        return True

    something_changed = True
    while something_changed:
        something_changed = False
        for next_valve in my_valve.leads_to.keys():
            if next_valve in path:
                continue

            if something_changed := simplify(next_valve, [*path, vname]):
                break

    return False

# Simplify the network with a valves_this_way entry on valve objects
simplify("AA", [])

# Start at AA
init_remaining_valves = [vn for vn in valves.keys() if valves[vn].rate > 0]
go_to_valve("AA", [], 30, 0, total_max_rates, init_remaining_valves, 0)

print(max_total_pressure)
print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
