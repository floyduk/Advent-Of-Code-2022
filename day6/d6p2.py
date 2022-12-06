# open and read the input file
stream = open("day6/input.txt", "r").readline().rstrip()

# Soluton 1:
# Iterate through the string taking list slices of the string and comparing the length of that list 
# with the length of the same list cast into a set (which will remove duplicates). If the lengths
# are the same then the list contains no duplicates and we can print the position and end.
for i in range(14, len(stream)):
    if(len(stream[i-14:i]) == len(set(stream[i-14:i]))):
        print(i)
        break

# Solution 2:
# Just cause this was such an easy one I thought it might be fun to reduce this to a single line
print(sorted(list(set([(i if len(stream[i-14:i]) == len(set(stream[i-14:i])) else -1) for i in range(14, len(stream))])))[1])