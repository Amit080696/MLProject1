from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    This will return the list of requirements
    '''
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    return requirements

setup(
name ='mlproject',
version='0.0.1',
author='Amit Baghel',
author_email='amit.bharat999@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
