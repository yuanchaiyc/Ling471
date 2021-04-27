# Pathlib
# Import the module:
import pathlib
import sys
# Get the path to directory from outside:
d = pathlib.Path(sys.argv[1])

# Iterate over files:
for filename in d.iterdir():
    if filename.is_file() and filename.suffix == '.open':
        with open(filename, 'r') as f:
            print(f.read())

# Furthermore, iterate only over the valid stuff:

print("End")
