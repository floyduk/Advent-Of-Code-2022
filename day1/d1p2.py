import fileinput

# elves_calories is an array of the total calories carried by each elf
elves_calories = []

# The current running total of calories carried by an elf
this_elf_calories = 0

# Iterate the list of calories adding numbers to this_elf_calories until we find a blank line
for line in fileinput.input(files="day1/input.txt"):
    line = line.rstrip()
    if line == "":
        # When we find a blank line we add the current running total to elves_calories array and start a new running total
        elves_calories.append(this_elf_calories)
        this_elf_calories = 0
    else:
        this_elf_calories += int(line)

# When we exit the loop we've still not added the last elf's total to the list. So do that now.
elves_calories.append(this_elf_calories)

# Sort the list of elves_calories and add th                                                                                                                                                                e top 3 numbers to get the answer
elves_calories.sort(reverse=True)
print(sum(elves_calories[0:3]))