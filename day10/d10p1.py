# open and read the input file
input_file = open("day10/input.txt", "r")
commands = input_file.read().split("\n")

# The total signal strength
signal_strength = 0

# The cycle number and starting x value
cycle = 1
x = 1

# Every cycle we check to see if this is a cycle we're interested in and if it is
# then add x value multiplied by the cycle to the signal strength total. 
# Then finally increase the cycle number.
def increase_cycle():
    global cycle, x, signal_strength
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength += (x * cycle)
    cycle += 1

# Iterate the commands in the input file
for command in commands:
    # If the command is a noop just save the x value and increase the cycle number
    if command == "noop":
        increase_cycle()
    else:
        # Get the value to be added to x
        parameter = int(command.split()[1])

        # Increase the cycle twice
        increase_cycle()
        increase_cycle()

        # Then add to x
        x += parameter

# Print the answer
print(signal_strength)