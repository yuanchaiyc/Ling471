from pathlib import Path

# Create a Path object to a folder on your computer and store it in a variable
p = Path()

# Add a subdirectory to that Path object
p = p / 'matt'

# Create a list of all files and folders in the path your object refers to
all_items = list(p.glob('*'))

# Create a list of only the files in the path your object refers to
all_files = [x for x in p.glob('*') if x.is_file()]

##################################################
# Showing a variety of ways of making lists
##################################################

# Create a list of only the files that have a docx file extension in the path your object refers to
all_docx = [x for x in p.glob('*.docx')]

# All PDFs
all_pdf = list(p.glob('*.pdf'))

# All py files
all_py = list(p.glob('*.py'))

# All jpg files
all_jpg = list() # or all_jpg = []
for x in p.glob('*.jpg'):
    all_jpg.append(x)
