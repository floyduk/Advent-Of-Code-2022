# open and read the input file
input_file = open("day7/input.txt", "r")
input_lines = input_file.read().split("\n")

# Lambda function to chop everything off after the last slash in string d
basename = lambda d : d[:d.rfind("/")]

current_line_number = 0     # Tracks the current input line we're working on
current_directory = "ROOT"  # The current working directory as a string
directory_sizes = {}        # A dictionary of directory names (key) and sizes (value)

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
            
            # We're only interested in files since only files have a size
            if(words[0] != "dir"):
                # Copy the current directory path and step backwards through it by chopping the last path element
                # off the end. Add this file size to every directory it's in.
                d = current_directory
                while(d != "ROOT"):
                    directory_sizes[d] = directory_sizes[d] + int(words[0]) if d in directory_sizes else int(words[0])
                    d = basename(d)
                directory_sizes[d] = directory_sizes[d] + int(words[0]) if d in directory_sizes else int(words[0])

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
            current_directory = "ROOT"
        elif parameter == "..":
            current_directory = basename(current_directory)
        else:
            current_directory += "/" + parameter

        # We've processed this line. Move on to the next
        current_line_number += 1

# Find directories that hold <= 100000 size. Sum the resulting list and print it.
suitable_directories = [d for d in directory_sizes.values() if d <= 100000]
print("Sum of size of directories holding <= 100000: " + str(sum(suitable_directories)))
