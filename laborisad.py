import os

# Specify the path to the folder
path2 = "/path/to/folder"

# Check if the folder exists at the specified path
if os.path.exists(os.path.join(path2, folder)):
    status = "DUPLICADA"
else:
    status = "UNICA"
