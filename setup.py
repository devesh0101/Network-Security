from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""

    requirement_lst: List[str] = []
    try:
        with open('/Users/devesh/Documents/projects/Network security /requirement.txt', 'r') as file:
            #read all lines from the file
            lines = file.readlines()
            #process each line to remove whitespace and comments
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
                    print("requirements.txt file not found.")
                    
    return requirement_lst


setup(
    name='NetworkSecurityProject',
    version='0.0.1',
    author='Devesh Dhyani',
    author_email="devesh.dhyani0101@gmail.com",
    packages=find_packages(),  
    install_requires=get_requirements(),
)

                   