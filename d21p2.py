input_file = open("day21/input.txt", "r")
input = input_file.read().split("\n")

# Process the input and make a dict of monkeys and their expressions
monkeys = dict()
for line in input:
    monkey_name, expression = line.split(": ")
    monkeys[monkey_name] = expression.split() if " " in expression else int(expression)

#############
# FUNCTIONS #
#############

# 3 step function to simplify our monkey data down to only expressions with 1 number and 1 monkey name
def simplify_monkeys() -> None:
    global monkeys
    # Simplify step 1 - Turn all expressions where both sides are int into ints
    updates = 1
    while(updates != 0):
        updates = 0
        for monkey_name, m in monkeys.items():
            if type(m) == int:
                continue
            else:
                if m[0] != "humn" and m[2] != "humn":
                    if type(monkeys[m[0]]) == int and type(monkeys[m[2]]) == int:
                        monkeys[monkey_name] = int(eval(f"{monkeys[m[0]]} {m[1]} {monkeys[m[2]]}"))
                        monkeys[m[0]], monkeys[m[2]] = 0, 0
                        updates += 1

    # Simplify step 2 - change monkey names to integers where we can
    for m in monkeys.values():
        if type(m) == int:
            continue
        else:
            if type(monkeys[m[0]]) == int and m[0] != "humn":
                mn = m[0]
                m[0] = monkeys[mn]
                monkeys[mn] = 0

            if type(monkeys[m[2]]) == int and m[2] != "humn":
                mn = m[2]
                m[2] = monkeys[mn]
                monkeys[mn] = 0

    # Simplify step 3 - delete all zero value monkeys (sorry monkeys)
    monkeys = {n:v for n, v in monkeys.items() if v != 0}

# Do the same to both sides of the remaining equation to solve for humn. Not even recursive. Simple simple.
def solve_for_humn(equality, monkey_name):
    while(monkey_name != "humn"):
        m = monkeys[monkey_name]
        operator = m[1]
        if type(m[2]) == int:
            if operator == "/":
                equality = equality * m[2]
            elif operator == "-":
                equality = equality + m[2]
            elif operator == "+":
                equality = equality - m[2]
            elif operator == "*":
                equality = equality // m[2]
            monkey_name = m[0]

        else:
            if operator == "/":
                    equality = m[0] / equality
            elif operator == "-":
                    equality = m[0] - equality
            elif operator == "+":
                    equality = equality - m[0]
            elif operator == "*":
                    equality = equality // m[0]
            monkey_name = m[2]

    return equality

#############
# MAIN LOOP #
#############

simplify_monkeys()
if type(monkeys["root"][0]) == int:
    print(solve_for_humn(monkeys["root"][0], monkeys["root"][2]))
else:
    print(solve_for_humn(monkeys["root"][2], monkeys["root"][0]))

################
# EXTRA CREDIT #
################

# Turn the monkey data into an equation - this isn't part of the AoC challenge. It's just a fun thing to do.
def get_expression_for(monkey_name):
    def subdo(m) -> None:
        if type(m) == int:
            return str(m)
        else:
            if m == "humn":
                return m
            else:
                return "(" + get_expression_for(m) + ")"

    if type(monkey_name) == int:
        return str(monkey_name)

    expression = ""
    expression += subdo(monkeys[monkey_name][0])
    expression += " " + monkeys[monkey_name][1] + " "
    expression += subdo(monkeys[monkey_name][2])

    return expression

print(get_expression_for(monkeys["root"][0]) + " = " + get_expression_for(monkeys["root"][2]))