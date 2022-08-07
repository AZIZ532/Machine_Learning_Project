from setuptools import find_packages, setup
from typing import List



#declaring variables for setup functions
Project_name = "housing-predictor"
Version = "0.0.2"
Author = "Abdul Aziz Khan"
Description = "This is my first machine learning end to end project"
Packages = ["housing"]
Requirement_file_name = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file
    
    return the package name which is used to install for this project
    """
    
    with open(Requirement_file_name) as requirement_file:
        requirement_file.readlines().remove("-e .")
setup (
    name=Project_name,
    version=Version,
    author=Author,
    description= Description,
    packages=find_packages(),
    install_requires = get_requirements_list()
)