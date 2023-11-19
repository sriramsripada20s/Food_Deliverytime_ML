# Import necessary libraries
import os, sys
from pathlib import Path
import logging

# Set up an infinite loop until a project name is provided
while True:
    project_name = input("Enter your Project Name: ")
    if project_name !="":
        break

# List of files to be created
#src/__init__.py
#src/components/__init__.py
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]


# Loop through each file path in the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object
    filedir, filename = os.path.split(filepath) # Split the file path into directory and file name

    # Checking if the directory is not empty (if directory exists)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True) # Create the directory if it doesn't exist
    
    # Check if the file doesn't exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass # Create an empty file
    else:
        logging.info("file is already present at : {filepath}") # Log a message if file already exists


#This code takes a project name as input and generates a structure of files and directories based on that name. 
# It iterates through a list of files, creates directories if needed, and generates empty files 
# if they don't exist or are empty. It also logs a message if a file already exists at the specified path.