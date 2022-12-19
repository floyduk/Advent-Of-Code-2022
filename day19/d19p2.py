# open and read the input file
input_file = open("day19/input.txt", "r")
input = input_file.read().split("\n")

# Use the input to create a list of blueprints
blueprints = []
for line in input:
    words = line.split()
    blueprints.append([
        (int(words[6]), 0, 0),                  # Ore robot costs
        (int(words[12]), 0, 0),                 # Clay robot costs
        (int(words[18]), int(words[21]), 0),    # Obsidian robot costs
        (int(words[27]), 0, int(words[30])),     # Geode robot costs
        int(words[1][:-1])                      # Blueprint ID
    ])

# ROBOTS                        MATERIALS
# 0 = ore robot                 0 = ore
# 1 = clay robot                1 = clay
# 2 = obsidian robot            2 = obsidian
# 3 = geode robot               3 = geode

# Returns a list of robot types I can make where 0 is ore, 1 is clay, 2 is obsidian, 3 is geode
# The order we return these in guides the recursion to a faster answer. It shouldn't CHANGE the answer. 
# But it does.. so I have a bug.
def robots_i_can_make(robots: list) -> list:
    return [b for b in [1, 2 if robots[1] else None, 3 if robots[2] else None, 0] if b != None]

# If we have 1 turn left then 0 possible geodes. 2 turns, 1 possible, 3 turns, 1 possible, 4 turns 2 possible etc
possible_geodes = lambda n: ((n-1)*n)//2

# The main work goes on here. We recurse whenever we face a decision. The only decision is what robot to make next.
max_geodes = 0
def recurse(bp: dict, budget: int, bots: list, mats: list, making: int):
    global max_geodes

    # Culling test
    if mats[3] + (bots[3] * budget) + (possible_geodes(budget)) <= max_geodes:
        return

    while budget > 0:
        # Are we making something? If not then choose something to make.
        # We are making something so check if we have the materials for it yet.
        if mats[0] >= bp[making][0] and mats[1] >= bp[making][1] and mats[2] >= bp[making][2]:
            # Spend resources to start making the robot
            for i in range(3):
                mats[i] -= bp[making][i]

            # All robots mine materials
            for i in range(4):
                mats[i] += bots[i]

            # Finish making the robot
            bots[making] += 1
            making = None

        # We are making something but don't have the materials yet.
        else:
            # All robots mine materials
            for i in range(4):
                mats[i] += bots[i]
            
        # Time marches on
        budget -= 1
    
        # If we end this loop not making anything then 
        if making == None:
            for m in robots_i_can_make(bots):
                recurse(bp, budget, [*bots], [*mats], m)
            return 

    # We ran out of time. How many Geodes do we have?
    if mats[3] > max_geodes:
        max_geodes = mats[3]
        # print(f"{bots_made}: {max_geodes}")
    return

#############
# MAIN LOOP #
#############
max_geodes_list = []
for i in range(3):
    blueprint = blueprints[i]
    max_geodes = 0
    for m in [1, 0]:    # At the start we can only afford ore bots or clay bots
        recurse(blueprint, 32, [1,0,0,0], [0,0,0,0], m)
    print(f"Blueprint {blueprint[4]} produced {max_geodes} geodes")
    max_geodes_list.append(max_geodes)

print(max_geodes_list[0] * max_geodes_list[1] * max_geodes_list[2])