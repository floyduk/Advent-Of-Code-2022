input_file = open("day21/input.txt", "r")
input = input_file.read().split("\n")

# Process the input and make a dict of monkeys and their expressions
monkeys = dict()
for line in input:
    monkey_name, expression = line.split(": ")
    monkeys[monkey_name] = expression.split() if " " in expression else int(expression)

def find_value_of(monkey_name):
    monkey = monkeys[monkey_name]

    if len(monkey) == 1:
        # One element means this is just an integer
        return monkey[0]
    else:
        # More than one elements means this is an expression
        m1 = monkeys[monkey[0]] if type(monkeys[monkey[0]]) == int else find_value_of(monkey[0])
        m2 = monkeys[monkey[2]] if type(monkeys[monkey[2]]) == int else find_value_of(monkey[2])

        return eval(f"{m1} {monkey[1]} {m2}")

#############
# MAIN LOOP #
#############

print(int(find_value_of("root")))