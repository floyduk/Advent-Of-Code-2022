from typing import NamedTuple

# open and read the input file
input_file = open("day7/input.txt", "r")
input_lines = input_file.read().split("\n")

# We're going to build a directory structure that consists of files and directories.
# Directories and files are represented using the NamedTuple types declared above. 
# Directories have a "contents" property that is a list of content elements.
current_line_number = 0     # Tracks the current input line we're working on
current_directory = "ROOT"  # The current working directory as a string
directory_sizes = {}        # A dictionary of directory names (key) and sizes (value)

# MAIN LOOP - Walk through the input_lines parsing the commands and output
while current_line_number < len(input_lines):
    words = input_lines[current_line_number].split()

    if(words[1] == "ls"):
        # Starting with the next line we'll be parsing a list of files and directories
        current_line_number += 1
        # Break out if we've reached the end of the input_lines
        if current_line_number >= len(input_lines):     
            break   

        # Keep iterating the input lines creating files and folders until we find a line that starts with a $
        while(input_lines[current_line_number][0] != "$"):
            # Turn this input line into words
            words = input_lines[current_line_number].split()
            
            # We're only interested in files since only files have a size
            if(words[0] != "dir"):
                # Copy the current directory path and step backwards through it by chopping the last path element
                # off the end. Add this file size to every directory it's in.
                d = current_directory
                while(d != "ROOT"):
                    directory_sizes[d] = directory_sizes[d] + int(words[0]) if d in directory_sizes else int(words[0])
                    d = d[:d.rfind("/")]
                directory_sizes[d] = directory_sizes[d] + int(words[0]) if d in directory_sizes else int(words[0])

            # We've processed this line. Move on to the next
            current_line_number += 1
            # Break out if we've reached the end of the input_lines
            if current_line_number >= len(input_lines):     
                break   

    else:
        # Change directory based on the parameter given
        parameter = words[2]
        if parameter == "/":
            current_directory = "ROOT"
        elif parameter == "..":
            current_directory = current_directory[:current_directory.rfind("/")]
        else:
            current_directory += "/" + parameter

        # We've processed this line. Move on to the next
        current_line_number += 1

# Calculate the sizes of all directories
total_available_space = 70000000
total_space_used = directory_sizes["ROOT"]
unused_space = total_available_space - total_space_used
space_required_for_update = 30000000
space_needing_to_be_freed = space_required_for_update - unused_space
print(f"\nTotal space used: {total_space_used}")
print(f"Unused space: {unused_space}")
print(f"Space needing to be freed: {space_needing_to_be_freed}")

# Sorry for the spaghetti code but this uses a list comprehension to select
# only the directories big enough to free sufficent space. It then sorts that
# list and selects the first(smallest) list item as our answer.
print("Smallest directory that frees enough space is: " + str(sorted([d for d in directory_sizes.values() if d >= space_needing_to_be_freed])[0]))