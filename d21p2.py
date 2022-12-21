input_file = open("day21/sample.txt", "r")
input = input_file.read().split("\n")

# Process the input and make a dict of monkeys and their expressions
monkeys = dict()
for line in input:
    monkey_name, expression = line.split(": ")
    monkeys[monkey_name] = expression.split() if " " in expression else int(expression)

# 3 step function to simplify our monkey data
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
        print(updates)

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

# Turn the monkey data into an equation
def get_expression_for(monkey_name):
    def subdo(m) -> None:
        if type(m) == int:
            return str(m)
        else:
            if m == "humn":
                return m
            else:
                return "(" + get_expression_for(m) + ")"

    if type(monkeys[monkey_name]) == int:
        return str(int)

    expression = ""
    expression += subdo(monkeys[monkey_name][0])
    expression += " " + monkeys[monkey_name][1] + " "
    expression += subdo(monkeys[monkey_name][2])

    return expression

#############
# MAIN LOOP #
#############

simplify_monkeys()
print(get_expression_for("root"))