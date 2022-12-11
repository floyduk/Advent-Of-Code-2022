from math import lcm

# open and read the input file
input_file = open("day11/input.txt", "r")
lines = input_file.read().split("\n")

# A class to hold Monkey data
class Monkey:
    items: list
    operator: str
    operand: int
    divisible_by: int
    true_dest: int
    false_dest: int
    inspection_count: int
    def __init__(self, i, op, operand, divisible_by, true_dest, false_dest) -> None:
        self.items = i
        self.operator = op
        self.operand = operand
        self.divisible_by = divisible_by
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspection_count = 0

# A list of monkeys
monkeys = []

# Read in the input file, creating Monkey objects and populating them with the starting data
for line in lines:
    if line.startswith("Monkey"):
        monkey_number = int(line[7])
    elif line.startswith("  Starting items: "):
        items_list = [int(a) for a in line[18:].split(", ")]
    elif line.startswith("  Operation: new = old "):
        operator, operand = line[23], int(line[25:]) if line[25:] != "old" else -1
    elif line.startswith("  Test: divisible by "):
        divisible_by = int(line[21:])
    elif line.startswith("    If true: throw to monkey "):
        true_dest = int(line[29:])
    elif line.startswith("    If false: throw to monkey "):
        false_dest = int(line[30:])
    elif line == "":
        monkeys.append(Monkey(items_list, operator, operand, divisible_by, true_dest, false_dest))
monkeys.append(Monkey(items_list, operator, operand, divisible_by, true_dest, false_dest))

# Get the least common multiple of all the monkey's divisors
least_common_multiple = lcm(*[monkey.divisible_by for monkey in monkeys])

# Now throw items for 10000 rounds
for round_number in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            # Monkey inspects the item
            if monkey.operand == -1:
                item = item * item
            elif monkey.operator == "+":
                item += monkey.operand
            else:
                item *= monkey.operand

            # Count the number of times this monkey inspects stuff
            monkey.inspection_count += 1

            # Instead of dividing by 3 as in part 1 we divide by the least common multiple and get the remainder
            item = item % least_common_multiple

            # monkeys[monkey.true_dest if item % monkey.divisible_by == 0 else monkey.false_dest].items.append(item)
            if item % monkey.divisible_by == 0:
                monkeys[monkey.true_dest].items.append(item)
            else:
                monkeys[monkey.false_dest].items.append(item)

        # Monkeys never throw to themselves so at the end of throws a monkey's items_list must be empty
        monkey.items = []

# Calculate monkey business values
most_inspections = sorted([m.inspection_count for m in monkeys], reverse=True)
print(most_inspections[0] * most_inspections[1])
