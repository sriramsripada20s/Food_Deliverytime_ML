#This file is used to define how a Python package should be installed, packaged, and distributed.


## Import necessary functions/classes. Setuptools defines the metadata about the Python package such as its name, 
#version, description, author details, and dependencies required for installation.
from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "End to End ML project"
AUTHOR_NAME = "name"
AUTHOR_EMIL = "your@email.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

#get_requirements_list() function reads a requirements.txt file and return the required dependencies in list
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requriment_file: # Open the requirements file in read mode
        # Read all lines from the requirements file
        requriment_list = requriment_file.readlines() 
        # Strip the newline character from each line and create a list of requirements
        requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list] 

        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)

        return requriment_list

# Setup function to define package details
setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMIL,
      packages=find_packages(), # Automatically discover and include all packages
      install_requries = get_requirements_list()  # Define the package dependencies from requirements.txt
     )