input_file = open("day2/input.txt", "r")
input_lines = input_file.read().split("\n")

# This is where all the work is done. I precalculated the score for all the possible
# combinations. This lets me just use the whole line to lookup the score.
# Part 2 is exactly the same. We can still pre-calculate the scores.
lookup = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

# Total score is the running total score. Duh.
total_score = 0

# Iterate the lines in the file calculating the score as we go
for line in input_lines:
    total_score += lookup[line]

# Print the result
print(total_score)