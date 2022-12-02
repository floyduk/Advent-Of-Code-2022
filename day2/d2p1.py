input_file = open("day2/input.txt", "r")
input_lines = input_file.read().split("\n")

# This is where all the work is done. I precalculated the score for all the possible
# combinations. This lets me just use the whole line to lookup the score.
lookup = {
    'A X': 4,   # 1+3
    'A Y': 8,   # 2+6
    'A Z': 3,   # 3+0
    'B X': 1,   # 1+0
    'B Y': 5,   # 2+3
    'B Z': 9,   # 3+6
    'C X': 7,   # 1+6
    'C Y': 2,   # 2+0
    'C Z': 6,   # 3+3
}

# Total score is the running total score. Duh.
total_score = 0

# Iterate the lines in the file calculating the score as we go
for line in input_lines:
    total_score += lookup[line]

# Print the result
print(total_score)