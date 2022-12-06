# open and read the input file
input_file = open("day6/input.txt", "r")
stream = input_file.readline().rstrip()

# Iterate through the string taking list slices of the string and comparing the length of that list 
# with the length of the same list cast into a set (which will remove duplicates). If the lengths
# are the same then the list contains no duplicates and we can print the position and end.
for i in range(4, len(stream)):
    if(len(stream[i-4:i]) == len(set(stream[i-4:i]))):
        print(i)
        break