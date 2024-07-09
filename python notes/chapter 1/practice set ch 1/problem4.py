import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories
        dir_contents = os.listdir(path)
        
        # Print the names of the files and directories
        for item in dir_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path
directory_path = '.'  # Current directory

# Call the function
print_directory_contents(directory_path)
