from typing import NamedTuple

# open and read the input file
input_file = open("day7/input.txt", "r")
input_lines = input_file.read().split("\n")

# Using named Tuples to create types for directories and files
class Directory(NamedTuple):
    name: str
    contents: list
    parent: NamedTuple

class File(NamedTuple):
    name: str
    size: int

# We're going to build a directory structure that consists of files and directories.
# Directories and files are represented using the NamedTuple types declared above. 
# Directories have a "contents" property that is a list of content elements.
current_line_number = 0                 # Tracks the current input line we're working on
directory_tree = Directory("/", [], ()) # The root of our directory structure
current_directory = directory_tree      # The current working directory
directory_sizes = {}                    # Dictionary of directories and their sizes

# A function to Walk the tree and display it
def display_node(n, indent=""):
    if(type(n) == Directory):
        print(f"{indent} - {n.name} (dir)")
        for n in n.contents:
            display_node(n, "  " + indent)
    else: 
        print(f"{indent} - {n.name} (file, size={n.size})")

# A function to walk the tree calculating the sizes of each directory and then add it to 
# the global directory_sizes dictionary
def calc_directory_sizes(n, path="") -> int:
    size = 0

    # Iterate all the elements of this node summing the total size of this node
    for n in n.contents:
        if(type(n) == Directory):
            size += calc_directory_sizes(n, path+"/"+n.name)
        else:
            size += n.size

    # Store this directory path and size in the global directory_sizes dictionary
    directory_sizes[path] = size

    # Return the size of this directory to the caller
    return size


# MAIN LOOP - Walk through the input_lines parsing the commands and output
while current_line_number < len(input_lines):
    words = input_lines[current_line_number].split()

    # HANDLE ls LINES
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
            if(words[0] == "dir"):
                # Create a directory
                current_directory.contents.append(Directory(words[1], [], current_directory))
            else:
                # Create a file
                current_directory.contents.append(File(words[1], int(words[0])))
            
            # We've processed this line. Move on to the next
            current_line_number += 1
            # Break out if we've reached the end of the input_lines
            if current_line_number >= len(input_lines):     
                break   

    # HANDLE cd LINES
    else:
        # Change directory based on the parameter given
        parameter = words[2]
        if parameter == "/":
            current_directory = directory_tree
        elif parameter == "..":
            current_directory = current_directory.parent
        else:
            for item in current_directory.contents:
                if item.name == parameter:
                    current_directory = item

        # We've processed this line. Move on to the next
        current_line_number += 1

# Display the tree just because we did a load of work to build it and I want
# to see the fruits of all that work.
print("Directory tree:")
display_node(directory_tree)

# Calculate the sizes of all directories
total_available_space = 70000000
total_space_used = calc_directory_sizes(directory_tree)
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