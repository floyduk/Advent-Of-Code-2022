# open and read the input file
input_file = open("day10/input.txt", "r")
commands = input_file.read().split("\n")

# The pixels on-screen. We'll split this into lines when we display it.
pixels = ""

# The cycle number and starting x value
cycle = 1
x = 1

# Every cycle we draw a pixel and then increase the cycle number.
def increase_cycle():
    global cycle, x, pixels
    pixels += "#" if abs(x - ((cycle-1) % 40)) <= 1 else "."
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
print(pixels[0:40] + "\n" + pixels[40:80] + "\n" + pixels[80:120] + "\n" + pixels[120:160] + "\n" + pixels[160:200] + "\n" + pixels[200:])